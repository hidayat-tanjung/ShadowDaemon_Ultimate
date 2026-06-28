#!/usr/bin/env python3
"""
Keylogger for Termux - Dummy Mode
イズミー Active 😈🔥
"""

import os
import time
import threading
import random
import string

LOG_FILE = "/tmp/.keylog_shadow"
is_running = False

def dummy_loop():
    global is_running
    words = [
        "hello", "world", "password", "admin", "root",
        "test", "user", "login", "email", "secret",
        "terminal", "command", "python", "script", "hack"
    ]
    while is_running:
        try:
            word = random.choice(words)
            for char in word:
                if not is_running:
                    break
                with open(LOG_FILE, 'a') as log:
                    log.write(char)
                time.sleep(random.uniform(0.05, 0.2))
            if random.random() < 0.3:
                with open(LOG_FILE, 'a') as log:
                    log.write(' ')
            elif random.random() < 0.1:
                with open(LOG_FILE, 'a') as log:
                    log.write('\n')
            time.sleep(random.uniform(0.5, 2))
        except:
            time.sleep(1)

def start():
    global is_running
    if is_running:
        return "Keylogger already running"
    is_running = True
    thread = threading.Thread(target=dummy_loop, daemon=True)
    thread.start()
    return "Keylogger started (Dummy mode)"

def stop():
    global is_running
    is_running = False
    return "Keylogger stopped"

def get_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return f.read()
    return "No logs found"
