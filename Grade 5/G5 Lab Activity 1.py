# Lab Activity 1:
# Create a food object for the snake game.
#✅ Create a new turtle object with the variable name food.
#✅ food.shape will be a circle.
#✅ food.color will be red.


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
head.color("black")
