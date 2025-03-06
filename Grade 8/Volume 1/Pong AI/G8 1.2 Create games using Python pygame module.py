#  Session 9: Adding Startup Screen & Score Increment
# In this session, we will:
# Increase the ball speed after after a certain time
# Reset the ball speed after a goal


import pygame

# Initialize Pygame
pygame.init()

# Set up game window
screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Define colors
BG_COLOR = (50, 25, 50)  # Dark purple background
WHITE = (255, 255, 255)  # White for lines and text

# Clock to control frame rate
clock = pygame.time.Clock()
fps = 60  # Frames per second

# Define font for displaying text
font = pygame.font.SysFont('Constantia', 30)

# Scores
cpu_score = 0
player_score = 0
margin = 50
winner = 0
live_ball = False
speed_increase = 0

# Function to draw the game board
def draw_board():
    screen.fill(BG_COLOR)
    pygame.draw.line(screen, WHITE, (0, margin), (screen_width, margin), 2)  # Top margin line

# Function to draw text on the screen
def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 100)  # Paddle dimensions
        self.speed = 5  # Movement speed
        self.ai_speed = 5  # AI movement speed

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 50:  # Move up (prevent going above score area)
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < screen_height:  # Move down
            self.rect.y += self.speed

    def ai(self):
        #ai to move the paddle automatically
        #move down
        if self.rect.centery < ball.rect.top and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.ai_speed)
        #move up
        if self.rect.centery > ball.rect.bottom and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.ai_speed)


    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)  # Draw paddle


# Ball class
class Ball:
    def __init__(self, x, y):
        self.reset(x, y)

    def move(self):
        #check collision with top margin
        if self.rect.top < margin:
            self.speed_y *= -1
        #check collision with bottom of the screen
        if self.rect.bottom > screen_height:
            self.speed_y *= -1
        if self.rect.colliderect(player_paddle) or self.rect.colliderect(cpu_paddle):
            self.speed_x *= -1

        #check for out of bounds
        if self.rect.left < 0:
            self.winner = 1
        if self.rect.left > screen_width:
            self.winner = -1

        #update ball position
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.winner

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.ball_rad = 8
        self.rect = pygame.Rect(x, y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = -4
        self.speed_y = 4
        self.winner = 0# 1 is the player and -1 is the CPU

# Create paddles and ball
player_paddle = Paddle(screen_width - 40, screen_height // 2 - 50)
cpu_paddle = Paddle(20, screen_height // 2 - 50)  # AI paddle (still static)
ball = Ball(screen_width - 60, screen_height // 2)  # Ball starts near player side

# Main loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
            live_ball = True
            ball.reset(screen_width - 60, screen_height // 2 + 50)
            print('Ball reset')

    # Draw everything
    draw_board()
    draw_text('CPU: ' + str(cpu_score), 20, 15)
    draw_text('P1: ' + str(player_score), screen_width - 100, 15)
    draw_text('BALL SPEED: ' + str(abs(ball.speed_x)), screen_width // 2 - 100 , 15)

    #draw paddles
    player_paddle.draw()
    cpu_paddle.draw()

    if live_ball == True:
        speed_increase += 1
        winner = ball.move()
        if winner == 0:
            #draw ball
            ball.draw()
            #move paddles
            player_paddle.move(pygame.K_UP, pygame.K_DOWN)
            cpu_paddle.ai()
        else:
            live_ball = False
            print("Live ball is false")
            if winner == 1:
                player_score += 1
            elif winner == -1:
                cpu_score += 1
    #print player instructions
    elif live_ball == False:
        if winner == 0:
            draw_text('CLICK ANYWHERE TO START',  100, screen_height // 2 -100)
        if winner == 1:
            draw_text('YOU SCORED!',  220, screen_height // 2 -100)
            draw_text('CLICK ANYWHERE TO START',  100, screen_height // 2 -50)
        if winner == -1:
            draw_text('CPU SCORED!', 220, screen_height // 2 -100)
            draw_text('CLICK ANYWHERE TO START',  100, screen_height // 2 -50)


    player_paddle.draw()
    cpu_paddle.draw()
    ball.draw()


    if speed_increase > 500:
        speed_increase = 0
        if ball.speed_x < 0:
            ball.speed_x -= 1
        if ball.speed_x > 0:
            ball.speed_x += 1
        if ball.speed_y < 0:
            ball.speed_y -= 1
        if ball.speed_y > 0:
            ball.speed_y += 1

    # Update display
    pygame.display.update()
    clock.tick(fps)  # Maintain FPS

# Quit Pygame
pygame.quit()
