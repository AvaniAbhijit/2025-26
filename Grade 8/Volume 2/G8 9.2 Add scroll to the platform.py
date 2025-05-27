# from line 100 to 102 check if the player has bounced to the top of the screen, if yes, then
# reverses this upward movement and scrolls the platforms downward by that same amount.
# self.rect.y += dy + scroll updates the player's vertical position on the screen 
# by combining two things on line 106.
# return scroll value to adjust platform positions based on the player's vertical movement on line 111.
# The update method from line 127 to 131 shifts the platform downward by the scroll amount to simulate the world moving.
# If the platform moves below the bottom of the screen (self.rect.top > SCREEN_HEIGHT), 
# it's removed using self.kill().


# Task - Uncomment the lines from 100 to 102 and observe the output.


import pygame
import random

pygame.init()

# Game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 1
SCROLL_THRESH = 200

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

# Tracking scrolling
scroll = 0
bg_scroll = 0
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
        scroll = 0  # reset scroll

        key = pygame.key.get_pressed()

        # Move left
        if key[pygame.K_a]:
            dx = -5
            self.flip = False

        # Task 1: Move right
        if key[pygame.K_d]:
            dx = 5
            self.flip = True

        # Apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # Stop at left edge
        if self.rect.left + dx < 0:
            dx = -self.rect.left

        # Task 2: Stop at the right edge
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

        #check if the player has bounced to the top of the screen
        #if self.rect.top <= SCROLL_THRESH:
            #if self.vel_y < 0:
                #scroll = -dy
         

        # Apply movement
        self.rect.y += dy + scroll
        self.rect.x += dx

        #Return the scroll value to adjust background and platform positions based
        # on the player's vertical movement.
        return scroll


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

    def update(self, scroll):
	    #update platform's vertical position
        self.rect.y += scroll
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
    screen.blit(bg_image, (0, 0 ))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    scroll = player.move()  # Moves the player and returns how much the screen should scroll (typically upward).

    if len(platform_group) < MAX_PLATFORMS:

        p_w = random.randint(40, 60)
        p_x = random.randint(0, SCREEN_WIDTH - p_w)
        p_y = platform.rect.y - random.randint(80, 120)
        platform = Platform(p_x, p_y, p_w)
        platform_group.add(platform)

    platform_group.update(scroll)
    # Update and draw
    platform_group.draw(screen)
    player.draw()

    pygame.display.update()

pygame.quit()
