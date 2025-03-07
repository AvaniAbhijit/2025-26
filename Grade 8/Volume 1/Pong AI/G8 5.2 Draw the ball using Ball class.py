# Create a Ball class on line 48 to draw it on the screen.
# pygame.draw.ellipse(screen, WHITE, self.rect) is a method to draw ellipse shape.
# self.rect = pygame.Rect(x, y, 15, 15) is rectangular area where the ball is drawn.

# Task 1 : Create a ball instance of Ball class at the center of the screen on line no.
# Task 2 : Call ball.draw() in the game loop on line no.

import pygame
pygame.init()

screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong AI Game')

BG_COLOR = (50, 25, 50)
WHITE = (255, 255, 255)

# Clock to control frame rate
clock = pygame.time.Clock()
fps = 60  # Frames per second
margin = 50

rect_width = 20
rect_height = 100
rect_y = (screen_height - rect_height) // 2

def draw_board():
    screen.fill(BG_COLOR)
    pygame.draw.line(screen, WHITE, (0, margin), (screen_width, margin), 2)  # Top margin line

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 100)  # Paddle dimensions
        self.speed = 5  # Movement speed

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 50:                        # Move up (prevent going above margin line area)
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < screen_height:  # Move down (prevent going below screen)
            self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)  # Draw paddle

# Ball class
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)  # Ball size

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)


right_paddle = Paddle(screen_width - 40, rect_y)
left_paddle = Paddle(20, rect_y)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player paddle
    right_paddle.move(pygame.K_UP, pygame.K_DOWN)

    draw_board()
    right_paddle.draw()
    left_paddle.draw()


    # Update display
    pygame.display.update()
    clock.tick(fps)  # Maintain FPS

pygame.quit()
