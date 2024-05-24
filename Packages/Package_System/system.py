import platform
from os import system

def clear_screen():
    os_name = platform.system()
    if os_name == "Windows":
        clear_screen()
    else:
        system("clear")
