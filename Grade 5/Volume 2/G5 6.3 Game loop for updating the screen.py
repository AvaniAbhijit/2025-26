# The while loop here is a game loop.
# It keeps running as long as the condition game_on is True.
# Inside the loop, screen.update() is called to refresh/redraw the game window continuously.
# This allows any changes you make (like moving the basket or falling fruits) to be shown live.
# The loop runs indefinitely because game_on is initially set to True and never changed inside the loop.

#Task 1: Run the code and observe the output.
#Task 2: Change the size and position of the basket.
#Task 3: Change game_on to False on line no 19.

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

# Set a flag to keep the game running
game_on = True

# Start the game loop
while game_on:
    # Update the screen continuously to reflect any changes
    screen.update()

# Keep the window open until the user closes it
screen.mainloop()
