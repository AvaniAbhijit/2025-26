# What is an Object?
# turtle.Screen() is an object in the below code that creates the game screen.
# .title ,.bgcolor, and .setup are the attributes of the turtle.Screen() object.

# Task: Change the value of the attributes( title,bgcolor, and setup) of the object in the below code.


import turtle  # Import the turtle module, which provides graphics functions for drawing.

# turtle.Screen() creates and returns a screen object, which is used to control the window.
turtle.Screen().title("Snake Game")  # Sets the title of the window to "Snake Game".

turtle.Screen().bgcolor("Dark Green") # sets the background color of the screen to dark green.

turtle.Screen().setup(width=600, height=600) # sets the dimensions of the window to 600x600 pixels.
