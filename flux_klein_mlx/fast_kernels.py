"""Small Metal kernels that avoid materializing full FP32 image activations.

All reductions use FP32. Attention remains global and group normalization uses
the complete image. Kernels run on the MLX stream and retain no tensor cache.
"""
from __future__ import annotations

import mlx.core as mx


_qkv_rope = mx.fast.metal_kernel(
    name="flux_qkv_rms_rope",
    input_names=["proj", "qw", "kw", "cosine", "sine"],
    output_names=["query", "key", "value"],
    source=r"""
        const uint lane = thread_position_in_threadgroup.x % 32;
        const uint row = thread_position_in_grid.x / 32;
        if (row >= TOKENS * 24) return;
        const uint token = row % TOKENS;
        const uint head = row / TOKENS;
        const uint base = token * 27648 + head * 128;
        float q[4], k[4];
        float qs = 0.0f, ks = 0.0f;
        for (uint i = 0; i < 4; ++i) {
            const uint d = (i / 2) * 64 + lane * 2 + i % 2;
            q[i] = float(proj[base + d]) * INPUT_SCALE;
            k[i] = float(proj[base + 3072 + d]) * INPUT_SCALE;
            qs += q[i] * q[i];
            ks += k[i] * k[i];
            value[row * 128 + d] = float(proj[base + 6144 + d]) * INPUT_SCALE;
        }
        const float qr = metal::rsqrt(metal::simd_sum(qs) / 128.0f + 1e-6f);
        const float kr = metal::rsqrt(metal::simd_sum(ks) / 128.0f + 1e-6f);
        for (uint i = 0; i < 2; ++i) {
            const uint pair = i * 32 + lane;
            const uint d = pair * 2;
            const float c = cosine[token * 64 + pair];
            const float s = sine[token * 64 + pair];
            const float qe = (q[2*i] * qr) * float(qw[d]);
            const float qo = (q[2*i+1] * qr) * float(qw[d+1]);
            const float ke = (k[2*i] * kr) * float(kw[d]);
            const float ko = (k[2*i+1] * kr) * float(kw[d+1]);
            query[row * 128 + d] = T(qe*c - qo*s);
            query[row * 128 + d+1] = T(qe*s + qo*c);
            key[row * 128 + d] = T(ke*c - ko*s);
            key[row * 128 + d+1] = T(ke*s + ko*c);
        }
    """,
)


def qkv_rms_rope(projected, query_weight, key_weight, cos, sin, *, output_dtype=None, input_scale=1):
    length = projected.shape[0]
    shape = (1, 24, length, 128)
    return _qkv_rope(inputs=[projected, query_weight, key_weight, cos, sin],
                     template=[("T", projected.dtype), ("TOKENS", length), ("INPUT_SCALE", input_scale)],
                     grid=(length * 24 * 32, 1, 1), threadgroup=(256, 1, 1),
                     output_shapes=[shape] * 3, output_dtypes=[output_dtype or projected.dtype] * 3)


_attention_mlp = mx.fast.metal_kernel(
    name="flux_attention_swiglu_pack",
    input_names=["attention", "projected"], output_names=["out"],
    source=r"""
        const uint i = thread_position_in_grid.x;
        if (i >= TOKENS * 12288) return;
        const uint token = i / 12288;
        const uint col = i % 12288;
        if (col < 3072) {
            out[i] = float(attention[((col / 128) * TOKENS + token) * 128 + col % 128]) / OUTPUT_DIVISOR;
        } else {
            const uint offset = token * 27648 + 9216 + col - 3072;
            const float gate = float(projected[offset]) * INPUT_SCALE;
            const float up = float(projected[offset + 9216]) * INPUT_SCALE;
            if (PRECISE) {
                out[i] = T(((gate / (1.0f + metal::exp(-gate))) * up) / OUTPUT_DIVISOR);
            } else {
                const T sigmoid = T(1.0f / (1.0f + metal::exp(-gate)));
                const T activated = T(gate * float(sigmoid));
                out[i] = T(float(activated) * up);
            }
        }
    """,
)


def attention_mlp_pack(attention, projected, *, precise=False, input_scale=1, output_divisor=1):
    length = projected.shape[0]
    return _attention_mlp(inputs=[attention, projected], template=[("T", projected.dtype), ("TOKENS", length), ("PRECISE", precise),
                          ("INPUT_SCALE", input_scale), ("OUTPUT_DIVISOR", output_divisor)],
                          grid=(length * 12288, 1, 1), threadgroup=(256, 1, 1),
                          output_shapes=[(length, 12288)], output_dtypes=[projected.dtype])[0]


_group_stats = mx.fast.metal_kernel(
    name="flux_group_stats",
    input_names=["x"], output_names=["stats"],
    source=r"""
        const uint tid = thread_position_in_threadgroup.x;
        const uint chunk = thread_position_in_grid.y;
        const uint group = thread_position_in_grid.z;
        const uint count = PIXELS * (CHANNELS / 32);
        const uint start = chunk * 1024 + tid;
        float sum = 0.0f;
        float values[4];
        for (uint i = 0; i < 4; ++i) {
            const uint j = start + i * 256;
            if (j < count) {
                const uint pixel = j / (CHANNELS / 32);
                const uint channel = group * (CHANNELS / 32) + j % (CHANNELS / 32);
                const float v = float(x[pixel * CHANNELS + channel]);
                values[i] = v;
                sum += v;
            }
        }
        sum = metal::simd_sum(sum);
        threadgroup float sums[8];
        threadgroup float squares[8];
        if (tid % 32 == 0) {
            sums[tid/32] = sum;
        }
        threadgroup_barrier(mem_flags::mem_threadgroup);
        if (tid < 32) {
            sum = metal::simd_sum(tid < 8 ? sums[tid] : 0.0f);
            if (tid == 0) {
                sums[0] = sum / float(min(1024u, count - chunk * 1024));
                stats[(group * CHUNKS + chunk) * 2] = sums[0];
            }
        }
        threadgroup_barrier(mem_flags::mem_threadgroup);
        const float mean = sums[0];
        float square = 0.0f;
        for (uint i = 0; i < 4; ++i) {
            if (start + i * 256 < count) {
                const float d = values[i] - mean;
                square += d * d;
            }
        }
        square = metal::simd_sum(square);
        if (tid % 32 == 0) squares[tid/32] = square;
        threadgroup_barrier(mem_flags::mem_threadgroup);
        if (tid < 32) {
            square = metal::simd_sum(tid < 8 ? squares[tid] : 0.0f);
            if (tid == 0) {
                stats[(group * CHUNKS + chunk) * 2 + 1] = square;
            }
        }
    """,
)

_group_apply = mx.fast.metal_kernel(
    name="flux_group_apply",
    input_names=["x", "mean", "inverse_std", "weight", "bias"],
    output_names=["out"],
    source=r"""
        const uint i = thread_position_in_grid.x;
        if (i >= SIZE) return;
        const uint channel = i % CHANNELS;
        const uint group = channel / (CHANNELS / 32);
        const float n = (float(x[i]) - mean[group]) * inverse_std[group];
        const T y = T(n * float(weight[channel]) + float(bias[channel]));
        if (SILU) {
            out[i] = T(float(y) / (1.0f + metal::exp(-float(y))));
        } else {
            out[i] = y;
        }
    """,
)


def group_norm(x, weight, bias, silu=False):
    if x.shape[0] != 1 or x.shape[-1] % 32:
        raise ValueError("The VAE group kernel expects batch 1 and 32 channel groups")
    channels = x.shape[-1]
    pixels = x.shape[1] * x.shape[2]
    count = pixels * (channels // 32)
    chunks = (count + 1023) // 1024
    stats = _group_stats(inputs=[x],
                         template=[("CHANNELS", channels), ("PIXELS", pixels), ("CHUNKS", chunks)],
                         grid=(256, chunks, 32), threadgroup=(256, 1, 1),
                         output_shapes=[(32, chunks, 2)], output_dtypes=[mx.float32])[0]
    counts = mx.minimum(1024, count - mx.arange(chunks, dtype=mx.float32) * 1024)
    mean = mx.sum(stats[:, :, 0] * counts, axis=1) / count
    # Merge centered chunk variances. E[x²]-E[x]² is unstable for almost
    # constant groups and would turn a minor precision change into a large one.
    variance = mx.sum(stats[:, :, 1] + counts * mx.square(stats[:, :, 0] - mean[:, None]), axis=1) / count
    inverse = mx.rsqrt(variance + 1e-6)
    return _group_apply(inputs=[x, mean, inverse, weight, bias],
                        template=[("T", x.dtype), ("CHANNELS", channels), ("SIZE", x.size), ("SILU", silu)],
                        grid=(x.size, 1, 1), threadgroup=(256, 1, 1),
                        output_shapes=[x.shape], output_dtypes=[x.dtype])[0]
