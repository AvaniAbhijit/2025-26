# Using python, we can create games.
# Task: Run the code and check the output

import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.title("Space Shooter")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Spaceship
spaceship = turtle.Turtle()
spaceship.shape("triangle")
spaceship.color("white")
spaceship.penup()
spaceship.goto(0, -250)
spaceship.setheading(90)

# Controls
def move_left():
    x = spaceship.xcor()
    x -= 10  # Reduced speed
    if x > -370:
        spaceship.setx(x)

def move_right():
    x = spaceship.xcor()
    x += 10  # Reduced speed
    if x < 370:
        spaceship.setx(x)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Bullet
class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.goto(0, -400)  # Offscreen initially
        self.hideturtle()  # Hide the bullet initially

    def fire(self, x, y):
        self.goto(x, y)
        self.setheading(90)
        self.showturtle()

    def move(self):
        self.sety(self.ycor() + 10)  # Slower bullet speed
        if self.ycor() > 300:
            self.hideturtle()

# Initialize bullets
bullet = Bullet()

def fire_bullet():
    if not bullet.isvisible():  # Only fire if the bullet is not currently visible
        bullet.fire(spaceship.xcor(), spaceship.ycor() + 20)

screen.onkey(fire_bullet, "space")

# Enemy
class Enemy(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(random.randint(-350, 350), random.randint(100, 250))

    def move(self):
        self.sety(self.ycor() - 5)  # Slower enemy movement
        if self.ycor() < -300:
            self.goto(random.randint(-350, 350), random.randint(100, 250))

# Create enemies
enemies = []

for _ in range(5):
    enemy = Enemy()
    enemies.append(enemy)

# Scoring
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

def update_score():
    global score
    score += 10
    score_display.clear()
    score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Collision detection
def check_collision():
    global score
    if bullet.isvisible():  # Only check collisions if the bullet is visible
        for enemy in enemies:
            if bullet.distance(enemy) < 20:
                enemy.goto(random.randint(-350, 350), random.randint(100, 250))
                bullet.hideturtle()  # Hide the bullet once it hits the enemy
                update_score()
                break

    # Check collision between spaceship and enemies
    for enemy in enemies:
        if spaceship.distance(enemy) < 20:
            reset_game()
            break

# Reset the game or reduce score
def reset_game():
    global score
    score -= 5  # Reduce the score when spaceship touches an enemy
    if score < 0:
        score = 0  # Avoid negative score
    score_display.clear()
    score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    spaceship.goto(0, -250)  # Reset spaceship position
    spaceship.setheading(90)  # Reset direction

# Game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)  # Increased delay to slow down the game

    # Move enemies
    for enemy in enemies:
        enemy.move()

    # Move bullet
    bullet.move()

    # Check for collisions
    check_collision()
