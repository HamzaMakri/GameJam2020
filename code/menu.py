import pygame
import sys
from pygame.locals import *

pygame.init()

menu = pygame.display.set_mode((1024, 768), RESIZABLE)
fond = pygame.image.load("image/background.png").convert()
menu.blit(fond, (0, 0))

click = False


def main_menu():

    pygame.key.set_repeat(1, 300)

    # BOUCLE INFINIE

    while True:

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            pass
        if button_1.collidepoint((mx, my)):
            pass

        pygame.draw.rect(menu, (255, 0, 0), button_1)
        pygame.draw.rect(menu, (255, 0, 0), button_2)

        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                sys.exit()


main_menu()