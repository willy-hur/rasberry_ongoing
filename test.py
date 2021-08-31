import pygame
import sys

pygame.init()

display = pygame.display.set_mode((1024,768),0,32)

run = True
im = pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/001.png')
im2 = pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/002.png')
moverect = im.get_rect()

imX = 360
imY = 200

im2X = 500
im2Y = 300

WHITE = (255,255,255)

while run:
    display.fill(WHITE)
    display.blit(im,(imX,imY))
    display.blit(im2,(im2X,im2Y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

pygame.quit()