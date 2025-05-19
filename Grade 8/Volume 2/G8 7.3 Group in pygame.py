# __init__ method on line 15 Accepts x, y, and size as arguments.
# Scales the platform image to the specified size.
# Positions the platform at (x, y) on the screen.
# Makes the object ready to be added to a sprite group.
# pygame.sprite.Group() lets you treat multiple sprites as one unit for drawing and updating.


import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))

original_image = pygame.image.load('land.png').convert_alpha()

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, size):  # Note: fixed typo from _init_ to __init__
        pygame.sprite.Sprite.__init__(self)  # Initialize the parent Sprite class
        self.image = pygame.transform.scale(original_image, size)  # Resize image to given size
        self.rect = self.image.get_rect()  # Get rectangle for positioning
        self.rect.topleft = (x, y)  # Set the top-left position

# Create two platform objects with different sizes
small_platform = Platform(50, 50, (50,10))   # Small platform
large_platform = Platform(200, 200, (60,30))  # Larger platform

# Group the platforms using pygame.sprite.Group()
# This allows you to manage and draw multiple sprites together
platform_group = pygame.sprite.Group()
platform_group.add(small_platform, large_platform)  # Add both platforms to the group

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((240, 240, 240))

    platform_group.draw(screen)  # Draw all platform sprites in the group with one line
    pygame.display.update()

pygame.quit()
