import socket
import time

class PortKnocking:
    def __init__(self, secret_sequence=[7000, 8000, 9000]):
        self.secret_sequence = secret_sequence
    
    def knock(self, target_ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect_ex((target_ip, port))
            sock.close()
            return True
        except:
            return False
    
    def stealth_knock(self, target_ip, ports=None):
        if not ports:
            ports = self.secret_sequence
        for port in ports:
            self.knock(target_ip, port)
            time.sleep(0.5)
        return "Knock sent"
    
    def run_client(self, target_ip, command="open"):
        if command == "open":
            return self.stealth_knock(target_ip)
        else:
            return self.stealth_knock(target_ip, self.secret_sequence[::-1])