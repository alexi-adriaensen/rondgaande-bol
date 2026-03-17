import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

#screen size
WIDTH, HEIGHT = 1800, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BALL")
clock = pygame.time.Clock()

#1 sircle kleur
circle_color = (0, 0, 0)
circle_radius = 50

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

speed = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

#2 move sircle
    circle_x += speed

    # 3 botsen op de rechterkant
    if circle_x > WIDTH - circle_radius:
        speed = -speed  # Verander richting bij botsing

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, circle_color, (int(circle_x), circle_y), circle_radius)
    pygame.display.update()
    clock.tick(0)
