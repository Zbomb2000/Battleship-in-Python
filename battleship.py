#Imports time delays, exit, and randomizing
import time
import random
import sys
#Welcomes the player
print("WELCOME to MINI PYTHON BATTLESHIP!")
#Starts the loop
start = 0
#Gives the player directions
print("Type 'START' to start, type 'HELP' for help.")
while start == 0:
    answerM = input("Type here: ")
#Tells the player the rules
    if answerM == "HELP":
        print("")
        print("This is the game Battleship, but it's about three times smaller and made in Python!")
        print("If you know how to play Battleship, then you can completely ignore this.")
        print("The object of Battleship is to try and sink all of the other player's ships before they sink all of your ships.")
        print("All of the other player's ships are somewhere on his/her board.")
        print("You try and hit them by calling out the coordinates of one of the squares on the board.")
        print("The other player also tries to hit your ships by calling out coordinates.")
        print("Neither you nor the other player can see the other's board so you must try to guess where they are.")
        print("Since the developer is too dumb to make full ships, you will have to hit 5 checkpoints placed on a random 3x3 grid.")
        print("Good luck...")
        print("")
#Starts the game
    elif answerM == "START":
        print("Starting game...")
        start = 2
    else:
        print("Please enter a valid command.")
time.sleep(1)
#Shows the player the grid
print("")
print("")
print("   1    2    3")
print("A")
print("")
print("B")
print("")
print("C")
#Sets up the player's grid
a1 = "-"
a2 = "-"
a3 = "-"
b1 = "-"
b2 = "-"
b3 = "-"
c1 = "-"
c2 = "-"
c3 = "-"
green = 0
while green < 1:
#Player chooses grid checkpoints
    checkpoint1 = input("Choose a grid point to place a checkpoint (no caps): ")
    checkpoint2 = input("Choose a grid point to place another checkpoint (no caps): ")
#Sets up the player's grid
    if checkpoint1 == "a1":
        a1 = "X"
        green = green + 1
    elif checkpoint1 == "a2":
        a2 = "X"
        green = green + 1
    elif checkpoint1 == "a3":
        a3 = "X"
        green = green + 1
        a3 = "X"
        green = green + 1
    elif checkpoint1 == "b1":
        b1 = "X"
        green = green + 1
    elif checkpoint1 == "b2":
        b2 = "X"
        green = green + 1
    elif checkpoint1 == "b3":
        b1 = "X"
    elif checkpoint1 == "c1":
        c1 = "X"
        green = green + 1
    elif checkpoint1 == "c2":
        c2 = "X"
        green = green + 1
    elif checkpoint1 == "c3":
        c3 = "X"
        green = green + 1

    if checkpoint2 == "a1":
        a1 = "X"
        green = green + 1
    elif checkpoint2 == "a2":
        a2 = "X"
        green = green + 1
    elif checkpoint2 == "a3":
        a3 = "X"
        green = green + 1
    elif checkpoint2 == "b1":
        b1 = "X"
        green = green + 1
    elif checkpoint2 == "b2":
        b2 = "X"
        green = green + 1
    elif checkpoint2 == "b3":
        b1 = "X"
        green = green + 1
    elif checkpoint2 == "c1":
        c1 = "X"
        green = green + 1
    elif checkpoint2 == "c2":
        c2 = "X"
        green = green + 1
    elif checkpoint2 == "c3":
        c3 = "X"
        green = green + 1
    else:
        print("Invalad grid points. Try again.")
#Sets up the player's attack grid
one = "-"
two = "-"
three = "-"
four = "-"
five = "-"
six = "-"
seven = "-"
eight = "-"
nine = "-"
#Sets up the attacker's checkpoint coordinates
attacker_coordinates = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
attacker = random.choice(attacker_coordinates)
attacker_checkpoint1 = attacker
attacker_coordinates.remove(attacker_checkpoint1)
attacker2 = random.choice(attacker_coordinates)
attacker_checkpoint2 = attacker2
#Game end and loop values
finish = 0
finishWin = 0
player_checkpoints = 2
#Loop
while finish < 1:
#Player's attack grid
    print("")
    print("")
    print("   1    2    3")
    print("A  "+one+"    "+two+"    "+three)
    print("")
    print("B  "+four+"    "+five+"    "+six)
    print("")
    print("C  "+seven+"    "+eight+"    "+nine)
    print("")
#Player's grid
    print("")
    print("   1    2    3")
    print("A  "+a1+"    "+a2+"    "+a3)
    print("")
    print("B  "+b1+"    "+b2+"    "+b3)
    print("")
    print("C  "+c1+"    "+c2+"    "+c3)
    answer = input("Type coordinates here (use capital letters): ")
    print("")
    print("")
#Attack grid markers
    if answer == "A1":
        one = "O"
    elif answer == "A2":
        two = "O"
    elif answer == "A3":
        three = "O"
    elif answer == "B1":
        four = "O"
    elif answer == "B2":
        five = "O"
    elif answer == "B3":
        six = "O"
    elif answer == "C1":
        seven = "O"
    elif answer == "C2":
        eight = "O"
    elif answer == "C3":
        nine = "O"
    else:
        print("Invalad answer or hit.")
#Registers hit or miss
    if answer == attacker_checkpoint1:
        finishWin = finishWin + 1
        print("HIT")
    elif answer == attacker_checkpoint2:
        finishWin = finishWin + 1
        print("HIT")
    else:
        print("MISS!")
#Checks for player victory
    if finishWin == 2:
        print("YOU WIN!")
        finish = 2
        sys.exit()
#Attacker attack
#Randomizes attack coordinates
    attack1 = ["a1",'a2','a3','b1','b2','b3','c1','c2','c3']
    attacker_attack = random.choice(attack1)
#Checks to see if attacker hit
    if attacker_attack == "a1":
        a1 = "!"
    elif attacker_attack == "a2":
        a2 = "!"
    elif attacker_attack == "a3":
        a3 = "!"
    elif attacker_attack == "b1":
        b1 = "!"
    elif attacker_attack == "b2":
        b2 = "!"
    elif attacker_attack == "b3":
        b3 = "!"
    elif attacker_attack == "c1":
        c1 = "!"
    elif attacker_attack == "c2":
        c2 = "!"
    elif attacker_attack == "c3":
        c3 = "!"
    else:
        print("Something went wrong.")
    if attacker_attack == checkpoint1:
        print("ATTACKER HIT!")
        print(attacker_attack)
        player_checkpoints = player_checkpoints - 1
        attack1.remove(attacker_attack)
    elif attacker_attack == checkpoint2:
        print("ATTACKER HIT!")
        print(attacker_attack)
        player_checkpoints = player_checkpoints - 1
        attack1.remove(attacker_attack)
    else:
        print("ATTACKER MISS!")
        attack1.remove(str(attacker_attack))
#Checks to see if player loses
    if player_checkpoints == 0:
        if finishWin != 2:
            print("Game over. You lose.")
        finish = 2
#End of loop
