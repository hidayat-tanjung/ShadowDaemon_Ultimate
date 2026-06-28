import subprocess
import os
import time

def record_screen(duration=30, with_audio=True):
    output_file = f"/tmp/shadow_rec_{int(time.time())}.mp4"
    
    if with_audio:
        cmd = f"ffmpeg -f x11grab -video_size 1920x1080 -i :0.0 -f pulse -i default -t {duration} {output_file}"
    else:
        cmd = f"ffmpeg -f x11grab -video_size 1920x1080 -i :0.0 -t {duration} {output_file}"
    
    subprocess.run(cmd, shell=True, timeout=duration+5)
    return output_file