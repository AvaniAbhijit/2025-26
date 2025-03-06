# The main loop in a Pygame program keeps the game running.
# It repeats again and again until the player decides to quit.
# We need event handling to listen to the player clicks.
# if player clicks "X" then game quits as on line 20 and 21.

import pygame
pygame.init()

screen_width = 600
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Main loop
while True:

    # Check for User Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Quit Pygame
            exit()        # Exit the program
    # Update display
    pygame.display.update()

