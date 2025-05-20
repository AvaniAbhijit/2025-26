#dy means "change in y" — how much the player should move up/down on line 56.
#Gravity adds to the vertical speed every frame on line 59.
#Moves the player down the screen by how much gravity says to 63.

#Task 1 :Modify the GRAVITY value and observe how the player falls faster on line 16.
#Task 2 :Add print() statements to track self.vel_y on line 61.

import pygame

pygame.init()


#game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 1

#define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (153, 217, 234)


#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Toggle Jump')

#set frame rate
clock = pygame.time.Clock()
FPS = 60

#load images
player = pygame.image.load('astronaut.png').convert_alpha()
bg_image = pygame.image.load('space.png').convert_alpha()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
platform_image = pygame.image.load('land.png').convert_alpha()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    def draw(self):
        screen.blit(self.image, (self.rect.x - 12, self.rect.y - 5))

    def move(self):
        # Reset vertical (dy) movement values for this frame
        dy = 0

        # Apply gravity to the player's vertical velocity
        self.vel_y += GRAVITY
        dy += self.vel_y           # Add vertical velocity to dy (falling effect)

        # Update the player's y position by applying dy
        self.rect.y += dy

    def draw(self):
        screen.blit(pygame.transform.flip(self.image,self.flip, False), (self.rect.x - 12, self.rect.y - 5))


#platform class
class Platform(pygame.sprite.Sprite):

	def __init__(self, x, y, width):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(platform_image, (width, 10))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y



# Sprite Groups
platform_group = pygame.sprite.Group()


# player Instance
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

#create starting platform
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100)
platform_group.add(platform)
run = True
while run:

    clock.tick(FPS)
    screen.blit(bg_image, (0, 0 ))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.move()

    #draw platforms
    platform_group.draw(screen)


    # draw player
    player.draw()

    #update display window
    pygame.display.update()

pygame.quit()
