# Lab Activity 2
# Move the food object in the snake game
# ✅ move it horizontally left
# ✅ move it vertically down.


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
head.goto(0,100)

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.color("red")

