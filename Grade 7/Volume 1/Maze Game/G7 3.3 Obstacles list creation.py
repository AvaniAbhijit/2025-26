# List of obstacles created using Rect objects on line 23.
# Used a for loop to go through each obstacle in the list on line 41.
# Draw the obstacles in brown color on the game screen using  pygame.draw.rect within the for loop on line 42.
# The green rectangle created is the "player" in this game on line 37.
# The blue rectangle created on line 38 is the "win" area.

# Task 1: Add another obstacle anywhere on the screen by modifying the obstacles list.
# Task 2: Experiment with changing the screen size and ensure all elements adjust properly.

import pygame
pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Maze Game')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create a list of obstacles using Rect objects
obstacles = [
    pygame.Rect(0, 0, 100, 150),     # First obstacle (x=0, y=0, width=100, height=150)
    pygame.Rect(150, 50, 70, 90)     # Second obstacle (x=150, y=50, width=70, height=90)
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    player = pygame.draw.rect(screen, GREEN, (0, 450, 50, 50))
    win = pygame.draw.rect(screen, BLUE, (450, 0, 50, 50))

    # Draw the obstacles in the maze using a loop
    for obstacle in obstacles:
        pygame.draw.rect(screen, (197, 65, 23), obstacle)  # Draw obstacles in brown color

    # Update the display to show the changes
    pygame.display.update()

pygame.quit()
