# Define snake segments as an empty list on line 75.
# Create a new_segment turtle object on line 96 when the snake head collides with food.
# Append the new_segment to the segment list on line 100.


# Task 1: Complete the code for new_segment to set the following.
#           speed(0), shape("square"), color("grey"), penup()


import turtle
import time
import random

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
head.direction = "stop"     # define the direction property as stop at the beginning.

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.75, 0.75)

def move():
    if head.direction == "up":      #check if direction is up
        y = head.ycor()
        head.sety(y + 20)           #set the y coordinate to 20 pixels up (+20)

    if head.direction == "down":       #check if direction is down
        y = head.ycor()
        head.sety(y - 20)           #set the y coordinate to 20 pixels down (-20)

    if head.direction == "right":    #check if direction is right
        x = head.xcor()
        head.setx(x + 20)           #set the x coordinate to 20 pixels right (+20)

    if head.direction == "left":   #check if direction is left
        x = head.xcor()
        head.setx(x - 20)           #set the x coordinate to 20 pixels left (-20)

# when up arrow key is pressed
def move_up():
    if head.direction != "down":
        head.direction = "up"   #sets the direction of snake head direction to UP

# when down arrow key is pressed
def move_down():
    if head.direction != "up":
        head.direction = "down"  #sets the direction of snake head direction to DOWN

# when right arrow key is pressed
def move_right():
    if head.direction != "left":
        head.direction = "right"  #sets the direction of snake head direction to RIGHT

# when left arrow key is pressed
def move_left():
    if head.direction != "right":
        head.direction = "left"    #sets the direction of snake head direction to LEFT

# Define snake segments as a list
segments = []

#turtle listens for key press
t.listen()
t.onkey(move_up, "Up")
t.onkey(move_left, "Left")
t.onkey(move_down, "Down")
t.onkey(move_right, "Right")

# Infinite game loop
while True:
    t.update()          # ensures continuous updates of the screen.

    # Check for snake head collision with food
    if head.distance(food) < 15:
        # Move the food to a random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Create and add a segment to the snake
        new_segment = turtle.Turtle()


        
        segments.append(new_segment)

    move()  # Call move() to move the snake continously

    # Check for collision with the wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)       # reset the position of snake to center.

    time.sleep(delay)   #  Adds a small delay to control speed of snake head.

