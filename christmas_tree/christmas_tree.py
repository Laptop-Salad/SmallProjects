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

def christmas_tree(height, topper_select):
    topper_name = ["star", "angel", "bow"]
    topper = ["*", "&", "%"]

    # Get height
    if height < 0:
        print("Please enter a height greater than 0")

    # Get topper        

    if topper_select < 0 or topper_select > 2:
        print("Please enter a valid number")

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

christmas_tree(5, 1)



