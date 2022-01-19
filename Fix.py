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


# This function makes sure the player entered a valid point
def validatePoint(input_var):
    if input_var == "a1" or input_var == "a2" or input_var == "a3":
        return True
    elif input_var == "b1" or input_var == "b2" or input_var == "b3":
        return True
    elif input_var == "c1" or input_var == "c2" or input_var == "c3":
        return True
    else:
        return False


# Creates the grid
main_grid = {"a1": 0, "a2": 0, "a3": 0, "b1": 0, "b2": 0, "b3": 0, "c1": 0, "c2": 0, "c3": 0}
attack_grid = {"a1": 0, "a2": 0, "a3": 0, "b1": 0, "b2": 0, "b3": 0, "c1": 0, "c2": 0, "c3": 0}

print("")
print("")
print("   1    2    3")
print("A")
print("")
print("B")
print("")
print("C")

# This is where the player chooses their points
while True:
    # Point 1
    checkpoint1 = pygui.prompt("Choose a grid point to place a checkpoint (Examples: 'a2', 'b1'): ")
    # Validates point
    if validatePoint(checkpoint1.lower()):
        break
    else:
        pygui.alert("Invalid point. Try again.")

while True:
    # Point 2
    checkpoint2 = pygui.prompt("Choose a grid point to place another checkpoint: ")
    # Validates point
    if validatePoint(checkpoint2.lower()):
        break
    else:
        pygui.alert("Invalid point. Try again.")
