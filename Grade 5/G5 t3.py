#Explain how function works here.
from turtle import Turtle
t= Turtle()
def draw(num_sides):
    for i in range(num_sides):
        angle = 360/num_sides
        t.forward(100)
        t.right(angle)
draw(5)

