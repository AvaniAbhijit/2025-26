#pygame.key.get_pressed() - checks which keys are currently being pressed on line 42.
# To Check for left/right, we need to modify only x coordinate by 10.
# To Check for up/down, we need to modify only y coordinate by 10.
# On line 45 it checks if the left arrow key is pressed, move the player to the left.
# on line 50 it checks if the right arrow key is pressed, move the player to the right.
# On line 25, x & y are the players coordinates.

# Task : Write the code for Up and Down Movement of the player on line 53 onwords.
# Hint : 1. Take the reference of right and left movement of the player.
#        2. Decrease the y-coordinate by 10 to move up.
#        3. Increase the y-coordinate by 10 to move down.

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
        if event.type == pygame.QUIT:  # Checks if the close button is clicked
            running = False

    keys = pygame.key.get_pressed()  # Get the keys that are pressed on the keyboard.

    # If the left arrow key is pressed, move the player to the left.
    if keys[pygame.K_LEFT]:
        # We decrease the x-coordinate by 10 to move left.
        x = x - 10

    # If the right arrow key is pressed, move the player to the right.
    if keys[pygame.K_RIGHT]:
        # We increase the x-coordinate by 10 to move right.
        x = x + 10

    screen.fill(WHITE)

    player = pygame.draw.rect(screen, GREEN, (x, y, 50, 50))  # Player rectangle
    win = pygame.draw.rect(screen, BLUE, (450, 0, 50, 50))  # Winning area

    for obstacle in obstacles:
        pygame.draw.rect(screen, (197, 65, 23), obstacle)  # Draw obstacles in brown color

    pygame.display.update()

pygame.quit()
