# What is a Variable?
# On line 13, t is a variable that is used to store the turtle.Screen() object.

# Why do we use variables?
# We use variables so we can store information and use it later in our programs. 
# Such as we used t later on line 17 and so on.

# Task: Change the variable name t to "t1".


import turtle  # Import the turtle module, which provides graphics functions for drawing.

# Create a screen object using the turtle.Screen() function and assign it to variable 't'.
t = turtle.Screen()

# Set the title of the game window to "Snake Game".
t.title("Snake Game")

# Set the background color of the window to "Dark Green".
t.bgcolor("Dark Green")

# Set the size of the window to 600 pixels wide and 600 pixels high.
t.setup(width=600, height=600)
