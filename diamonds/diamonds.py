"""
Diamonds
"""

# Get input for size of diamond and if diamond should be outlined or not
print("Enter size of diamond")
size = input(">")

while not size.isnumeric() or int(size) <= 0:
    print("Please enter a size greater than 0")
    size = input(">")
    
print("Should the diamond be an outline Y/N")
outline = input(">")

while outline.lower() != "y" and outline.lower() != "n":
    print("Please enter 'Y' for yes or 'N' for no")
    outline = input(">")
    
size = int(size)

"""
/\\
\\/

Diamond generation is based on the following variables (based on first half of diamond, second half is reversed):
1. spaces outside of diamond = starts at size * 2 and decreases by 1
2. spaces inside of diamond = starts at 0, doubles
"""
height = size * 2
total_spaces_out = size - 1
total_spaces_in = (size - 1) * 2
spaces_out = total_spaces_out
spaces_in = 0
characters_between = [' ', ' ']

# If outline spaces in-between should be another diamond
if outline.lower() == "y":
    characters_between[0] = '/'
    characters_between[1] = '\\'

# Print first half
for line in range(0, int(height / 2)):
    print("{}/{}{}\\".format(' ' * spaces_out, characters_between[0] * int(spaces_in / 2), characters_between[1] * int(spaces_in / 2)))
    spaces_out -= 1
    spaces_in += 2

# Print second half
spaces_out = 0
spaces_in = total_spaces_in
 
for line in range(0, int(height / 2)):
    print("{}\\{}{}/".format(' ' * spaces_out, characters_between[1] * int(spaces_in / 2), characters_between[0] * int(spaces_in / 2)))
    spaces_out += 1
    spaces_in -= 2
