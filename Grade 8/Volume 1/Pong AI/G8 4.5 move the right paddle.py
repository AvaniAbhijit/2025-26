# Added speed inside init() - another attribute for the paddle class on line 33.
#                       This is number of pixels that the paddle will move up or down.
# Added move() - another method of paddle class on line 39 which checks and moves the paddle.
# pygame.key.get_pressed() - checks which keys are currently being pressed.
# As we are checking for only up/down, we need to modify only rect.y value by speed.

#Task : Check for DOWN arrow key and modify the rect.y value accordingly within
#       the move method on line no 43.

import pygame
pygame.init()

screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

BG_COLOR = (50, 25, 50)
WHITE = (255, 255, 255)
margin = 50

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
        self.speed = 5 # Movement speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)  # Draw paddle

    # Handle the movement of the paddle up/down when the arrow keys pressed
    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] :  # Move up when up arrow pressed
            self.rect.y -= self.speed

left_paddle = Paddle(20, rect_y)
right_paddle = Paddle(screen_width - 40, rect_y)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    right_paddle.move(pygame.K_UP, pygame.K_DOWN) # Call move

    draw_board()
    left_paddle.draw()
    right_paddle.draw()

    pygame.display.update()

pygame.quit()
