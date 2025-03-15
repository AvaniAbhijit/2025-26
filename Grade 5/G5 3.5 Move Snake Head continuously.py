# Define the direction property for the snake head on line 29.
# On line 56, function move_up() checks for the up arrow key to change the direction of the snake head to up.
# On line 70, function move_left() checks for the left arrow key to change the direction of the snake head to left.
# On line 38, move() function to set the new position based on the directions.
# Move the snake head continuously in the game loop by calling move() on line 93.


# Task 1 : Complete the code for move_down() on line 61 onwords.
# Task 2: Complete the code for move_right() on line 65 onwards.

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
        head.direction = "up"   #sets the direction of snake head to UP

# when down arrow key is pressed
def move_down():
    

# when right arrow key is pressed
def move_right():



# when left arrow key is pressed
def move_left():
    if head.direction != "right":
        head.direction = "left"    #sets the direction of snake head direction to LEFT


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

    move()  # Call move() to move the snake continously

    # Check for collision with the wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)       # reset the position of snake to center.

    time.sleep(delay)   #  Adds a small delay to control speed of snake head.
