import os
from random import randint
from time import sleep

print("""
Deep Cave
Press Ctrl+C to stop.
""")

width = int(os.get_terminal_size().columns)
gap_length = 10
first_half_length = int((((width / 2) - (gap_length / 2)) - 5))
second_half_length = int((((width / 2) - (gap_length / 2)) + 5))

try:
    while True:
        first_change = randint(0, 2)
        second_change = randint(0, 2)
        
        # Randomly decide whether first_half_length will increase, decrease or stay the same
        match first_change:
            case 1:
                first_half_length -= 1
                gap_length += 1
            case 2:
                first_half_length += 1
                gap_length -= 1
            case _:
                pass
        
        # Randomly decide whether second_half_length will increase, decrease or stay the same  
        match second_change:
            case 1:
                second_half_length -= 1
                gap_length += 1
            case 2:
                second_half_length += 1
                gap_length -= 1
            case _:
                pass
        
        # Ensure first_half_length, second_half_length and gap_length does not go below 1
        if first_half_length <= 0:
            first_half_length += 2
            gap_length -= 2
        
        if second_half_length <= 0:
            second_half_length += 2
            gap_length -= 2
        
        if gap_length <= 0:
            gap_length += 2
            second_half_length -= 1
            first_half_length -= 1
        
        sleep(0.1)  
        print("{}{}{}".format("#" * first_half_length, 
                            " " * gap_length, 
                            "#" * second_half_length))
                
except KeyboardInterrupt:
    pass
