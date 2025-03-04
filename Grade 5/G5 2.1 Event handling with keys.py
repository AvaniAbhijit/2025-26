# What is Event handling?
# Event handling is making the computer respond when you press a key, 
# click the mouse, or do an action.

# Why are we using event handling in this game?
# To move the snake head using the keyboard key. turtle.listen()
# It makes sure the program is ready to detect key presses. : turtle.onkey() 
# t.onkey(function_name, "Key") binds a key press to a function. 
# Function_name is the name of the function that is called when a particular “Key” is pressed

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
food.penup()
food.goto(100,0)
food.speed(0)
food.shapesize(0.75, 0.75)

#turtle listens for key press
t.listen()

#when up arrow key is pressed, it calls move_up() function
t.onkey(move_up, "Up")       # Press ↑ to move up

#when left arrow key is pressed, it calls move_left() function
t.onkey(move_left, "Left")   # Press ← to move left


