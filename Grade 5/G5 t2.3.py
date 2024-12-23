#Understand angle calculation
from turtle import Turtle
t= Turtle()
num_sides = 7
for i in range(num_sides):
    angle = 360/num_sides
    t.forward(100)
    t.right(angle)

