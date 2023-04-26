"""
DNA Visualization
"""

"""
longest indents = 9

sequence:

1
3
5
6
6
5
3
1
0

#{letter}{- * sequence}{letter}#
"""
from random import randint
from time import sleep

def create_dna():
    """create one twisted ladder"""
    letters = [["A", "T"],["G", "C"]]

    # How many dashes
    sequence = [1, 3, 5, 6, 6, 5, 3, 1, 0]
    indents = [8, 7, 6, 5, 5, 6, 7, 8, 9]
    current_line = 0

    # Decide if indents should be different than original
    indents_change = randint(0, 2)
    if indents_change != 0:
        # If indent change amount should be added or minused
        minus = randint(0, 1)
        for elem in range(0, len(indents)):
            if minus:
                indents[elem] -= indents_change
            else:
                indents[elem] += indents_change

    # Print ladder
    for line in range(0, len(sequence)):
        if current_line == 8:
            print("{indents}##".format(
                indents = " " * indents[current_line]
            ))
        else:
            letter_set = letters[randint(0, 1)].copy()

            print("{indents}#{flet}{dashes}{slet}#".format(
                indents = " " * indents[current_line],
                flet = letter_set.pop(randint(0, 1)),
                dashes = "-" * sequence[current_line],
                slet = letter_set[0],
            ))

        current_line += 1

        # For each line wait
        sleep(0.5)

# Print ladders infinitely until stopped
print("Press Ctrl+C to quit.")
while True:
    try:
        create_dna()
    except KeyboardInterrupt:
        break
