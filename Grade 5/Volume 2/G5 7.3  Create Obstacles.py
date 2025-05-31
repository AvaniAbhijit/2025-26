# create_obstacle() function is same as create_fruit() function. 
# Obstacles are black triangle shapes created in a random position.
# obstacle_list is a list which used to store the obstacles created.

# Task 1: Create an empty list called obstacle_list.
# Task 2: Write a function called create_obstacle() that:
#         Creates a new turtle object obstacle.
#         Sets its shape to "triangle".
#         Sets its color to "black".
#         Lifts the pen using penup().
#         Places it at a random x-coordinate between -350 and 350, and at a y-coordinate of 300.
#         Adds the new obstacle to the obstacles list.

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

#Write a function called create_obstacle()





game_on = True
while game_on:
    # This line gives a 1 in 20 chance to create a new fruit on each check
    if random.randint(1, 20) == 1:
        create_fruit()
    if random.randint(1, 40) == 1:         # Obstacles appear less frequently
        create_obstacle()            
    screen.update()
screen.mainloop()
