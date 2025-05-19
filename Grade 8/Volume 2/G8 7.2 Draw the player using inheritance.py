# A sprite in Pygame is a 2D game object that includes an image and a rectangle
#(image and rect) for drawing & managed efficiently using the pygame.sprite.Sprite class on line 31.

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


# --- Game loop ---
run = True
while run:

    clock.tick(FPS)

    # Draw background
    screen.blit(bg_image, (0, 0))

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update and draw player sprite

    player.draw()

    # Update display
    pygame.display.update()

pygame.quit()
