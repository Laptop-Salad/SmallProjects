"""
Carrot in a Box

A game for two players. Each player has a box. One box has a carrot in it, and each 
player wants to have the carrot. The first player looks and their box and tells the second player if they have the carrot or not.
The second player can decide to keep or swap their box.
"""

from random import randint
import keyboard

print("Carrot in a Box")

# Get player names
player_one = input("Human player 1, enter your name: ")
player_two = input("Human player 2, enter your name: ")

# Display closed boxes to players
print("HERE ARE TWO BOXES:")
print("""
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
{}             {}
""".format(player_one, player_two))

print("{}, you have a RED box in front of you.".format(player_one))
print("{}, you have a GOLD box in front of you.".format(player_two))
print("When {} has closed their eyes, press Enter...".format(player_two))

# Decide which box has the carrot, 1 for RED, 2 for GOLD
carrot = randint(1, 2)

# Wait for player_two to close their eyes
while True:
    try:
        if keyboard.is_pressed('enter'):
            break
    except:
        pass

# Display opened RED box to player_one
if carrot == 1:
    print("""
 _____VV____
 |    VV    |
 |    VV    |
 |____||____|    __________
 /    ||    /| /         /|
+---------+  |+---------+ |
|   RED   |  ||   GOLD  | |
|   BOX   | / |   BOX   | /
+---------+/  +---------+/
(carrot!)
{}             {}
    """.format(player_one, player_two))
else:
    print("""
   _________
  |         |
  |         |
  |_________|    __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
 (no carrot!)
{}              {}
    """.format(player_one, player_two))

# Wait for player_one to continue
print("Press space to continue")

while True:
    try:
        if keyboard.is_pressed('space'):
            break
    except:
        pass

# Display 200 empty lines to prevent player_two from seeing player_one's box
for line in range(0, 200):
    print()

print("{} can open their eyes now".format(player_two))

# Ask if player_two wishes to keep/swap their box
print("{}, do you want to (s)wap or (k)eep your box?".format(player_two))
choice = input(">")

# Ensure choice is either 's' or 'k
while choice.lower() != "s" and choice.lower() != "k":
    print("Please enter 's' for swap or 'k' for keep")
    choice = input(">")

# Swap boxes if choice is 's'
if choice.lower() == "s":
    print("{} you decided to take the RED box".format(player_two))
    
    # Display winner
    if carrot == 1:
        print("The carrot is in the RED box, {} wins!".format(player_two))
    else:
        print("The carrot is in the GOLD box, {} wins!".format(player_one))
else:
    # If choice is 'k', don't swap
    print("{} you decided to keep your GOLD box".format(player_two))

    # Display winner
    if carrot == 1:
        print("The carrot is in the RED box, {} wins!".format(player_one))
    else:
        print("The carrot is in the GOLD box, {} wins!".format(player_two))
