"""FP32 normalization and residuals with compact per-stream conditioning.

The transformer has image, optional reference, and text modes. Keep one 3072
vector per mode instead of broadcasting three full token-by-channel matrices.
Only GEMM operands are rounded to FP16. Centered FP32 variance avoids the
cancellation of E[x²] - E[x]² on nearly constant residuals.
"""
import mlx.core as mx


NORM_SOURCE = r"""
    const uint row = threadgroup_position_in_grid.x;
    const uint tid = thread_index_in_threadgroup;
    const uint lane = tid % 32;
    const uint warp = tid / 32;
    float values[12];
    float total = 0;
    for (uint i = 0; i < 12; ++i) {
        values[i] = x[row * 3072 + tid + i * 256];
        total += values[i];
    }
    total = metal::simd_sum(total);
    threadgroup float sums[8];
    if (lane == 0) sums[warp] = total;
    threadgroup_barrier(mem_flags::mem_threadgroup);
    if (warp == 0) {
        total = metal::simd_sum(lane < 8 ? sums[lane] : 0.0f);
        if (lane == 0) sums[0] = total / 3072.0f;
    }
    threadgroup_barrier(mem_flags::mem_threadgroup);
    const float mean = sums[0];
    float square = 0;
    for (uint i = 0; i < 12; ++i) {
        values[i] -= mean;
        square += values[i] * values[i];
    }
    square = metal::simd_sum(square);
    threadgroup_barrier(mem_flags::mem_threadgroup);
    if (lane == 0) sums[warp] = square;
    threadgroup_barrier(mem_flags::mem_threadgroup);
    if (warp == 0) {
        square = metal::simd_sum(lane < 8 ? sums[lane] : 0.0f);
        if (lane == 0) sums[0] = metal::rsqrt(square / 3072.0f + 1e-6f);
    }
    threadgroup_barrier(mem_flags::mem_threadgroup);
    const float inv = sums[0];
    const uint mod = mode[row] * 3072;
    for (uint i = 0; i < 12; ++i) {
        const uint col = tid + i * 256;
        const float normalized = values[i] * inv;
        const float factor = 1.0f + scale[mod + col];
        const float result = factor * normalized + shift[mod + col];
        out[row * 3072 + col] = half(result / 256.0f);
    }
"""

RESIDUAL_SOURCE = r"""
    const uint i = thread_position_in_grid.x;
    if (i >= SIZE) return;
    const uint col = i % 3072, row = i / 3072;
    const float result = float(projected[i]) * 256.0f;
    out[i] = x[i] + gate[mode[row] * 3072 + col] * result;
"""


norm_kernel = mx.fast.metal_kernel(
    name="flux_scaled_modulate", input_names=["x", "shift", "scale", "mode"],
    output_names=["out"], source=NORM_SOURCE)
residual_kernel = mx.fast.metal_kernel(
    name="flux_compact_residual", input_names=["x", "projected", "gate", "mode"],
    output_names=["out"], source=RESIDUAL_SOURCE)


def normalized(x, shift, scale, mode):
    return norm_kernel(inputs=[x, shift, scale, mode], grid=(x.shape[0] * 256, 1, 1),
                       threadgroup=(256, 1, 1), output_shapes=[x.shape], output_dtypes=[mx.float16])[0]


def residual(x, projected, gate, mode):
    return residual_kernel(inputs=[x, projected, gate, mode], template=[("SIZE", x.size)],
                           grid=(x.size, 1, 1), threadgroup=(256, 1, 1),
                           output_shapes=[x.shape], output_dtypes=[mx.float32])[0]
