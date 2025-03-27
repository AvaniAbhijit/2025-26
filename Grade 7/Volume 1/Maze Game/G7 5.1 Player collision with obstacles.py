# for loop on line 59 is used 
#  to check if the player collides with any obstacle in the obstacles list.
# colliderect method tells us if we collided with another rect object on line 61.

# Task: Write the code to check the player collision with the win rectangle from line 65 onwards.

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

    # Player collision with obstacles
    for obstacle in obstacles:
        #colliderect method tell us, if we collided with another rect object.
        if player.colliderect(obstacle):
            running = False #we set the running to False, we will exit the for loop.
    
    # Player collision with win rectangle


    pygame.display.update()
    clock.tick(30)
pygame.quit()
