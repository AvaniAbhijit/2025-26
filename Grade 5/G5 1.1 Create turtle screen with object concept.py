# What is an Object?
# An object is a thing that has attributes (features) and functions (actions it can perform).

# What is an Object in a Turtle? 
# In Python's turtle module, an object is like a real turtle(turtle.screen()) that you can control on the screen 
# and set attributes like title, bgcolor, and setup.

# Task: Change the properties( title,bgcolor,and setup) of the object in the below code.


import turtle  # Import the turtle module, which provides graphics functions for drawing.

# turtle.Screen() creates and returns a screen object, which is used to control the window.
turtle.Screen().title("Snake Game")  # Sets the title of the window to "Snake Game".

turtle.Screen().bgcolor("Dark Green") # sets the background color of the screen to dark green.

turtle.Screen().setup(width=600, height=600) # sets the dimensions of the window to 600x600 pixels.
