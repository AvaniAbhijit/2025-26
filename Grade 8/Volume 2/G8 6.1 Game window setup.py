# The code creates a 400x600 game window titled "Sky Jumper" using Pygame.
# It runs a loop to keep the window open and listens for the close event.
# Each frame, it fills the screen with light blue and updates the display until the window is closed.


Task 1: Change the window title to your name.
Task 2: Change the background color to another RGB color, like yellow or pink.

import pygame  # Import the pygame module
pygame.init()  # Initialize all pygame modules

# Create the game window with width 400 and height 600
screen = pygame.display.set_mode((400, 600))

# Set the title of the game window
pygame.display.set_caption("Sky Jumper")

# Variable to control the game loop
run = True
while run:
    # Check for events like closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Fill the screen with a light blue color
    screen.fill((153, 217, 234))

    # Update the display with the latest changes
    pygame.display.update()

# Quit pygame when the loop ends
pygame.quit()
