# Code from line no 138 to 154 generates new platforms if there are fewer than the maximum allowed,
# with random width and horizontal position within the screen.
# Each new platform is placed above the previous one at a random vertical distance.
# def update(self): defines an update method that will be called (if explicitly used) to handle changes in the platform's 
# state during each frame of the game loop.

# Task 1: Experiment by changing the range of platform widths (p_w) from 40-60 to 20-80.
# Observe how the platforms change in the game.
# Task 2: Change the value of MAX_PLATFORMS on line 34 and observe the change.


import pygame
import random

pygame.init()

# Game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 1

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (153, 217, 234)

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Toggle Jump')

# Set frame rate
clock = pygame.time.Clock()
FPS = 60
MAX_PLATFORMS = 10

# Load images
player_image = pygame.image.load('astronaut.png').convert_alpha()
bg_image = pygame.image.load('space.png').convert_alpha()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
platform_image = pygame.image.load('land.png').convert_alpha()


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_image, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    def move(self):
        # Reset movement variables
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        # Move left
        if key[pygame.K_a]:
            dx = -5                 # Task 3: Changed to 5 pixels
            self.flip = False

        # Task 1: Move right
        if key[pygame.K_d]:
            dx = 5                 # Task 3: Changed to 5 pixels
            self.flip = True

        # Apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # Stop at left edge
        if self.rect.left + dx < 0:
            dx = -self.rect.left

        # Task 2: Stop at right edge
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right

        # Check collision with platforms
        for platform in platform_group:
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.vel_y = -20

        # Apply movement
        self.rect.y += dy
        self.rect.x += dx

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))


# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
     
		#check if the platform has gone off the screen
		if self.rect.top > SCREEN_HEIGHT:
			self.kill()


# Sprite groups
platform_group = pygame.sprite.Group()

# Player instance
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

# Create initial platform
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100)
platform_group.add(platform)

# Game loop
run = True
while run:
    clock.tick(FPS)
    screen.blit(bg_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Generate new platforms if there are fewer platforms than the maximum allowed
    if len(platform_group) < MAX_PLATFORMS:
        # Randomly choose the width of the new platform between 40 and 60 pixels
        p_w = random.randint(40, 60)

        # Randomly choose the horizontal position (x-coordinate) of the new platform,
        # ensuring it fits within the screen width by subtracting platform width from screen width
        p_x = random.randint(0, SCREEN_WIDTH - p_w)

        # Set the vertical position (y-coordinate) of the new platform to be
        # somewhere above the last platform by subtracting a random value between 80 and 120 pixels
        p_y = platform.rect.y - random.randint(80, 120)

        # Create a new Platform object with the randomly generated position and width
        platform = Platform(p_x, p_y, p_w)

        # Add the new platform to the group of platforms for drawing and collision detection
        platform_group.add(platform)


    # Update and draw
    player.move()
    platform_group.draw(screen)
    player.draw()

    pygame.display.update()

pygame.quit()
