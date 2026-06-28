import os
import subprocess

def capture():
    filename = f"/tmp/shadow_cam_{int(os.times()[4])}.jpg"
    try:
        subprocess.run(["fswebcam", "-r", "640x480", filename], timeout=10, check=True)
        return filename
    except:
        return "Webcam capture failed"
