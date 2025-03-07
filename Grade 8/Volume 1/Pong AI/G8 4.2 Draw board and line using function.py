# On line 38,draw_board() is the function to draw the screen and margin line.
# The function is called inside the game while loop on line 51.
# margin value defined on line no 21.
# screen.fill(BG_COLOR) has been moved from while loop under draw_board function.
# pygame.draw.line is the method in pygame to draw the line on the screen.

# Task 1 : define the function draw() after draw_board() function.
# Task 2 : Move the line no 54 and 55 code into the above function body.
# Task 3 : Insted of the line 54,55 call the function draw().

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
margin=50

# Rectangle dimensions
rect_width = 20
rect_height = 100

# Positioning the rectangles at the vertical center
rect_y = (screen_height - rect_height) // 2

# Left rectangle (x = 20)
left_paddle = pygame.Rect(20, rect_y, rect_width, rect_height)

# Right rectangle (x = screen_width - 40)
right_paddle = pygame.Rect(screen_width - 40, rect_y, rect_width, rect_height)


# Function to draw the game board
def draw_board():
    screen.fill(BG_COLOR)
    #(0, margin)=0,50 starting point and (screen_width, margin) = 600,50 ending point. 2 is thickness.
    pygame.draw.line(screen, WHITE, (0, margin), (screen_width, margin), 2)  # Top margin line

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game board
    draw_board()
    # Draw the rectangles
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)

    pygame.display.update()

pygame.quit()
