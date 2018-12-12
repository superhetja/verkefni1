from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command


PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

def clear_screen():
    '''Clears the terminal screen.'''
    command = "-cls" if system_name().lower()=="windows" else "clear"
    system_call(command)

clear_screen()
print(BOLD + 'Hello World' + END)
x = input('> ')
clear_screen()
print(RED + 'Hello World' + END)