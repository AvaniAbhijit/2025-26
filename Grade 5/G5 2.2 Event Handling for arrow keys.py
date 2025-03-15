# Event Handling for arrow keys
# t.listen(): on line 38, turtle screen starts listening for key press. Works with onkey() function.
# t.onkey(): on line 39, calls a function move_up() when UP arrow key is pressed.
# move_up() function is defined on line 32. Currently, it does nothing but pass.

# Task 1: Write similar onkey() functions for Down, Left and Right arrow keys.
# Task 2: Write the corresponding move_down(), move_left() and move_right() functions.

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
food.shapesize(0.75, 0.75)
food.penup()

#function for up arrow key pressed
def move_up():
    pass

# Task 2: define move_down(), move_up() and move_right functions

#Event handling for arrow keys pressed
t.listen()                  # turtle listens for key press
t.onkey(move_up, "Up")      # Calls move_up() when up arrow key is pressed

# Task 1: onkey() functions for Down, Right and Left arrow keys
