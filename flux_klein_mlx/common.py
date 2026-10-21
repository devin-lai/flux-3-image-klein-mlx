"""Small runtime utilities; no conversion dependencies."""
import ctypes
import json
import os
from pathlib import Path


def physical_footprint():
    """Kernel-accounted process footprint, including Metal allocations on UMA.

    rusage_info_v4 layout from the installed macOS SDK's sys/resource.h.
    Unlike RSS this reports the memory charged to the process, and its true
    lifetime peak does not depend on our polling interval.
    """
    libproc = ctypes.CDLL("/usr/lib/libproc.dylib")
    buffer = ctypes.create_string_buffer(16 + 35 * 8)
    if libproc.proc_pid_rusage(os.getpid(), 4, ctypes.byref(buffer)) != 0:
        raise OSError("proc_pid_rusage(RUSAGE_INFO_V4) failed")
    values = (ctypes.c_uint64 * 35).from_buffer(buffer, 16)
    return {"physical_footprint_bytes": values[7], "peak_physical_footprint_bytes": values[28]}


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")
