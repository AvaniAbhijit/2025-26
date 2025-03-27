# pygame.draw.rect() is used to draw a rectangle shape on line 32.
# This method takes 3 parameters:
#   - where to draw: the screen object
#   - Color of the shape: WHITE
#   - rectangular area : tuple : (x_coordinate, y_coordinate, width, height)
# The x and y coordinates are the values of the top left position of the rectangle

# Task 1: Change the position of the green rectangle on the game window 
#         from the center to the bottom left corner of the game window.
# Task 2: Draw one more rectangle on the top right corner of the screen with Color=BLUE 
#         and the same dimensions as the  green rectangle.

import pygame

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Maze Game')

WHITE=(255,255,255)
GREEN =(0,255,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    # Draws the white rectangle on screen at rect_x, rect_y
    pygame.draw.rect(surface=screen, color=GREEN, rect=(200,150,100,50))

    pygame.display.update()

pygame.quit()
