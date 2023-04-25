"""
Digital stream
"""
import os
from random import randint

characters = ["0", "1"]
grid = """"""
# width-1 to prevent newline
width = int(os.get_terminal_size().columns) - 1
streams = []

# Generate streams
# Create columns that span the length of the screen
for column in range(0, width):
    stream_length = randint(1, 19)
    stream = [" " for i in range(0, 19)]

    # Decide if column should be blank or a stream
    stream_type = randint(1, 3) 
    for character in range(0, stream_length):
        # If column should be a stream, randomly replace stream (up to stream_length) with either "1" or "0"
        if stream_type == 2:
            stream[character] = characters[randint(0, 1)]
    
    streams.append(stream)
current_char = 0

# Add streams to all_lines which acts as a grid
all_lines = [[] for i in range(0, 20)]
current_line_num = 0

for stream in streams:
    for char in stream:
        all_lines[current_line_num].append(char)
        current_line_num += 1
    
    current_line_num = 0

# Print grid
for line in all_lines:
    print(''.join(line))
