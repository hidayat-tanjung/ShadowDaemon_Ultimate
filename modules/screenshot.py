import os
import subprocess

def capture():
    filename = f"/tmp/shadow_scr_{int(os.times()[4])}.png"
    try:
        subprocess.run(["scrot", filename], timeout=5, check=True)
    except:
        try:
            subprocess.run(["import", "-window", "root", filename], timeout=5, check=True)
        except:
            return "Screenshot failed"
    return filename
