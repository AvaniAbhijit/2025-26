# move_fruits() function on line 67 moves each fruit down using a for loop.
# On line 69, each fruit's y-coordinates changed by 10 pixels.
# If a fruit goes below the bottom of the screen (y = -300)on line 70,
# it is hidden and removed from the list to keep the game clean on lines 71 & 72.
# The time module in Python provides functions to work with time, such as pausing the program (sleep).

#Task 1: Create a similar function called move_obstacle() that:
#        Moves each obstacles down by 10 pixels.
#        If an obstacle goes below the bottom of the screen (y = -300),
#        It is hidden and removed from the obstacle_list to keep the game clean.


import turtle
import random
import time
screen = turtle.Screen()
screen.title("Fruit Catcher Game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)
screen.tracer(0)

basket = turtle.Turtle()
basket.shape("square")
basket.color("brown")
basket.shapesize(1,5)
basket.penup()
basket.goto(0, -250)

# Function to move the basket to the left
def move_left():
    x = basket.xcor() - 50
    if x > -350:
        basket.setx(x)

def move_right():
    x = basket.xcor() + 50
    if x < 350:
        basket.setx(x)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

fruits=[]
fruit_colors =["red", "yellow", "green", "orange"]

def create_fruit():
    fruit = turtle.Turtle()
    fruit.shape("circle")
    fruit.color(random.choice(fruit_colors))
    fruit.penup()
    fruit.goto(random.randint(-350, 350), 300)
    fruits.append(fruit)

#Create an empty list called obstacle_list.
obstacle_list=[]
#Write a function called create_obstacle()
def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.shape("triangle")
    obstacle.color("black")
    obstacle.penup()
    obstacle.goto(random.randint(-350, 350), 300)
    obstacle_list.append(obstacle)

# Function to move all the fruits downward
def move_fruits():
    for fruit in fruits:  # Loop through each fruit in the fruits list
        fruit.sety(fruit.ycor() - 10)  # Move the fruit 10 units downward
        if fruit.ycor() < -300:  # If the fruit falls below the screen (y-coordinate < -300)
            fruit.hideturtle()   # Hide the fruit from the screen
            fruits.remove(fruit) # Remove the fruit from the fruits list








game_on = True
while game_on:
    time.sleep(0.05)   # Pause the program for 0.05 seconds to control the speed of the game's updates
    # This line gives a 1 in 20 chance to create a new fruit on each check
    if random.randint(1, 20) == 1:
        create_fruit()
    if random.randint(1, 40) == 1:
        create_obstacle()
    move_fruits()
    move_obstacle()
    screen.update()
screen.mainloop()
