import pygame
from pygame.locals import *

pygame.init()


fenetre = pygame.display.set_mode((1280,720), RESIZABLE)
fond = pygame.image.load("imageTest.jpg").convert()
koopa = pygame.image.load("perso.png").convert()


fenetre.blit(fond, (0,0))
perso = pygame.image.load("perso.png").convert()
fenetre.blit(perso, (200,300))

pygame.display.flip()


continuer = 1

while continuer:
    continuer = int(input())

print("Hello World")
