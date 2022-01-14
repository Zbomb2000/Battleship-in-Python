#!/usr/bin/python3

# Importing libraries
print("[PROGRAM] Importing libraries...")
print()

import random
import sys
import os
import time

print("Starting...")

# This gets the current directory
cd = os.path.dirname(__file__)
raw_cd_var = r"{}".format(cd)

def installLibrary():
    # Attempts to install the library
    try:
        os.system("pip3 install pyautogui")
        print()
        print("'pyautogui' was successfully installed! Please relaunch the program for the changes to take effect")
        print("IMPORTANT: If it says 'attempt failed', this is an error that I can't figure out how to fix.")
        print("[EXIT] Exiting program...")
        print()
        time.sleep(2)
        sys.exit()
    except:
        print()
        print("Attempt failed. You will have to install 'colorama' manually.")
        print("[EXIT] Exiting program...")
        print()
        time.sleep(2)
        sys.exit()


try:
    import pyautogui as pygui
except:
    installLibrary()


# Welcomes the player
print("WELCOME to MINI PYTHON BATTLESHIP!")

# Main menu
menu = pygui.confirm("Welcome to\nMINI BATTLESHIP (in Python)\nBy: Zbomb2000", buttons=["START", "EXIT"])
if menu == "START":
    pass
elif menu is None or menu == "EXIT":
    sys.exit()
