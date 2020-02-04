
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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pass
        if button_2.collidepoint((mx, my)):
            if  event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                 salle1()


        pygame.draw.rect(menu, (255, 0, 0), button_1)
        pygame.draw.rect(menu, (255, 0, 0), button_2)

        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()



def salle1():
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
        sortieDroite = pygame.Rect(1024, 250, 3, 300)
        pygame.draw.rect(fond, (255, 0, 0), sortieDroite)

        if sortieDroite.collidepoint((position_perso.x, position_perso.y)):
            salle2()


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

        if left and (position_perso.x > 20):
            position_perso = position_perso.move(-1, 0)
            koopa = pygame.image.load("code/magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and ((0 < position_perso.y < 250 and position_perso.x < 900) or (250 < position_perso.y < 385) or (385 < position_perso.y < 739 and position_perso.x < 900)):
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920 :
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and position_perso.y < 650 and position_perso.x < 920:
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

def salle2():
    # Ouverture de la fenêtre Pygame

    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc - 2.png").convert()
    menu.blit(fond, (0, 0))
    murY = pygame.image.load("code/mur.png").convert()
    position_murY = murY.get_rect()
    menu.blit(murY, position_murY)

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(50, 300)

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
        sortieDroite = pygame.Rect(1024, 250, 3, 300)
        pygame.draw.rect(fond, (255, 0, 0), sortieDroite)

        sortieBas = pygame.Rect(405, 768, 300, 3)
        pygame.draw.rect(fond, (255, 0, 0), sortieBas)

        sortieGauche = pygame.Rect(0, 250, 3, 300)
        pygame.draw.rect(fond, (255, 0, 0), sortieGauche)

        if sortieGauche.collidepoint((position_perso.x, position_perso.y)):
            salle1()

        if sortieDroite.collidepoint((position_perso.x, position_perso.y)):
            salle3()

        if sortieBas.collidepoint((position_perso.x, position_perso.y)):
            salle4()

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

        if left and  250 < position_perso.y < 385 :
            position_perso = position_perso.move(-1, 0)
            koopa = pygame.image.load("code/magicienGauche.png").convert_alpha()
            pygame.time.wait(0)
        if left and 0 < position_perso.y < 250 and position_perso.x > 20:
            position_perso = position_perso.move(-1, 0)
            koopa = pygame.image.load("code/magicienGauche.png").convert_alpha()
            pygame.time.wait(0)
        if left and 385 < position_perso.y < 739 and  position_perso.x > 20:
            position_perso = position_perso.move(-1, 0)
            koopa = pygame.image.load("code/magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and 0 < position_perso.y < 250 and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)
        if right and 250 < position_perso.y < 385:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)
        if right and 385 < position_perso.y < 739 and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920 :
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)


        if down and position_perso.y < 650 and position_perso.x < 920:
            position_perso = position_perso.move(0, 1)
            koopa = pygame.image.load("code/magicienFace.png").convert_alpha()
            pygame.time.wait(0)
        if down and 380 < position_perso.x < 550:
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

def salle3():
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

        sortieGauche = pygame.Rect(0, 250, 3, 300)
        pygame.draw.rect(fond, (255, 0, 0), sortieGauche)

        if sortieGauche.collidepoint((position_perso.x, position_perso.y)):
            salle2()

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


        if right and 0 < position_perso.y < 250 and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)
        if right and 250 < position_perso.y < 385:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)
        if right and 385 < position_perso.y < 739 and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920:
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and position_perso.y < 650 and position_perso.x < 920:
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

def salle4():
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

        sortieHaut = pygame.Rect(405, 0, 300, 3)
        pygame.draw.rect(fond, (255, 0, 0), sortieHaut)

        sortieBas = pygame.Rect(405, 768, 300, 3)
        pygame.draw.rect(fond, (255, 0, 0), sortieBas)

        if sortieHaut.collidepoint((position_perso.x, position_perso.y)):
            salle2()
        if sortieBas.collidepoint((position_perso.x, position_perso.y)):
            salle5()

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

        if right and 0 < position_perso.y < 250 and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)
        if right and 250 < position_perso.y < 385:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)
        if right and 385 < position_perso.y < 739 and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920:
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and position_perso.y < 650 and position_perso.x < 920:
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

def salle5():
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
        sortieDroite = pygame.Rect(1024, 250, 3, 300)
        pygame.draw.rect(fond, (255, 0, 0), sortieDroite)
        sortieHaut = pygame.Rect(405, 0, 300, 3)
        pygame.draw.rect(fond, (255, 0, 0), sortieHaut)


        if sortieDroite.collidepoint((position_perso.x, position_perso.y)):
            salle6()

        if sortieHaut.collidepoint((position_perso.x, position_perso.y)):
            salle4()


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


        if right and 0 < position_perso.y < 250 and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)
        if right and  250 < position_perso.y < 385 :
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)
        if right and 385 < position_perso.y < 739 and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920 :
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)


        if down and position_perso.y < 650 and position_perso.x < 920:
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

def salle6():
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

        sortieGauche = pygame.Rect(0, 250, 3, 300)
        pygame.draw.rect(fond, (255, 0, 0), sortieGauche)

        if sortieGauche.collidepoint((position_perso.x, position_perso.y)):
            salle5()

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


        if right and 0 < position_perso.y < 250 and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)
        if right and  250 < position_perso.y < 385 :
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)
        if right and 385 < position_perso.y < 739 and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920 :
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)


        if down and position_perso.y < 650 and position_perso.x < 920:
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

def fin():
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
        sortieDroite = pygame.Rect(1024, 250, 3, 300)
        pygame.draw.rect(fond, (255, 0, 0), sortieDroite)

        sortieGauche = pygame.Rect(0, 250, 3, 300)
        pygame.draw.rect(fond, (255, 0, 0), sortieGauche)

        sortieHaut = pygame.Rect(405, 0, 300, 3)
        pygame.draw.rect(fond, (255, 0, 0), sortieHaut)

        sortieBas = pygame.Rect(405, 768, 300, 3)
        pygame.draw.rect(fond, (255, 0, 0), sortieBas)

        if sortieDroite.collidepoint((position_perso.x, position_perso.y)):
            salle2()
        if sortieGauche.collidepoint((position_perso.x, position_perso.y)):
            salle1()
        if sortieHaut.collidepoint((position_perso.x, position_perso.y)):
            salle2()
        if sortieBas.collidepoint((position_perso.x, position_perso.y)):
            salle1()

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

        if right and 0 < position_perso.y < 250 and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)
        if right and  250 < position_perso.y < 385 :
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)
        if right and 385 < position_perso.y < 739 and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920 :
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)


        if down and position_perso.y < 650 and position_perso.x < 920:
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






