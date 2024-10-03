#!/usr/bin/env python
from platform import system
from os import getppid, kill
import signal

menu = input('Start or Check?: ').lower()
while True:
    if menu == 'start':
        from main import main
        break
    elif menu == 'check':
        from main import faction_checker
        break
    else:
        print('Answer correctly!')
if system() == 'Linux':
    kill(getppid(), signal.SIGHUP)
