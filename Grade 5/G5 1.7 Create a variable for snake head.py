# head is a variable name which is storing turtle.Turtle() object.

# Task: Set the color for the head on line 16.

import turtle
t = turtle.Screen()
t.title("Snake Game")
t.bgcolor("Dark Green")
t.setup(width=600, height=600)

# Create a turtle object named 'head' that will represent the snake's head.
head = turtle.Turtle()
# Set the shape of the 'head' turtle to a square.
head.shape("square")
# Set the color of the 'head' turtle to black.
head.color("")
