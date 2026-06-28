import os
import subprocess

def record(duration=10):
    filename = f"/tmp/shadow_mic_{int(os.times()[4])}.wav"
    try:
        subprocess.run(["arecord", "-d", str(duration), "-f", "cd", "-t", "wav", filename],
                      timeout=duration+5, check=True)
        return filename
    except:
        return "Microphone recording failed"
