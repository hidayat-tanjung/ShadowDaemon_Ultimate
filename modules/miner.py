import os
import subprocess

def start(wallet, pool):
    if not os.path.exists("./xmrig"):
        subprocess.run(["wget", "https://github.com/xmrig/xmrig/releases/latest/download/xmrig-linux-x64.tar.gz"], check=True)
        subprocess.run(["tar", "-xzf", "xmrig-linux-x64.tar.gz"], check=True)
    cmd = f"./xmrig -o {pool} -u {wallet} -k --threads=4 &"
    subprocess.Popen(cmd, shell=True)
    return "Miner started"

def stop():
    os.system("pkill xmrig")
    return "Miner stopped"
