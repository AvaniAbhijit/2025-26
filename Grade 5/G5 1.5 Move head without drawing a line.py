# We can use the following functions of the turtle to solve the above problem of not drawing while moving the turtle to a different position. 
# penup() 🖊️ (Pick up the pen) – The turtle moves without drawing.
# pendown() 🖊️ (Put the pen down) – The turtle starts drawing again.

# Task: Move the food without drawing a line 

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

#penup() - helps head turtle to move to (0,100) without drawing a line
head.penup()
head.goto(0,100)

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.color("red")






