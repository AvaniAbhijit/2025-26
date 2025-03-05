# Lab Activity 3
# Change the following for the food object:
# ✅ move the food with penup() 
# ✅ make the food size smaller using shapesize(0.85, 0.85). 
# Note: Syntax: shapesize(height, width). By default, the shapesize is (1,1). 

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
head.penup()
head.goto(0,100)

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.color("red")

#todo: make the food size smaller by 0.75 times using shapesize()
#Hint: food.shapesize(width, height). By default, the shapesize is (1,1).


food.goto(100,0)
