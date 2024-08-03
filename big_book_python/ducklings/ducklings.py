"""
Ducklings

("= 
(v )
 ^^  
"""

import os
from random import randint
from time import sleep

small_duck_temp = """ ("=  
(v ) 
 ^^   
"""

# Split small_duck_temp into a 2d list
small_duck_temp = small_duck_temp.splitlines()
for char in range(0, len(small_duck_temp)):
    small_duck_temp = list(small_duck_temp)

width = int(os.get_terminal_size().columns) - 1
# Generate grid with width rows and 20 columns
grid = [[" " for column in range(0, width)] for row in range(0, 20)]

try:
    placements_tried = 0
    while True:
        # Randomly get where to place duck in grid
        column = randint(0, width-3)
        row = randint(0, 20-2)

        has_space = True

        # Ensure that based on row, column there is enough space to place duck
        try:
            for line in range(row, row+3):
                for char in range(column, column+4):
                    if grid[line][char] != " ":
                        has_space = False
                        break
        except:
            has_space = False
        
        # If there is space, place duckling
        if has_space:
            duck_line = 0
            duck_char = 0
            for line in range(row, row+3):
                duck_char = 0
                for char in range(column, column+4):
                    grid[line][char] = small_duck_temp[duck_line][duck_char]
                    duck_char += 1

                duck_line += 1

            sleep(1)
            os.system("cls")
            for line in grid:
                print(''.join(line))
            print("Press Ctrl+C to quit.")
        else:
            placements_tried += 1
        
        # If failed attempts to place duckling is 5, reset grid
        if placements_tried == 5:
            for line in range(0, len(grid)):
                for char in range(0, len(grid[line])):
                    grid[line][char] = " "
            
            placements_tried = 0
except KeyboardInterrupt:
    pass
