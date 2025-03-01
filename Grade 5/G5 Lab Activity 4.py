#Task: - write the code for todo below

import turtle

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
food.goto(100,0)
food.speed(0)
food.shapesize(0.75, 0.75)

#turtle listens for key press
t.listen()
t.onkey(move_up, "Up")       # Press ↑ to move up
t.onkey(move_left, "Left")   # Press ← to move left

#todo: write onkey() for down arrow key, call move_down() function

#todo: write onkey() for right arrow key, call move_right() function

