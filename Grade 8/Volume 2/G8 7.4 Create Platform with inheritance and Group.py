# Add a platform for the player to jump on. Create a Platform class as given in the task.
# Image for the platform is declared as platform_image on line
# pygame.sprite.Group() on line __ creates a container to hold multiple platform objects
# Line 70 to 75: Create a platform group, platform object, and add the platform to the group

# Task 1: Create a Platform class that inherits from pygame.sprite.Sprite
# Task 2: Define the init method which takes x, y, and width as parameters.
# Task 3: Call the init method of the Base class - pygame.sprite.Sprite.__init__(self)
# Task 4: Define the following attributes of the class within this method:
#       image: platform_image and scale it to (width, 10)
#       rect: Use get_rect() method on the image.
#       Set the rect.x as the x value received as parameter
#       Set the rect.y as the y value received as a parameter
# Task 5: Call draw on the platform_group object.


import pygame

pygame.init()
pygame.mixer.init()

#game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

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

#platform class




# player Instance
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

# Create an empty Sprite Group
platform_group = pygame.sprite.Group()
# Create starting platform at a certain position and width.
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100)
# Add the platform to the group
platform_group.add(platform)

run = True
while run:

    clock.tick(FPS)
    screen.blit(bg_image, (0, 0 ))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.draw()

    #draw platforms using the group


    #update display window
    pygame.display.update()

pygame.quit()
