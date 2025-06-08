# The player moves left or right when the arrow keys are pressed by changing its x position.
# When the spacebar is pressed, the player jumps up by decreasing their y position (moves upward).

# Task 1: Write the code to move the player right on line 37.

import pygame  # Import the pygame module
pygame.init()  # Initialize all pygame modules

# Create the game window with a width of 400 and a height of 600
screen = pygame.display.set_mode((400, 600))

# Set the title of the game window
pygame.display.set_caption("Sky Jumper")

# Create a rectangle representing the player at position (180, 500) with width 40 and height 50
player = pygame.Rect(180, 500, 40, 50)

# Variable to control the game loop
run = True
while run:
    # Limit the frame rate
    pygame.time.delay(30)

    # Check for events like closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get all keys pressed
    keys = pygame.key.get_pressed()

    # Move player left
    if keys[pygame.K_LEFT]:
        player.x -= 5

    # Move player right


	
    # Jump when spacebar is pressed (move up once)
    if keys[pygame.K_SPACE]:
        player.y -= 50  # Move player up

    # Fill the screen with a light blue color
    screen.fill((153, 217, 234))

    # Draw the player as a red rectangle on the screen
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Update the display with the latest changes
    pygame.display.update()

# Quit pygame when the loop ends
pygame.quit()
