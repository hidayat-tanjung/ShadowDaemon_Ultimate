import subprocess

def execute(command):
    try:
        result = subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOUT,
            timeout=30, text=True
        )
        return result if result else "Command executed (no output)"
    except Exception as e:
        return f"Error: {str(e)}"
