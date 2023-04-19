"""
Conway's Game of Life

A 2d array with cells

Rules:
1. Living cells with two or three neighbours stay alive
2. Dead cells with exactly three neighbours become alive
3. Any other cell dies/stays dead

The simulation will stop if there have been no changes to the grid in 1 iteration.
"""

from sys import stdout as terminal
from time import sleep
from itertools import cycle
from threading import Thread
import os

print("Do not resize window while program is running")

def get_alive_neighbours(grid, row, column):
    """Gets all alive neighbours around a cell

    Args:
        grid (str): 2d grid of dead/alive cells
        row (int): row that current cell is on
        column (int): column that current cell is on

    Returns:
        _type_: _description_
    """
    alive_neighbours = 0
    
    for x in range(row-1, row+2):
        for y in range(column-1, column+2):
            try:
               if grid[x][y] == '0':
                   if x == row and y == column:
                       pass
                   else:
                       alive_neighbours += 1
            except:
                pass
    
    return alive_neighbours
    

def start_simulation(grid: list):
    """Simulates conways game of life

    Args:
        grid (str): 2d grid of dead/alive cells
    """
    changes = False

    # How many neighbours does a living cell have
    for row in range(0, len(grid)):
        for column in range(0, len(grid[row])):
            # If a column is alive
            if grid[row][column] == '0': 
                # Get neighbours
                alive_neighbours = get_alive_neighbours(grid, row, column)
                
                if alive_neighbours < 2 or alive_neighbours > 3:
                    grid[row][column] = ' '
                    changes = True
                    
            # If a column is dead
            else:
                alive_neighbours = get_alive_neighbours(grid, row, column)
                
                if alive_neighbours == 3:
                    grid[row][column] = '0' 
                    changes = True
    
    sleep(1)
    draw_grid(grid)  
        
    if changes:
        start_simulation(grid)

def draw_grid(grid):
    """draws a grid to stdout

    Args:
        grid (str): a 2d grid of dead/alive cells
    """
    os.system('cls')
    for row in grid:
        for cell in row:
            terminal.write(cell)
        
        terminal.write("\n")
    
        
def create_grid():    
    """Initialise 2d grid[row][column]
    """
    size =os.get_terminal_size()
    columns = int(size.columns)
    rows = int(size.lines)
    
    grid = [[' ' for i in range(columns - 1)] for j in range(int((rows / 2) - 2))]
    
    # Set alive cells
    grid[1][1] = '0'
    grid[1][0] = '0'
    grid[1][2] = '0'
    grid[0][1] = '0'
    grid[0][0] = '0'
    
    draw_grid(grid)
    
    # Set rows, columns to new height
    rows = (rows / 2) - 2
    columns = columns - 1

    start_simulation(grid)

if __name__ == '__main__':
    create_grid()
