#check_collision() function checks for collisions between the basket and fruits/obstacles On line 78.
#from line 79 to 83 checks if any fruit touches the basket.
# If a fruit is close enough, it hides the fruit, removes it from the list,

# Task : Write the code from line 85 to check - if any obstacles touches the basket.
#         If a obstacle is close enough, it hides the obstacle, removes it from the obstacle_list.

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
    for fruit in fruits:
        fruit.sety(fruit.ycor() - 10)
        if fruit.ycor() < -300:
            fruit.hideturtle()
            fruits.remove(fruit)

# Function to move all the fruits downward
def move_obstacle():
    for obstacle in obstacle_list:
        obstacle.sety(obstacle.ycor() - 10)
        if obstacle.ycor() < -300:
            obstacle.hideturtle()
            obstacle_list.remove(obstacle)

# Function to check for collisions between the basket and fruits/obstacles
def check_collision():
    # Check collision with fruits
    for fruit in fruits:
        if fruit.distance(basket) < 50:  # If fruit is close to the basket
            fruit.hideturtle()            # Hide the fruit
            fruits.remove(fruit)          # Remove it from the fruits list
    # Check collision with obstacles






game_on = True
while game_on:
    time.sleep(0.05)
    if random.randint(1, 20) == 1:
        create_fruit()
    if random.randint(1, 40) == 1:
        create_obstacle()
    move_fruits()
    move_obstacle()
    check_collision()
    screen.update()
screen.mainloop()
