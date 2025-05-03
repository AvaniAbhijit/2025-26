# pygame.image.load() load an image for the background and the player on lines 38 and 39.
# convert_alpha() converts the loaded image so it can be drawn more quickly on the screen.
# pygame.transform.scale() on line 40 is used to resize an image to a new width and height.
# The blit() function on line 48 is used to draw one surface (like an image) onto another(like game screen).

# Task 1: Declare the def __init__(self,x,y) function for the Player class with following attributes:
#         self.image:pygame.transform.scale(player, (45, 45))
#         self.width: 25,
#         self.height: 40,
#         self.rect: pygame.Rect(0, 0, self.width, self.height)
#         self.rect.center: (x, y) -  these parameters are passed while instantiating the object.
#         self.vel_y: 0
#         self.flip: False
# Task 2:Create player object at center horizontally and 150px above bottom on line 54.
# Task 3: Use blit() function to draw the bg_image on screen at (0,0) on line 60.

import pygame

pygame.init()

#game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

#define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (153, 217, 234)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Toggle Jump')

#set frame rate
clock = pygame.time.Clock()
FPS = 60

#load images
player_image = pygame.image.load('astronaut.png').convert_alpha() # player image
bg_image = pygame.image.load('space.png').convert_alpha()         # background image
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT)) # scaled to the size of the screen


class Player():



	def draw(self):
		screen.blit(self.image, (self.rect.x - 12, self.rect.y - 5))


# declare player object at horizontally center and
# 150 pixels vertically above from bottom of screen


run = True
while run:

    clock.tick(FPS)
    #blit the bg_image on screen at (0,0)


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.draw()

    #update display window
    pygame.display.update()

pygame.quit()
