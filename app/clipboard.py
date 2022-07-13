import pyperclip

# Windows
def copy_to_clipboard_win(data):
    pyperclip.copy(data)
    clip = pyperclip.paste()

# Mac
import subprocess

def copy_to_clipboard_mac(data):
    subprocess.run("pbcopy", universal_newlines=True, input=data)
