# score_display.write sets up a text display at the top of the screen
# to show the player's score on line 34.
# The update_score() function updates this text every time the score changes,on line 105.

#Task 1: Set the text color to black for score_display turtle on line 28.
#Task 2: Lift the pen so it doesn't draw lines on line 29.
#Task 3: Move the turtle to (0, 260) - the top center of the screen on line 30.

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

# Create a turtle object to display the score
score_display = turtle.Turtle()
score_display.hideturtle()  # Hide the turtle shape (we only want the text to show)
                        # Set the text color to black
                        # Lift the pen so it doesn't draw lines
                        # Move the turtle to the top center of the screen
score_display.write("Score: 0", align="center", font=("Arial", 24, "normal"))  # Write initial score text


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
    global score
    # Check collision with fruits
    for fruit in fruits:
        if fruit.distance(basket) < 50:  # If fruit is close to the basket
            fruit.hideturtle()            # Hide the fruit
            fruits.remove(fruit)          # Remove it from the fruits list
            score+=1
    # Check collision with obstacles
    for obstacle in obstacle_list:
        if obstacle.distance(basket) < 50:  # If fruit is close to the basket
            obstacle.hideturtle()            # Hide the fruit
            obstacle_list.remove(obstacle)
            score-=1


# Define a function to update the score on screen
def update_score():
    score_display.clear()  # Clear the previous score
    # Write the updated score
    score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

game_on = True
score=0
while game_on:
    time.sleep(0.05)
    if random.randint(1, 20) == 1:
        create_fruit()
    if random.randint(1, 40) == 1:
        create_obstacle()
    move_fruits()
    move_obstacle()
    check_collision()
    update_score()
    screen.update()
screen.mainloop()
