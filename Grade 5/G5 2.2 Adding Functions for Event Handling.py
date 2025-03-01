#Functions for event handling

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

#function for up arrow key pressed
def move_up():
    # move the head up by 20 pixels

#function for left arrow key pressed
def move_up():
    # move the head left by 20 pixels


#turtle listens for key press
t.listen()
t.onkey(move_up, "Up")
t.onkey(move_left, "Left")
t.onkey(move_down, "Down")
t.onkey(move_right, "Right")

