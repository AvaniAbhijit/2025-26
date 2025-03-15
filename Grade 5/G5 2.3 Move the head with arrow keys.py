# ycor() returns the current y-coordinate of the turtle on the screen on line 32.
# new_y is the new coordinate of the y, which is changed to 20 pixels up(+) on line 33.
# sety() moves the turtle to the given y-coordinate without changing its x-coordinate on line 34.

# Task: Based on move_up function body, write a similar function body for:
#       move_down(), move_right() and move_left() functions.

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

#when up arrow key pressed, increase y coordinate
def move_up():
    cur_y = head.ycor()   # get the current y coordinate of the head
    new_y = cur_y + 20    # change the y coordinate to 20 pixels up(+).
    head.sety(new_y)      # set the head to new y coordinate

#when left arrow key pressed, decrease x coordinate by 20 pixels
def move_left():
    pass

#when down arrow key pressed, decrease y coordinate by 20 pixels
def move_down():
    pass

#when right arrow key pressed, increase x coordinate by 20 pixels
def move_right():
    pass

#Event handling for arrow keys pressed
t.listen()
t.onkey(move_up, "Up")
t.onkey(move_left, "Left")
t.onkey(move_down, "Down")
t.onkey(move_right, "Right")
