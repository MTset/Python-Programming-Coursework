#!/usr/local/bin/python3

""" Clear screen for improved legibility """
import os
import sys

def clear():  
    host_platform = sys.platform

    if host_platform == "win32": # windows
        os.system('cls')
    else: # *nix and OS X
        os.system('clear')
        
clear()