# Adding the Game loop to update the snake game screen continuously.
# t.update() on line 68 refreshes the screen to show the latest changes.
# time.sleep(delay) on line 69 pauses the program for a few seconds to make the animation smoother.
# Note: delay is declared as a variable on line 13 as 0.1 seconds.

# Task 1: Add an infinite while loop on line 67 for the screen to update continuously.
# Task 2: Uncomment lines 68 and 69 to see the output.


import turtle
import time

delay = 0.1

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
food.shapesize(0.75, 0.75)

#function for up arrow key pressed
def move_up():
    cur_y = head.ycor()   # get the current y coordinate of the head
    new_y = cur_y + 20    # change the y coordinate to 20 pixels up(+).
    head.sety(new_y)      # set the head to new y coordinate

#function for left arrow key pressed
def move_left():
    cur_x = head.xcor()   # get the current x coordinate of the head
    new_x = cur_x - 20    # change the x coordinate to 20 pixels left(-).
    head.setx(new_x)      # set the head to new x coordinate

#function for down arrow key pressed
def move_down():
    cur_y = head.ycor()   # get the current y coordinate of the head
    new_y = cur_y - 20    # change the y coordinate to 20 pixels down(-).
    head.sety(new_y)      # set the head to new y coordinate

#function for left arrow key pressed
def move_right():
    cur_x = head.xcor()   # get the current x coordinate of the head
    new_x = cur_x + 20    # change the x coordinate to 20 pixels right(+).
    head.setx(new_x)      # set the head to new x coordinate

#turtle listens for key press
t.listen()
t.onkey(move_up, "Up")
t.onkey(move_left, "Left")
t.onkey(move_down, "Down")
t.onkey(move_right, "Right")

# Infinite game loop

#    t.update()          # ensures continuous updates of the screen.
#    time.sleep(delay)   # Adds a small delay to control the speed of the snake head.
