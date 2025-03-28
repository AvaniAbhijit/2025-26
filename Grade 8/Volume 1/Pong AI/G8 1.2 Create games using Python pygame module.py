# Using python, we can create games.

# Task: Run the code and check the output

import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
ROAD_WIDTH = 300
ROAD_X = (SCREEN_WIDTH - ROAD_WIDTH) // 2

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Game variables
FPS = 60
CAR_WIDTH = 50
CAR_HEIGHT = 80

# Initialize pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Racing Game")
clock = pygame.time.Clock()


class Car:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, CAR_WIDTH, CAR_HEIGHT)
        self.color = color
        self.speed = 5  # Player car speed

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > ROAD_X:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < ROAD_X + ROAD_WIDTH:
            self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


class EnemyCar:
    def __init__(self):
        self.rect = pygame.Rect(
            random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - CAR_WIDTH), -CAR_HEIGHT, CAR_WIDTH, CAR_HEIGHT
        )
        self.speed = 4  # Enemy car speed

    def move(self):
        self.rect.y += self.speed

    def reset(self):
        self.rect.y = -CAR_HEIGHT
        self.rect.x = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - CAR_WIDTH)

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)


# Create player and enemy cars
player = Car(ROAD_X + (ROAD_WIDTH // 2) - (CAR_WIDTH // 2), SCREEN_HEIGHT - CAR_HEIGHT - 10, BLUE)
enemy = EnemyCar()

# Game variables
score = 0
game_over = False


def draw_text(text, size, color, x, y):
    """Function to display text on screen"""
    font = pygame.font.SysFont('Arial', size)
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


# Main Game Loop
running = True
while running:
    clock.tick(FPS)

    if game_over:
        screen.fill(BLACK)
        draw_text("GAME OVER!", 40, WHITE, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20)
        draw_text(f"Final Score: {score}", 30, WHITE, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20)
        draw_text("Press R to Restart", 25, WHITE, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                # Restart game
                player.rect.x = ROAD_X + (ROAD_WIDTH // 2) - (CAR_WIDTH // 2)
                enemy.reset()
                score = 0
                enemy.speed = 4
                game_over = False
        continue

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move objects
    player.move()
    enemy.move()

    # Check if enemy goes out of screen
    if enemy.rect.y > SCREEN_HEIGHT:
        enemy.reset()
        score += 1
        enemy.speed += 0.5  # Increase difficulty over time

    # Check for collision
    if enemy.rect.colliderect(player.rect):
        game_over = True

    # Draw elements
    screen.fill(GRAY)  # Road background
    pygame.draw.rect(screen, BLACK, (ROAD_X, 0, ROAD_WIDTH, SCREEN_HEIGHT))  # Road
    player.draw()
    enemy.draw()
    draw_text(f"Score: {score}", 30, WHITE, 20, 20)

    pygame.display.update()

pygame.quit()
