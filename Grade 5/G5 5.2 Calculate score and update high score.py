# Update score and high score values upon snake head & food  collision on lines 114 to 116.
# Clear the text and display the new values on lines 119, 169.
# Reset the score when the snake head collides with itself on line 166 onwards.
# t.tracer(0) is a Turtle Graphics function that controls automatic screen updates on line 19.

# Task 1: Write the code for resetting the score when the snake head collides with a wall on line 149 onwards.

import turtle
import time
import random

delay = 0.1

# turtle screen functions
t = turtle.Screen()
t.title("Snake Game")
t.bgcolor("Dark Green")
t.setup(width=600, height=600)
t.tracer(0)
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
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()  # hide the turtle from the screen
pen.goto(0, 260)
# use write() to display score and high_score
pen.write(f"Score: 0 High Score: {high_score}", align="center", font=("Courier", 24, "normal")) 



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

# Infinte Game loop
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

        # Increase the score when collision happens
        score += 10
        if score > high_score:      # check if the current score is greater than high_score
            high_score = score      # set the high score to the current score

        # Update score display
        pen.clear()             # clear the previous score values
        pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))     


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
            segment.hideturtle()

        # Clear the segment list
        segments.clear()

        # Reset score
   


    # Check for collision with the snake itself
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.hideturtle()

            # Clear the segment list
            segments.clear()

            # Reset score
            score = 0
            pen.clear()
            pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal")) 



    time.sleep(delay)   #  Adds a small delay to control the speed of the snake head.





