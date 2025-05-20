# This code defines a Platform class that inherits from pygame.sprite.Sprite is used to handle platform objects in a game.
# Two platforms of different sizes are created and added to a sprite group for easy management. 
# This group allows drawing and updating all platforms together efficiently.
# Using platform_group.add(...), we add the small_platform and large_platform to this group.

import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))

original_image = pygame.image.load('land.png').convert_alpha()

class Platform(pygame.sprite.Sprite):  # Platform inherits from Pygame's Sprite class
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)  # Call parent constructor
        self.image = pygame.transform.scale(original_image, size)  # Set and scale the platform image
        self.rect = self.image.get_rect()  # Get rectangular area for positioning
        self.rect.topleft = (x, y)  # Place the platform at (x, y)

# Create two platform objects with specific sizes
small_platform = Platform(50, 50, (50,10))    # First platform, smaller in size
large_platform = Platform(200, 200, (60,30))  # Second platform, slightly larger

# Add platforms to a group for easier handling and drawing
platform_group = pygame.sprite.Group()
platform_group.add(small_platform, large_platform)


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
