#Give different color to different shape.
#Use list for it, so i can store the different color in the list.
from turtle import Turtle
import random

t= Turtle()
colors=["steel blue","lime","firebricks","bisque","darkviolet","olive","dark salmon","yellow"]
def draw(num_sides):
    for i in range(num_sides):
        angle = 360/num_sides
        t.forward(100)
        t.right(angle)
for shapes_side_n in range(3,11):
    t.color(random.choice(colors))
    draw(shapes_side_n)
