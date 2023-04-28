import os
import keyboard
from time import sleep

width = int(os.get_terminal_size().columns) - 1

grid = [[" " for column in range(0, width)] for row in range(0, 20)]

def display_grid():
    print("Press WASD to move")
    for line in grid:
        print(''.join(line))

# Show starting position
grid[0][0] = "#" 
current_position = [0, 0]

display_grid()

try:
    while True:
        event = keyboard.read_event()

        # UP
        if event.name == "w":
            try:
                current_position[0] -= 1

                if current_position[0] < 0:
                    current_position[0] = 0
                    continue

                grid[current_position[0]][current_position[1]] = "#"
            except:
                current_position[0] += 1
                continue
        # LEFT
        elif event.name == "a":
            try:
                current_position[1] -= 1

                if current_position[1] < 0:
                    current_position[1] = 0
                    continue

                grid[current_position[0]][current_position[1]] = "#"
            except:
                current_position[1] += 1
                continue
        # DOWN
        elif event.name == "s":
            try:
                current_position[0] += 1

                if current_position[0] > 20:
                    current_position[0] = 20
                    continue

                grid[current_position[0]][current_position[1]] = "#"
            except:
                current_position[0] -= 1
                continue
        # RIGHT
        elif event.name == "d":
            try:
                current_position[1] += 1

                if current_position[1] > width:
                    current_position[1] = width
                    continue

                grid[current_position[0]][current_position[1]] = "#"
            except:
                current_position[1] -= 1
                continue
    
        sleep(1)
        os.system("cls")
        display_grid()
except KeyboardInterrupt:
    pass
