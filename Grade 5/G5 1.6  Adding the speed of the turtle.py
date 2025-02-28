# control the speed of the turtle

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

#speed() - to control the speed of the turtle movement
#0-(fastest), 1-(slowest) to 10-(very fast)
head.speed(0)

head.penup()
head.goto(0,100)

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.goto(100,0)




