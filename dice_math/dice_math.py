import datetime
import os
from random import sample, randint

dice = [
[1, 
"""
+-------+
|       |
|   O   |
|       |
+-------+
""",
],
[2,
"""
+-------+
| O     |
|       |
|     O |
+-------+
""",
],
[3,
"""
+-------+
| O     |
|   O   |
|     O |
+-------+
""",
],
[4, 
"""
+-------+
| O   O |
|       |
| O   O |
+-------+
""",
],
[5, 
"""
+-------+
| O   O |
|   O   |
| O   O |
+-------+
""",
],
[6, 
"""
+-------+
| O   O |
| O   O |
| O   O |
+-------+
""",
],
]

"""5 height, 9 width"""

print("""
Add up all the sides of all the dice displayed on the screen. You have
30 seconds to answer as many as possible. You get 4 points for each
correct answer and lose 1 point for each incorrect answer.
""")

end_time = datetime.datetime.now() + datetime.timedelta(seconds=30)
points = 0

while datetime.datetime.now() < end_time:
    display = """"""
    dice_amount = randint(2, 6)
    selected_dice = sample(dice, dice_amount)
    total = 0
    
    for line in range(0, 6):
        for current_dice in selected_dice:
            split_current_dice = current_dice[1].splitlines()
            display += split_current_dice[line]
        
        display += "\n"
    
    for current_dice in selected_dice:
        total += current_dice[0]
    
    print(display)            
    
    answer = input(">")
    
    while not answer.isnumeric():
        print("Please enter a number")
        answer = input(">")
    
    if int(answer) == total:
        points += 4
        print("Correct")
    else:
        points -= 1
        print("Incorrect, Answer: ", total)
    
    print("Points: ", points)

print("Times up!")
print("Points =", points)
