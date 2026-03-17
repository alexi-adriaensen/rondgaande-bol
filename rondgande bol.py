import pygame
from pygame.locals import *
import random

pygame.init()
pygame.mixer.init()

# screen size
WIDTH, HEIGHT = 1800, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BALL")
clock = pygame.time.Clock()

# 1 cirkel kleur
circle_color = (255, 0, 100)
circle_radius = 50

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

speed_x = 5
speed_y = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 2 beweeg cirkel
    circle_x += speed_x
    circle_y += speed_y

    # 3 botsen op de 4 zijden en willekeurige richting
    if circle_x > WIDTH - circle_radius or circle_x < circle_radius:
        speed_x = random.choice([-1, 1]) * abs(speed_x)  # Willekeurige x-richting
    if circle_y > HEIGHT - circle_radius or circle_y < circle_radius:
        speed_y = random.choice([-1, 1]) * abs(speed_y)  # Willekeurige y-richting

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, circle_color, (int(circle_x), int(circle_y)), circle_radius)
    pygame.display.update()
    clock.tick(60)
