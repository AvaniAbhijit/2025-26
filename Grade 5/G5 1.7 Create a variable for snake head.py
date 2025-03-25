# head is a variable name which is storing turtle.Turtle() object on line 13.
# turtle.Turtle() on line 13 creates a new turtle object.

# Task: Set the color of the 'head' turtle to black within the " " on line no. 16.

import turtle
t = turtle.Screen()
t.title("Snake Game")
t.bgcolor("Dark Green")
t.setup(width=600, height=600)

# Create a turtle object named 'head' that will represent the snake's head.
head = turtle.Turtle()
# Set the shape of the 'head' turtle to a square.
head.shape("square")
head.color("")
