# How does the turtle move?
# The goto(x, y) function in the turtle module moves the turtle directly to a specific position on the screen using coordinates (X, Y). 
# Example: turtle.goto(100,50) moves the turtle right to X = 100 and up to Y = 50
# turtle.goto(-50,-100) moves the turtle left to X = -50 and down to Y = -100. Line 21 moves the head turtle 100 pixels up along the Y coordinate 


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
