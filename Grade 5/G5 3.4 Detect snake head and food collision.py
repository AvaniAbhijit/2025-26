# Detect snake head and food collision by checking the distance between the food and snake head objects.
# distance() on line 73 computes the distance between the current (x, y) positions of snake head and food objects.
# The random module is used to fetch random values for the x and y coordinates of food on lines 75 & 76.
# The width and height of the screen is 600 pixels. Hence, left/down is -300 and right/up is +300 from the  center.
# For left and right wall collision, we check if head.xcor()is within the range -290 and 290 on line 80.
# If the snake head collides with the left or right wall, then move the snake back to the center on line 81.

# Task: Write the code for up and down wall collision on line 80. 
#        Hint: for up and down wall: head.ycor() must be within the range -290 and 290

import turtle
import random
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
    cur_y = head.ycor()
    new_y = cur_y + 20
    head.sety(new_y)

#function for left arrow key pressed
def move_left():
    cur_x = head.xcor()
    new_x = cur_x - 20
    head.setx(new_x)

#function for down arrow key pressed
def move_down():
    cur_y = head.ycor()
    new_y = cur_y - 20
    head.sety(new_y)

#function for left arrow key pressed
def move_right():
    cur_x = head.xcor()
    new_x = cur_x + 20
    head.setx(new_x)

#turtle listens for key press
t.listen()
t.onkey(move_up, "Up")
t.onkey(move_left, "Left")
t.onkey(move_down, "Down")
t.onkey(move_right, "Right")

# Main game loop
while True:
    t.update()

    # Check for collision with food
    if head.distance(food) < 15:                # checking the distance between food and head
        # Move the food to a random position
        x = random.randint(-290, 290)           # random value for x coordinate
        y = random.randint(-290, 290)           # random value for y coordinate
        food.goto(x, y)                         # move the food to the random position

   # Check for Wall collision
    if head.xcor() > 290 or head.xcor() < -290 :
        head.goto(0, 0)  # Move the snake back to the center

    time.sleep(delay)
