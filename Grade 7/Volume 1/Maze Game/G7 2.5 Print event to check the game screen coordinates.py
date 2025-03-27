# On  line 21, we print the event to check the screen coordinates.

# Task: Run the code and move the mouse on the output screen to check the screen coordinates.

import pygame
pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Maze Game')

# Define colors
WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)

    # Fill the background color
    screen.fill(WHITE)

    # Update display
    pygame.display.update()

pygame.quit()
