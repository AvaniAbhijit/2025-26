# On  line 22, we print the event to check the screen coordinates.

# Task: Run the code and move the mouse on the output screen to check the screen coordinates.

import pygame
pygame.init()

screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong AI Game')

# Define colors
BG_COLOR = (50, 25, 50)  # Dark purple background
WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)

    # Fill the background color
    screen.fill(BG_COLOR)

    # Update display
    pygame.display.update()

pygame.quit()
