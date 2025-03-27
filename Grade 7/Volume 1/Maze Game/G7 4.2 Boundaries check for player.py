# x > 0, checks player doesn't move left beyond the screen on line 42.
# x < (screen_width-player.width),checks player doesn't move right beyond the screen on line 46.
#(screen_width - player.width) calculates the maximum x-coordinate the player can move to.
# and is a logical operator in Python, which checks both the conditions must be true.

# Task 1 : Run the code and move the player left/right and observe the change.
# Task 2 : Modify the code to ensure the
#          player does not move off the screen top, bottom on line 49 & 52 respectively.

import pygame
pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Maze Game')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
x,y= (0,450)

obstacles = [
    pygame.Rect(0, 0, 400, 50),
    pygame.Rect(60, 90, 50, 200),
    pygame.Rect(200, 150, 400, 50),
    pygame.Rect(60, 280, 150, 50),
    pygame.Rect(180, 350, 200, 50),
    pygame.Rect(450, 420, 30, 200)
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()

        # Check if the left arrow key is pressed and the player is not at the left boundary.
        if keys[pygame.K_LEFT] and x > 0:
            x = x - 10   # Move the player 10 pixels to the left.

        # Check if the right arrow key is pressed and the player is not at the right boundary.
        if keys[pygame.K_RIGHT] and x < (screen_width-player.width):
            x = x + 10  # Move the player 10 pixels to the right.

        if keys[pygame.K_UP]:
            y = y - 10

        if keys[pygame.K_DOWN]:
            y = y + 10

    screen.fill(WHITE)

    player = pygame.draw.rect(screen, GREEN, (x, y, 50, 50))  # Player rectangle
    win = pygame.draw.rect(screen, BLUE, (450, 0, 50, 50))  # Winning area

    for obstacle in obstacles:
        pygame.draw.rect(screen, (197, 65, 23), obstacle)  # Draw obstacles in brown color

    pygame.display.update()

pygame.quit()
