# pygame.time.Clock() on line 35
# This creates a Clock object that helps control the frame rate of the game.
# It ensures that the game runs at a consistent speed across different computers.

# clock.tick(30) on line 65
# This limits the game loop to 30 frames per second (FPS).
# If clock.tick(30) is not used, the game will run as fast as possible,
# making movement too fast and CPU usage very high.

# Task : Change the value inside clock.tick and run the code, observe the change.

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
# Clock for controlling frame rate
clock = pygame.time.Clock()

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
    # Limit frame rate to 30 FPS
    clock.tick(30)
pygame.quit()
