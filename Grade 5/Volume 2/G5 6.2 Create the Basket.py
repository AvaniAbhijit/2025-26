# basket = turtle.Turtle() creates the basket object that the player will control.
# basket.shape("square") will change the turtle's shape to a square.
# basket.shapesize(stretch_wid=1, stretch_len=5) resize the turtle to make it look like a rectangular basket.

# Task 1: Change the shape basket to a square.
# Task 2: Change the basket color to brown.   
# Task 3: Lift the basket(basket.penup()) to prevent drawing lines.


import turtle
screen = turtle.Screen()
screen.title("Fruit Catcher Game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the basket turtle
basket = turtle.Turtle()                  # Create a basket object.
                                          # Task 1: Change the shape basket to a square.
                                          # Task 2: Change the basket color to brown.
#using basket.shapesize(stretch_wid=1, stretch_len=5) to stretch the square into a rectangle.
basket.shapesize(stretch_wid=1, stretch_len=5)  #  Resize to look like a rectangle
                                          # Task 3: Lift the basket(basket.penup()) to prevent drawing lines.
basket.goto(0, -250)                      #  Move basket to bottom of screen.
screen.update()                           # Manually refreshes the screen since automatic updates are off.
