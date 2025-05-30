# create_fruit function creates a random fruit with random colours & random position from line 48 onwards.
# random is a Python module that has functions to generate random numbers. To use it, import it on line 13.
# random.choice(fruit_colors) picks one color randomly from fruit_colors list on line 51.
# random.randint(-350, 350) randomly picks an X position (left to right) on line 53.
# The Y position 300 means the fruit starts high up on the screen (top area)  on line 53.
# on line 59, random.randint randomly creates a fruit with a 1 in 20 chance during each iteration.


# Task 1: Create an empty list (fruits) to store fruit objects on line 44.
# Task 2: Define a list of possible fruit_colors ["red", "yellow", "green", "orange"] on line 46.

import turtle
import random

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

# Create an empty list to store fruit objects

# Define a list of possible fruit colors

# Function to create a fruit
def create_fruit():
    fruit = turtle.Turtle()                        # Create a new turtle object for the fruit
    fruit.shape("circle")                          # Set the shape of the fruit to a circle
    fruit.color(random.choice(fruit_colors))       # Choose a random color from the list and apply it
    fruit.penup()                                  # Prevent the fruit from drawing lines as it moves
    fruit.goto(random.randint(-350, 350), 300)     # Place the fruit at a random x-position at the top
    fruits.append(fruit)                           # Add the fruit to the fruits list

game_on = True
while game_on:
    # This line gives a 1 in 20 chance to create a new fruit on each check
    if random.randint(1, 20) == 1:
        create_fruit()
    screen.update()
screen.mainloop()
