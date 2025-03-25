# Declared score and high_score variables on line 36 & 37 .
# Created pen turtle object to show text - score and high_score on screen on line 39.
# Use write() to display score and high_score on line 47.

# Task: Write the code for setting the following properties of pen turtle  on line 40 onwards:
# speed(0), shape("square"), color("white"), penup(),hideturtle(), goto(0, 260) 

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

# Score and high score variables
score = 0
high_score = 0

pen = turtle.Turtle()






# use write() to display score and high_score
pen.write(f"Score: 0 High Score: {high_score}", align="center", font=("Courier", 24, "normal"))     # Use f-string to display the high_score value.

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
    head.direction = "up"   #sets the direction of snake head to UP

# when down arrow key is pressed
def move_down():
    head.direction = "down"  #sets the direction of snake head to DOWN

# when right arrow key is pressed
def move_right():
    head.direction = "right"  #sets the direction of snake head to RIGHT

# when left arrow key is pressed
def move_left():
    head.direction = "left"    #sets the direction of snake head to LEFT

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
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the snake segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()      # x coordinate of the previous segment
        y = segments[index - 1].ycor()      # y coordinate of the previous segment
        segments[index].goto(x, y)          # move the current segment to the previous segment position

    if len(segments) > 0:       # move the first segment
        x = head.xcor()         # x coordinate of first segment as head x coordinate
        y = head.ycor()         # y coordinate of first segment as head y coordinate
        segments[0].goto(x, y)  # set the position of first segment as head position

    move()  # Call move() to move the snake continously

    # Check for collision with the wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)       # reset the position of snake to center.
        head.direction = "stop"  #change the direction of head to stop on collision

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)   #moving segments to off-screen location

        # Clear the segment list
        segments.clear()

    # Check for collision with the snake itself
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segment list
            segments.clear()


    time.sleep(delay)   #  Adds a small delay to control speed of snake head.








