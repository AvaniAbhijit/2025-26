#dx = 0: Resets how much the player will move side-to-side for each frame on line 60.
#If A (K_a) is pressed → move left by dx = -10, and self.flip = False to face left on line 67.
#If moving left goes off-screen, set dx to stop at the edge on line 82.
#self.rect.x += dx moves the player horizontally based on dx on line 104.

#Task 1 : Write the code If D (K_d) is pressed → move right by dx = 10, and
#       self.flip = True to face right on line 72 onwords.
#Task 2 : Write the code make sure the player doesn't move beyond the right edge of the screen.
#        Hint : dx = SCREEN_WIDTH - self.rect.right on line 86 onwords.
# Task 3 : Change the value of dx=10 to 5 pixels and observe the change on line 68 and 73.


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
        #reset variables
        dx = 0
        dy = 0

        # Check which keys are currently being pressed
        key = pygame.key.get_pressed()

        # If the 'A' key is pressed, move the player left
        if key[pygame.K_a]:
            dx = -10                # Move left by 10 pixels
            self.flip = False       # Do not flip the image (face left)

        # If the 'D' key is pressed, move the player right

                                # Move right by 10 pixels
                                # Flip the image horizontally (face right)

        # Apply gravity to the player's vertical velocity
        self.vel_y += GRAVITY
        dy += self.vel_y           # Add vertical velocity to dy (falling effect)


        # Make sure the player doesn't move beyond the left edge of the screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left  # Adjust dx so the player's left side stays at 0

        # Make sure the player doesn't move beyond the right edge of the screen

                                # Adjust dx so the player's right side stays within screen width



           #check collision with platforms
        for platform in platform_group:
            #collision in the y direction
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if above the platform
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.vel_y = -20

        # Update the player's y position by applying dy
        self.rect.y += dy
        self.rect.x += dx


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
