# penup() function of turtle on line 20 helps head turtle to move to (0,100) without drawing a line.

# Task 1: To move the food object without drawing a line, use the penup() function.
# Task 2: Move the food object to position (100,100) using goto(100,100) function. 

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






