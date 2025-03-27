# Following are the steps to display text on screen -
# 1. Define font variable on line 31.
# 2. Call font.render to convert text to image on line 63.
# 3. Call blit method to transfer image on the screen pixel by pixel line 67.
#pygame.time.delay(2000) is used to keep the game over message on the screen for 2 seconds on line 67.

# Task  : Write the code to print the game win message under the if condition on line 72.

import pygame
pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Maze Game')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
x, y = (0, 450)

obstacles = [
    pygame.Rect(0, 0, 400, 50),
    pygame.Rect(60, 90, 50, 200),
    pygame.Rect(200, 150, 400, 50),
    pygame.Rect(60, 280, 150, 50),
    pygame.Rect(180, 350, 200, 50),
    pygame.Rect(450, 420, 30, 200)
]
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x = x-10

    if keys[pygame.K_RIGHT] and x < (screen_width - player.width):
        x = x+10

    if keys[pygame.K_UP] and y > 0:
        y = y-10

    if keys[pygame.K_DOWN] and y < (screen_height - player.height):
        y = y+10

    screen.fill(WHITE)

    player = pygame.draw.rect(screen, GREEN, (x, y, 50, 50))  # Player
    win = pygame.draw.rect(screen, BLUE, (450, 0, 50, 50))  # Winning area

    for obstacle in obstacles:
        pygame.draw.rect(screen, (197, 65, 23), obstacle)  # Draw obstacles

    for obstacle in obstacles:
        if player.colliderect(obstacle):
            game_over_text = font.render('Game Over', True, (255, 0, 0))
            #blit method places one surface object on the other.
            screen.blit(game_over_text, (230, 250))
            pygame.display.update()
            pygame.time.delay(2000)  #adding delay
            running = False

    if player.colliderect(win):



        running = False

    pygame.display.update()
    clock.tick(30)
pygame.quit()
