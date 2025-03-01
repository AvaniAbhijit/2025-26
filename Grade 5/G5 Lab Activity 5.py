#Task: - write the code for todo below
#Apply the + or - operations on x or y coordinates accordingly.

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
    # get the current y coordinate of the head
    cur_y = head.ycor()

    #change the y coordinate of head
    #to move the head up by 20 pixels
    new_y = cur_y + 20

    #set the head to new y coordinate
    head.sety(new_y)


#function for left arrow key pressed
def move_up():
    #todo: write similar code like move_up()
    # to move the head left by 20 pixels


#function for left arrow key pressed
def move_down():
    #todo: write similar code like move_up()
    # to move the head down by 20 pixels


#function for right arrow key pressed
def move_right():
    #todo: write similar code like move_up()
    # to move the head right by 20 pixels


#turtle listens for key press
t.listen()
t.onkey(move_up, "Up")
t.onkey(move_left, "Left")
t.onkey(move_down, "Down")
t.onkey(move_right, "Right")

