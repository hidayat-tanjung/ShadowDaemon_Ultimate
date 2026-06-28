import os

def move_mouse(x, y):
    os.system(f"xdotool mousemove {x} {y}")
    return f"Moved mouse to ({x}, {y})"

def click_mouse(button=1):
    os.system(f"xdotool click {button}")
    return f"Clicked button {button}"

def type_text(text):
    os.system(f"xdotool type '{text}'")
    return f"Typed: {text}"