import pygame  # Import the pygame module
pygame.init()  # Initialize all pygame modules

# Create the game window with width 400 and height 600
screen = pygame.display.set_mode((400, 600))

# Set the title of the game window
pygame.display.set_caption("Sky Jumper")

# Create a rectangle representing the player at position (180, 500) with width 40 and height 50
player = pygame.Rect(180, 500, 40, 50)

# Variable to control the game loop
run = True
while run:
    # Check for events like closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Fill the screen with a light blue color
    screen.fill((153, 217, 234))

    # Draw the player as a red rectangle on the screen
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Update the display with the latest changes
    pygame.display.update()

# Quit pygame when the loop ends
pygame.quit()
