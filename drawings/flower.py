from turtle import *
from random import random

t = Turtle()
increase = 0
t.screen.tracer(False)
colours = [
    "black",
    "navy", 
    "blue", 
    "deep sky blue", 
    "light sea green",
    "yellow green",
    "yellow",
    "dark orange",
    "light salmon",
    "light coral"
]

for i in range(5):
    increase = 0
    
    for i in range(10):
        t.color(colours[i])
        t.circle(100 + increase, 90, 90)
        t.left(90)
        t.circle(100 + increase, 90, 90)

        t.penup()
        t.left(90)
        t.pendown()

        increase += 10

        t.pendown()
        
    t.left(135)
                
    t.right(45 + 20)
                    
    t.penup()
    t.pendown()
    
t.screen.update()
    
t.screen.exitonclick()
t.screen.mainloop()
