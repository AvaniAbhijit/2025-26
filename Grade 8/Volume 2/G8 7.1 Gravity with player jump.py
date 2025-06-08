# vel_y stores the vertical speed of the player.
# gravity = 1 makes the player fall slowly each frame by increasing vel_y.
# When the spacebar is pressed and the player is standing on the platform, the player jumps.
# A negative vel_y moves the player up on line 51.

# Task 1: Change the value for gravity on line 22.


import pygame  # Import the pygame module
pygame.init()  # Initialize all pygame modules

# Create the game window with a width of 400 and a height of 600
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Sky Jumper")

# Create a rectangle representing the player at position (180, 500) with width 40 and height 50
player = pygame.Rect(180, 500, 40, 50)
platform = pygame.Rect(150, 550, 100, 10)

# Gravity and velocity
vel_y = 0
gravity = 1
is_jumping = False

# Game loop
run = True
while run:
    pygame.time.delay(30)

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Restrict movement within screen
    if player.x < 0:
        player.x = 0
    if player.x > 400 - player.width:
        player.x = 400 - player.width

    # Jump only if player is standing on platform or bottom of screen
    if keys[pygame.K_SPACE]:
        if player.bottom >= 550: 
            vel_y = -15  # Jump up

    # Apply gravity
    vel_y += gravity
    player.y += vel_y

    # Stop falling at bottom of screen
    if player.bottom >= 550:
        player.bottom = 550
        vel_y = 0

    # Drawing
    screen.fill((153, 217, 234))  # Background color
    pygame.draw.rect(screen, (255, 0, 0), player)     # Player
    pygame.draw.rect(screen, (255, 255, 0), platform) # Platform

    pygame.display.update()

pygame.quit()
