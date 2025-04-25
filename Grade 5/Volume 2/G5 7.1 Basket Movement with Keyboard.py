# move_left is a function defined on line 26 to move the basket when left arrow is pressed.
# From line 38 to 44 - This code helps the program listen to keyboard keys.
#                      When you press the left or right arrow key,
#                      the basket will move left or right on the screen.

# Task 1: Write the move_right() function on line 31 to move the basket when right arrow is pressed.
#         Get current x position and add 50 units to move right
#         Check if the new position is within 350 then,
#         Set the new x position for the basket

import turtle
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

# Function to move the basket to the left
def move_left():
    x = basket.xcor() - 50  # Get current x position and move 50 units left
    if x > -350:            # Check if the new position is within the left boundary
        basket.setx(x)      # Set the new x position for the basket







# Start listening for keyboard events
screen.listen()

# Bind the left arrow key to the move_left function
screen.onkey(move_left, "Left")

# Bind the right arrow key to the move_right function (assumes move_right is defined elsewhere)
screen.onkey(move_right, "Right")

game_on = True
while game_on:
    screen.update()
screen.mainloop()
