# penup() function of turtle on line 20 helps head turtle to move to (0,100) without drawing a line.


# Task: Move the food object using goto(100,100) and for without drawing a line using penup() function of turtle.. 

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






