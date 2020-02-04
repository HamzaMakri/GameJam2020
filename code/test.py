import pygame
import sys
from pygame.locals import *

pygame.init()
import pygame
import sys
from pygame.locals import *

pygame.init()

menu = pygame.display.set_mode((1024, 768), RESIZABLE)
fond = pygame.image.load("code/menuBeta.png").convert()
menu.blit(fond, (0, 0))

click = False


def main_menu():

    while True:
        fond = pygame.image.load("code/menuBeta.png").convert()
        menu.blit(fond, (0, 0))
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(150, 600, 200, 50)
        button_2 = pygame.Rect(650, 600, 200, 50)
        if button_1.collidepoint((mx, my)):
            option()
        if button_1.collidepoint((mx, my)):
            pass

        pygame.draw.rect(menu, (255, 0, 0), button_1)
        pygame.draw.rect(menu, (255, 0, 0), button_2)

        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()



def option():
    # Ouverture de la fenêtre Pygame

    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc.png").convert()
    menu.blit(fond, (0, 0))
    murY = pygame.image.load("code/mur.png").convert()
    position_murY = murY.get_rect()
    menu.blit(murY, position_murY)

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(500, 400)

    # chargement et collage des murs
    mur = pygame.image.load("code/mur.png").convert_alpha()
    position_mur = mur.get_rect()
    mur.set_colorkey((255, 255, 255))  # Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
    menu.blit(mur, (0, 0))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    pygame.key.set_repeat(1, 300)

    # BOUCLE INFINIE
    continuer = 1

    up = False
    down = False
    left = False
    right = False

    while continuer:
        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                continuer = 0

            if event.type == KEYDOWN:
                if event.key == K_DOWN:  # Si "flèche bas"
                    # On descend le perso
                    down = True
                if event.key == K_UP:  # Si "flèche bas"
                    # On descend le perso
                    up = True
                if event.key == K_LEFT:  # Si "flèche bas"
                    # On descend le perso
                    left = True
                if event.key == K_RIGHT:  # Si "flèche bas"
                    # On descend le perso
                    right = True

            elif event.type == KEYUP:
                if event.key == K_DOWN:  # Si "flèche bas"
                    # On descend le perso
                    down = False
                if event.key == K_UP:  # Si "flèche bas"
                    # On descend le perso
                    up = False
                if event.key == K_LEFT:  # Si "flèche bas"
                    # On descend le perso
                    left = False
                if event.key == K_RIGHT:  # Si "flèche bas"
                    # On descend le perso
                    right = False

        if left and position_perso.x > 20:
            position_perso = position_perso.move(-1, 0)
            koopa = pygame.image.load("code/magicienGauche.png").convert_alpha()
            pygame.time.wait(0)
        if right and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)
        if up and position_perso.y > 0:
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)
        if down and position_perso.y < 650:
            position_perso = position_perso.move(0, 1)
            koopa = pygame.image.load("code/magicienFace.png").convert_alpha()
            pygame.time.wait(0)

        # si le rect perso touche le rect mur alors il y a colision
        if (position_perso.colliderect(position_mur)) == True:
            print("Colision!")

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(mur, (0, 0))
        menu.blit(koopa, position_perso)

        # Rafraichissement
        pygame.display.flip()


main_menu()

print("Fin")

pygame.init()






