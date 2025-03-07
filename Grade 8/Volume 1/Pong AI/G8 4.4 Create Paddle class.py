# class Paddle defined for the left and right paddles. Has attributes - rect object.
# draw() function has been moved into the class.
# left_paddle and right_paddle are instance objects of Paddle.

# Task 1: Create the right_paddle instance by passing the x and y coordinates on line no 38.
# Task 2: Call the draw method right_paddle in the while game loop after left_paddle.draw().

import pygame
pygame.init()

screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong AI Game')

BG_COLOR = (50, 25, 50)  # Dark purple background
WHITE = (255, 255, 255)  # White for lines and text
margin = 50

# Rectangle dimensions
rect_width = 20
rect_height = 100
rect_y = (screen_height - rect_height) // 2

def draw_board():
    screen.fill(BG_COLOR)
    pygame.draw.line(screen, WHITE, (0, margin), (screen_width, margin), 2)  # Top margin line

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, rect_width, rect_height)  # Paddle dimensions

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)  # Draw paddle

left_paddle = Paddle(20, rect_y)
right_paddle = Paddle()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game board
    draw_board()
    left_paddle.draw()

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
