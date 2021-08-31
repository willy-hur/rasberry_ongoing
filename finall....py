import pygame
import sys

# 오른쪽 카운터, 다음 카운터, 각 파트의 카운터

pygame.init()

display = pygame.display.set_mode((1024, 768), 0, 32)

run = True
im = pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/001.png')


def part1():
    display.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/002.png'), (180, 100))


while run:
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    display.fill((255, 255, 255))
    part1()
    pygame.display.update()

pygame.quit()
