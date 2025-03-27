# screen.fill on line 27 is used to give the screen color.
# BG_COLOR on line 17 is a tuple variable contaning RGB values.
# A tuple is a Python datatype that is an ordered list of elements within round brackets ().

# Task 1: Create a RED tuple variable on line 18 with value (255,0,0).
# Task 2 :Change the screen color to RED.

import pygame
pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Maze Game')

# Define colors
BG_COLOR = (255, 255, 255)  # White background


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background color
    screen.fill(BG_COLOR)

    # Update display
    pygame.display.update()

pygame.quit()
