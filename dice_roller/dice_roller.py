from random import randint
import re

def format_dice_input(dice):
    issue = False
    try: 
        if "-" in dice:
            dice = re.split("d|-", dice)
            bonus_points = int(dice[2]) - (int(dice[2]) * 2)
        elif "+" in dice:
            dice = re.split("d|[+]", dice)
            bonus_points = int(dice[2])
        else:
            dice = re.split("d", dice)
            bonus_points = 0
        
        dice_sides = int(dice[1])
        dice_amount = int(dice[0])
    except:
        issue = True

    if not issue:
        return dice_sides, dice_amount, bonus_points

    while "d" not in dice or issue:
        print("Optional: [sides of dice]d-[points to minus] : 36d6-10")
        print("Optional: [sides of dice]d+[points to add]: 36d9+10") 
        dice = input(">")

# Get user input for dice
print("Dice Roller")
dice = input(">")
bonus_points = 0

# Check dice input to ensure correct format
while "d" not in dice.lower():
    print("Please enter a value using the format:")
    print("[sides of dice]d : 36d5, 1d6")
    print("Optional: [sides of dice]d-[points to minus] : 36d-10")
    print("Optional: [sides of dice]d+[points to add]: 36d+10")
    dice = input(">")

# Split dice input and ensure correct format
dice = format_dice_input(dice)
dice_sides = dice[0]
dice_amount = dice[1]
bonus_points = dice[2]

# Keep track of dices rolled and sum of those dices
dices = []
total = 0

# Roll dices
for current_dice in range(0, dice_amount):
    current_dice_roll = randint(1, dice_sides)
    dices.append(current_dice_roll)
    total += current_dice_roll

# Add bonus points
total += bonus_points

# Display answer
print("{} {}".format(total, dices))
