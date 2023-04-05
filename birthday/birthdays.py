"""
Birthday Paradox

Asks user for a number of how many random birthdays to generate.
Tells you in that pool how many birthdays were the same.
Runs 100,000 simulations and tells you how many times therw were matching birthdays.
"""

import datetime
import keyboard
from random import randint

def generate_birthdays(num: int) -> list:
    """generate num amount of random birthdays

    Args:
        num (int): amount of birthdays to randomly generate

    Returns:
        list[datetime]: birthdays
    """
    birthdays = []
    i = 0
    while i < num:
        month = randint(1, 12)
        thirty_one = [1, 3, 5, 7, 8, 10, 12]
        thirty = [4, 6, 9, 11]
        
        if month in thirty_one:
            day = randint(1, 31)
        elif month in thirty:
            day = randint(1, 30)
        elif month == 2:
            day = randint(1, 28)

        birthdays.append(datetime.datetime(
            2023,
            month,
            day
        ))
        
        i += 1
        
    return birthdays

def check_matching_birth(birthdays: list) -> int and list[str]:
    """checks a given birthdays list for matching birthdays

    Args:
        birthdays (list[datetime])

    Returns:
        int: amount of matching birthdays
        ist[str]: matching birthdays formatted, ex. Oct, 22
    """
    length = len(birthdays)
    unique_birthdays = set(birthdays)
    new_length = len(unique_birthdays)
    
    if length == new_length:
        return 0, [""]
    
    found = {}
    for birthday in unique_birthdays:
        found[birthday] = None
    
    matching = []
    matches = 0
    for birthday in birthdays:
        if found[birthday] is not None:
            matching.append("{} {}".format(birthday.strftime("%b"), birthday.day))
            matches += 1
        else:
            found[birthday] = 1
    
    return matches, matching

def calculate_chance(matches: int) -> float:
    """calculates the chance of a matching birthday

    Args:
        matches (int): matches in birthdays after 100,000 simulations

    Returns:
        float: chance of matching birthday
    """
    chance = round((matches / 100_000) * 100, 2)
    print(chance)
    return chance

def run_simulations(num: int) -> int:
    """runs 100,000 simulations of num birthdays

    Args:
        num (int): birthdays to generate

    Returns:
        int: matching birthdays
    """
    matches = 0
    total_simulations = 0
    
    print("{} simulations run...".format(total_simulations))
    
    for round in range(0, 10):
        for simulation in range(0, 10_000):
            birthdays = generate_birthdays(num)
            matching = check_matching_birth(birthdays)
            
            if matching[0] > 0:
                matches += 1
        
        total_simulations += 10_000
        print("{} simulations run...".format(total_simulations))
    
    return matches

def start_birthdays():
    print("Birthday Paradox")
    print("How many birthdays shall I generate? (Max 100, Min 2)")
    num_birthdays = int(input(">"))

    # Ensure num_birthdays is between 2 and 100 inclusive
    while num_birthdays < 2 or num_birthdays > 100:
        print("Please enter a number between 2 and 100 inclusive")
        num_birthdays = int(input(">"))
    
    # Generate num_birthdays birthdays
    birthdays = generate_birthdays(num_birthdays)

    # Format and stringify birthdays, ex. Oct 22, Jan 1...
    stringified_birthdays = []

    for i in birthdays:
        stringified_birthdays.append("{} {}".format(i.strftime("%b"), i.day))

    stringified_birthdays = ', '.join(stringified_birthdays)

    print("Here are {} birthdays:".format(num_birthdays))
    print(stringified_birthdays)

    # Find how many people have matching birthdays and print appropriate message
    duplicates = check_matching_birth(birthdays)

    if duplicates[0] == 0:
        print("In this simulation, no one had matching birthdays")
    elif duplicates[0] == 1:
        print("In this simulation, two people have a birthday on {}".format(duplicates[1][0]))
    elif duplicates[0] > 1 and len(duplicates[1]) == 1:
        print("In this simulation multiple people have a birthday on {}".format(duplicates[1][0]))
    else:
        print("In this simulation multiple people have birthdays on {}".format(', '.join(duplicates[1])))

    # Ensure user wants to start 100,000 simulations
    print("Generating {} random birthdays 100,000 times...".format(num_birthdays))
    print("Press Enter to begin or Escape to exit...")

    while True:
        if keyboard.is_pressed('enter'):
            break
        if keyboard.is_pressed("esc"):
            return
    
    # Run 100,000 simulations of num_birthdays
    matches = run_simulations(num_birthdays)
    chance = calculate_chance(matches)
    print("Out of 100,000 simulations of {} people, there was a\nmatching birthday in that group {} times. This means".format(num_birthdays, matches))
    print("that {} people have a {}%/ chance of\nhaving a mathching birthday in their group.".format(num_birthdays, chance))
    print("That's probably more than you would think!")
    

if __name__ == '__main__':
    start_birthdays()
