# Task 1: Create a turtle object named basket to catch falling fruits.

# Task 2: Change the shape of the turtle to a square.

# Task 3: Change the color of the basket.

# Task 4: Resize the turtle to make it look like a basket 
#         using basket.shapesize(stretch_wid=1, stretch_len=5) to stretch the square into a rectangle.

# Task 5: Lift the pen so it doesn’t draw when moving.

# Task 6: Move the basket to the bottom of the screen to (0, -250).

import turtle
screen = turtle.Screen()
screen.title("Fruit Catcher Game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)
screen.tracer(0)
