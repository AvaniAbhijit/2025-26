#RECAP : 
#turtle.Screen() creates a window where the game will be displayed on line 13.
#.tracer(0) turns off automatic screen updates to allow smoother animations when updated manually on line 20.
#The title and background color are set using .title(), .bgcolor().


# Task 1: Set the title of the window on line 14.
# Task 2: Set the background color on line 15.

# Import the turtle module
import turtle

screen = turtle.Screen()   # This creates the game window
                           # Sets the title at the top of the window
                           # Changes the background color of the window

# Set the window size
screen.setup(width=800, height=600)  # Sets the width and height of the game window

# Turn off automatic screen updates
screen.tracer(0)                    # Disables automatic updates to allow manual refreshing (smoother animations)
