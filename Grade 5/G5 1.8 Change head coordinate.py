# turtle.goto(0,100) moves the turtle up to Y = 100 on line 20.

# Task: Change the head position to -50 for the x-axis and 200 for the y-axis.


import turtle

# turtle screen functions
t = turtle.Screen()
t.title("Snake Game")
t.bgcolor("Dark Green")
t.setup(width=600, height=600)

# Snake Head
head = turtle.Turtle()
head.shape("square")
head.color("black")

#move the head turtle 100 pixels up along the Y coordinate
head.goto(0,100)

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
