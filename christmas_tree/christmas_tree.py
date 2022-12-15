# Christmas Trees

## Example
# Height: 5
# Topper: (number for bow)

"""
    %
    #
   ###
  #####
 #######
#########
   | |
"""

## Example
# Height: 2
# Topper: (number for star)

"""
 *
 #
###
| |
"""

topper_name = ["star", "angel", "bow"]
topper = ["*", "&", "%"]

# Get height
height = int(input("Height: "))

while height < 0:
    print("Please enter a number greater than 0")
    height = int(input("Height: "))


# Print list of toppers
for i in range(len(topper_name)):
    print("{number}: {topper}".format(number=i,topper=topper_name[i]))

# Get topper        
topper_select = int(input("Enter number for topper: "))

while topper_select < 0 or topper_select > 2:
    print("Please enter a valid number")
    topper_select = int(input("Enter number for topper: "))


bottom_row = (height - 1) + height

# Print topper
space = int(bottom_row / 2)
star = (" " * (space + 1) + topper[topper_select])
print(star)

# Print first row
print((" " * (space + 1) + "#"))


# Print body
amount = 1
for i in range(height - 1):
    space = space = int(bottom_row / 2) - i
    amount += 2
    print((" " * space) + ("#" * amount))
    

# Print trunk
space = int(bottom_row / 2)
print(" " * space + "| |")



