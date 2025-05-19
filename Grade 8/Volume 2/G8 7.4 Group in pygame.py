# __init__ method on line 15 Accepts x, y, and size as arguments.
# Scales the platform image to the specified size.
# Positions the platform at (x, y) on the screen.
# Makes the object ready to be added to a sprite group.
# pygame.sprite.Group() lets you treat multiple sprites as one unit for drawing and updating.


import pygame
pygame.init()

# game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (153, 217, 234)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Toggle Jump')

# set frame rate
clock = pygame.time.Clock()
FPS = 60

# load images
player_image = pygame.image.load('astronaut.png').convert_alpha()  # player image
bg_image = pygame.image.load('space.png').convert_alpha()          # background image
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))  # scaled to screen
platform_image = pygame.image.load('land.png').convert_alpha()

# --- Player class using pygame.sprite.Sprite ---
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # Initialize Sprite class
        self.image = pygame.transform.scale(player_image, (45, 45))  # Set image
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    def draw(self):
        screen.blit(self.image, (self.rect.x - 12, self.rect.y - 5))

# --- Create player sprite  ---
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)



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
    clock.tick(FPS)

    # Draw the background
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    platform_group.draw(screen)  # Draw all platform sprites in the group with one line
    player.draw()
    pygame.display.update()

pygame.quit()
