# On line 8, t is a variable that is used to store the turtle.Screen() object.

# Task 1: Change the variable name t to "t1" on line 9.
# Task 2: Run the code and observe the error and fic the error.

import turtle  # Import the turtle module, which provides graphics functions for drawing.

# Create a screen object using the turtle.Screen() function and assign it to variable 't'.
t = turtle.Screen()

# Set the title of the game window to "Snake Game".
t.title("Snake Game")

# Set the background color of the window to "Dark Green".
t.bgcolor("Dark Green")

# Set the size of the window to 600 pixels wide and 600 pixels high.
t.setup(width=600, height=600)
