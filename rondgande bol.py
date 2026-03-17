import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1800,900
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BALL")
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
