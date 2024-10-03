from platform import system
import os

def clear():
    if system() == 'Windows':
        os.system('cls')
    elif system() == 'Linux':
        os.system('clear')
    else:
        print('Your operating system is not supported')
