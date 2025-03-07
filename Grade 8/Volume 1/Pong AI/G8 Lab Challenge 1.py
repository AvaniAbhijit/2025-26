# Lab Challenge 1 :
# Task: Define the left and right paddle objects on lines 29 and 32,
#       ensuring they are vertically centered using rect_y from line 26.
# 1. Left Paddle: Position 20 pixels from the left edge.
# 2. Right Paddle: Position 20 pixels from the right edge (account for paddle width).
# 3. Use rect_width and rect_height for dimensions.

import pygame
pygame.init()

# Screen setup
screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Two Vertical Rectangles')

# Colors
BG_COLOR = (50, 25, 50)
WHITE = (255, 255, 255)

# Rectangle dimensions
rect_width = 20
rect_height = 100

# Positioning the rectangles at the vertical center
rect_y = (screen_height - rect_height) // 2

# Left rectangle (x = 20)
left_rect = pygame.Rect()

# Right rectangle (x = screen_width - 40)
right_rect = pygame.Rect()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    # Draw the rectangles
    pygame.draw.rect(screen, WHITE, left_rect)
    pygame.draw.rect(screen, WHITE, right_rect)

    pygame.display.update()

pygame.quit()
