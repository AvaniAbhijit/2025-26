# On line no 37 pygame.draw.rect() is used to draw a rectangle shape as a line.
# This method takes 3 parameters:
#   - where to draw: the screen object
#   - Color of the shape: WHITE
#   - rectangular area : tuple : (x_coordinate, y_coordinate, width, height)
# The x and y coordinates are the values of the top left position of the rectangle
# All these variables are defined from line no 21 to 28.

# Task: Draw a GREEN rectangle with the same dimensions as the WHITE rectangle and
#       touching the WHITE rectangle on the vertical side.

import pygame

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Maze Game')

WHITE=(255,255,255)
GREEN =(0,255,0)

# Rectangle position and dimension
rect_x = 200    # x coordinate where the rectangle starts
rect_y = 150    # y coordinate where the rectangle starts
rect_width = 100    # width of the rectangle
rect_height = 50    # height of the rectangle

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    # Draws the white rectangle on screen at rect_x, rect_y
    pygame.draw.rect(screen, GREEN, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.update()

pygame.quit()
