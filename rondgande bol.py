import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1800, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BALL")
clock = pygame.time.Clock()

circle_color = (255, 0, 0)
circle_radius = 50

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


    circle_x += speed


    if circle_x > WIDTH + circle_radius:
        circle_x = -circle_radius


    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    pygame.display.update()
    clock.tick(60)

