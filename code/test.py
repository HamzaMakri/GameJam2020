
import pygame
import sys
from pygame.locals import *

pygame.init()

menu = pygame.display.set_mode((1024, 768), RESIZABLE)
fond = pygame.image.load("code/menuBeta.png").convert()
menu.blit(fond, (0, 0))
player_health = 0
niveau_gaz = 0
open_coffre = False

click = False

clock = pygame.time.Clock()

def main_menu():

    while True:
        clock.tick(120)
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

def health_bar(player_health):
    if player_health <= 0:
        vie = pygame.image.load("code/vie 0.png").convert_alpha()
        menu.blit(vie, (100, 20))
    if player_health == 25:
        vie = pygame.image.load("code/vie 20.png").convert_alpha()
        menu.blit(vie, (100, 20))
    if player_health == 50:
        vie = pygame.image.load("code/vie 40.png").convert_alpha()
        menu.blit(vie, (100, 20))
    if player_health == 75:
        vie = pygame.image.load("code/vie 70.png").convert_alpha()
        menu.blit(vie, (100, 20))
    if player_health >= 100:
        vie = pygame.image.load("code/vie 100.png").convert_alpha()
        menu.blit(vie, (100, 20))

def gaz_bar(niveau_gaz) :
    if niveau_gaz == 0:
        gaz = pygame.image.load("code/gaz 0.png").convert_alpha()
        menu.blit(gaz, (200, 20))
    elif niveau_gaz == 50:
        gaz = pygame.image.load("code/gaz 50.png").convert_alpha()
        menu.blit(gaz, (200, 20))
    else:
        gaz = pygame.image.load("code/gaz 100.png").convert_alpha()
        menu.blit(gaz, (200, 20))

def salle1():

    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc.png").convert()
    menu.blit(fond, (0, 0))

    # Mur
    murY = pygame.image.load("code/mur.png").convert_alpha()
    position_murY = murY.get_rect()
    menu.blit(murY, position_murY)

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(500, 400)

    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

    # BOMBONNE
    gaz = pygame.image.load("code/bombonne.png").convert_alpha()
    position_gaz = gaz.get_rect()
    menu.blit(gaz, position_gaz)
    position_gaz = position_gaz.move(200, 400)

    # Coeur
    coeur = pygame.image.load("code/Coeur.png").convert_alpha()
    position_coeur = coeur.get_rect()
    menu.blit(coeur, position_gaz)
    position_coeur = position_coeur.move(300, 200)

    # health bar
    health_bar(player_health)

    # barre de gaz
    gaz_bar(niveau_gaz)

    # VENT
    vent = pygame.image.load("code/Vent.png").convert_alpha()
    position_vent = vent.get_rect()
    # mur.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
    menu.blit(vent, position_vent)
    position_mur = position_perso.move(1050, 800)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    pygame.key.set_repeat(1, 300)

    # BOUCLE INFINIE
    continuer = 1

    up = False
    down = False
    left = False
    right = False
    space = False

    while continuer:
        sortieDroite = pygame.Rect(1024, 250, 3, 300)
        pygame.draw.rect(fond, (255, 0, 0), sortieDroite)

        coeurRect = pygame.Rect(position_coeur.x, position_coeur.y, 32, 32)
        gazRect = pygame.Rect(position_gaz.x, position_gaz.y, 32, 32)


        if sortieDroite.collidepoint((position_perso.x, position_perso.y)):
            salle2()

        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                continuer = 0
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    space = True

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
                if event.key == K_SPACE:  # Si "flèche bas"
                    # On descend le perso
                    space = False
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



        if left and space:
            mur = pygame.image.load("code/VentGauche.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.x > 45:
                menu.blit(fond, (0, 0))

                position_mur = position_mur.move(-4, 0)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.wait(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if right and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.x < 950:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(4, 0)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if up and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.y > 100:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(0, -4)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if down and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.y < 700:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(0, 4)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        # si le rect perso touche le rect Bombanne Gaz alors il y a colision
        if (position_perso.colliderect(position_murY)) == True:
            print("Colision!")

        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(coeurRect) and player_health < 99:
            coeur = pygame.image.load("code/Vide.png")
            position_coeur= position_coeur.move(-1000, -1000)
            player_health = player_health + 25

        if hit_box_objet.colliderect(gazRect) and niveau_gaz < 99:
            gaz = pygame.image.load("code/bombonne.png")
            position_gaz = position_gaz.move(-500, -100)
            niveau_gaz = niveau_gaz + 50

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(murY, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(gaz, position_gaz)
        menu.blit(coeur, position_coeur)
        menu.blit(vent, position_vent)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

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


    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

    # chargement et collage des murs
    mur = pygame.image.load("code/mur.png").convert_alpha()
    position_mur = mur.get_rect()
    mur.set_colorkey((255, 255, 255))  # Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
    menu.blit(mur, (0, 0))

    # BOMBONNE
    gaz = pygame.image.load("code/bombonne.png").convert_alpha()
    position_gaz = gaz.get_rect()
    menu.blit(gaz, position_gaz)
    position_gaz = position_gaz.move(200, 400)

    # Coeur
    coeur = pygame.image.load("code/Coeur.png").convert_alpha()
    position_coeur = coeur.get_rect()
    menu.blit(coeur, position_gaz)
    position_coeur = position_coeur.move(300, 200)

    # health bar
    health_bar(player_health)

    # barre de gaz
    gaz_bar(niveau_gaz)

    # VENT
    vent = pygame.image.load("code/Vent.png").convert_alpha()
    position_vent = vent.get_rect()
    # mur.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
    menu.blit(vent, position_vent)
    position_mur = position_perso.move(1050, 800)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    pygame.key.set_repeat(1, 300)

    # BOUCLE INFINIE
    continuer = 1

    up = False
    down = False
    left = False
    right = False
    space = False

    while continuer:
        coeurRect = pygame.Rect(position_coeur.x, position_coeur.y, 32, 32)

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
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    space = True
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
                if event.key == K_SPACE:  # Si "flèche bas"
                    # On descend le perso
                    space = False
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

        if left and  ((250 < position_perso.y < 385) or (0 < position_perso.y < 250 and position_perso.x > 20) or (385 < position_perso.y < 739 and  position_perso.x > 20) ):
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

        if down and ( (position_perso.y < 650 and position_perso.x >20) or (380 < position_perso.x < 550) ):
            position_perso = position_perso.move(0, 1)
            koopa = pygame.image.load("code/magicienFace.png").convert_alpha()
            pygame.time.wait(0)


        if left and space:
            mur = pygame.image.load("code/VentGauche.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.x > 45:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(-4, 0)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.wait(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if right and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.x < 950:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(4, 0)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if up and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.y > 100:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(0, -4)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if down and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.y < 700:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(0, 4)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")



        # si le rect perso touche le rect mur alors il y a colision
        if (position_perso.colliderect(position_mur)) == True:
            print("Colision!")



        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(coeurRect) and player_health < 99:
            coeur = pygame.image.load("code/Vide.png")
            position_coeur = position_coeur.move(-1000, -1000)
            player_health = player_health + 25


        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(murY, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(coeur, position_coeur)
        menu.blit(vent, position_vent)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        pygame.display.flip()

def salle3():
    # Ouverture de la fenêtre Pygame

    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc - 3.png").convert()
    menu.blit(fond, (0, 0))
    murY = pygame.image.load("code/mur.png").convert()
    position_murY = murY.get_rect()
    menu.blit(murY, position_murY)

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(500, 400)

    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)
    global open_coffre

    # chargement et collage des murs
    mur = pygame.image.load("code/mur.png").convert_alpha()
    position_mur = mur.get_rect()
    mur.set_colorkey((255, 255, 255))  # Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
    menu.blit(mur, (0, 0))

    # BOMBONNE
    gaz = pygame.image.load("code/bombonne.png").convert_alpha()
    position_gaz = gaz.get_rect()
    menu.blit(gaz, position_gaz)
    position_gaz = position_gaz.move(-1000, -1000)

    #COFFRE
    coffre = pygame.image.load("code/coffre.png").convert_alpha()
    position_coffre = coffre.get_rect()
    menu.blit(coffre, position_coffre)
    position_coffre= position_coffre.move(500, 400)


    # health bar
    health_bar(player_health)

    # barre de gaz
    gaz_bar(niveau_gaz)

    # VENT
    vent = pygame.image.load("code/Vent.png").convert_alpha()
    position_vent = vent.get_rect()
    # mur.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
    menu.blit(vent, position_vent)
    position_mur = position_perso.move(1050, 800)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    pygame.key.set_repeat(1, 300)

    # BOUCLE INFINIE
    continuer = 1

    up = False
    down = False
    left = False
    right = False
    space = False

    while continuer:
        gazRect = pygame.Rect(position_gaz.x, position_gaz.y, 32, 32)
        coffreRect = pygame.Rect(position_coffre.x, position_coffre.y, 32, 32)

        sortieGauche = pygame.Rect(0, 250, 3, 300)
        pygame.draw.rect(fond, (255, 0, 0), sortieGauche)

        if sortieGauche.collidepoint((position_perso.x, position_perso.y)):
            salle2()

        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                continuer = 0
                sys.exit()


            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    space = True
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
                if event.key == K_SPACE:  # Si "flèche bas"
                    # On descend le perso
                    space = False
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

        if left and  ((250 < position_perso.y < 385) or (0 < position_perso.y < 250 and position_perso.x > 20) or (385 < position_perso.y < 739 and  position_perso.x > 20) ):
            position_perso = position_perso.move(-1, 0)
            koopa = pygame.image.load("code/magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and position_perso.x < 900:
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

        if left and space:
            mur = pygame.image.load("code/VentGauche.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.x > 45:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(-4, 0)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.wait(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if right and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.x < 950:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(4, 0)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if up and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.y > 100:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(0, -4)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if down and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.y < 700:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(0, 4)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        # si le rect perso touche le rect mur alors il y a colision
        if (position_perso.colliderect(position_mur)) == True:
            print("Colision!")

        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)



        if hit_box_objet.colliderect(coffreRect) and open_coffre== False :
            open_coffre = True
            gaz = pygame.image.load("code/bombonne.png")
            position_gaz = position_coffre.move(-30, -30)


        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(gazRect) and niveau_gaz < 99:
            gaz = pygame.image.load("code/bombonne.png")
            position_gaz = position_gaz.move(-1000, -1000)
            niveau_gaz = niveau_gaz + 50


        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(murY, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(gaz, position_gaz)
        menu.blit(vent, position_vent)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        pygame.display.flip()

def salle4():
    # Ouverture de la fenêtre Pygame

    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc - 4.png").convert()
    menu.blit(fond, (0, 0))
    murY = pygame.image.load("code/mur.png").convert()
    position_murY = murY.get_rect()
    menu.blit(murY, position_murY)

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(500, 400)

    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

    # chargement et collage des murs
    mur = pygame.image.load("code/mur.png").convert_alpha()
    position_mur = mur.get_rect()
    mur.set_colorkey((255, 255, 255))  # Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
    menu.blit(mur, (0, 0))

    # BOMBONNE
    gaz = pygame.image.load("code/bombonne.png").convert_alpha()
    position_gaz = gaz.get_rect()
    menu.blit(gaz, position_gaz)
    position_gaz = position_gaz.move(500, 400)

    # health bar
    health_bar(player_health)

    # barre de gaz
    gaz_bar(niveau_gaz)

    # VENT
    vent = pygame.image.load("code/Vent.png").convert_alpha()
    position_vent = vent.get_rect()
    # mur.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
    menu.blit(vent, position_vent)
    position_mur = position_perso.move(1050, 800)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    pygame.key.set_repeat(1, 300)

    # BOUCLE INFINIE
    continuer = 1

    up = False
    down = False
    left = False
    right = False
    space = False

    while continuer:
        gazRect = pygame.Rect(position_gaz.x, position_gaz.y, 32, 32)

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
                sys.exit()


            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    space = True
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
                if event.key == K_SPACE:  # Si "flèche bas"
                    # On descend le perso
                    space = False
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

        if right and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920 :
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and ( (position_perso.y < 650 and position_perso.x >20) or (380 < position_perso.x < 550) ):
            position_perso = position_perso.move(0, 1)
            koopa = pygame.image.load("code/magicienFace.png").convert_alpha()
            pygame.time.wait(0)



        if left and space:
            mur = pygame.image.load("code/VentGauche.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.x > 45:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(-4, 0)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.wait(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if right and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.x < 950:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(4, 0)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if up and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.y > 100:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(0, -4)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if down and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.y < 700:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(0, 4)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")



        # si le rect perso touche le rect mur alors il y a colision
        if (position_perso.colliderect(position_mur)) == True:
            print("Colision!")

        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):

        if hit_box_objet.colliderect(gazRect) and niveau_gaz < 99:
            gaz = pygame.image.load("code/bombonne.png")
            position_gaz = position_gaz.move(-500, -100)
            niveau_gaz = niveau_gaz + 50

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(murY, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(gaz, position_gaz)
        menu.blit(vent, position_vent)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        pygame.display.flip()

def salle5():

    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc - 5.png").convert()
    menu.blit(fond, (0, 0))
    murY = pygame.image.load("code/mur.png").convert()
    position_murY = murY.get_rect()
    menu.blit(murY, position_murY)

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(500, 400)
    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

    # chargement et collage des murs
    mur = pygame.image.load("code/mur.png").convert_alpha()
    position_mur = mur.get_rect()
    mur.set_colorkey((255, 255, 255))  # Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
    menu.blit(mur, (0, 0))

    # Coeur
    coeur = pygame.image.load("code/Coeur.png").convert_alpha()
    position_coeur = coeur.get_rect()
    menu.blit(coeur, position_coeur)
    position_coeur = position_coeur.move(300, 200)

    # health bar
    health_bar(player_health)

    # barre de gaz
    gaz_bar(niveau_gaz)

    # VENT
    vent = pygame.image.load("code/Vent.png").convert_alpha()
    position_vent = vent.get_rect()
    # mur.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
    menu.blit(vent, position_vent)
    position_mur = position_perso.move(1050, 800)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    pygame.key.set_repeat(1, 300)

    # BOUCLE INFINIE
    continuer = 1

    up = False
    down = False
    left = False
    right = False
    space = False

    while continuer:
        coeurRect = pygame.Rect(position_coeur.x, position_coeur.y, 32, 32)

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
                sys.exit()


            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    space = True
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
                if event.key == K_SPACE:  # Si "flèche bas"
                    # On descend le perso
                    space = False
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



        if left and space:
            mur = pygame.image.load("code/VentGauche.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.x > 45:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(-4, 0)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.wait(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if right and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.x < 950:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(4, 0)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if up and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.y > 100:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(0, -4)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if down and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.y < 700:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(0, 4)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")



        # si le rect perso touche le rect mur alors il y a colision
        if (position_perso.colliderect(position_mur)) == True:
            print("Colision!")

        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(coeurRect) and player_health < 99:
            coeur = pygame.image.load("code/Vide.png")
            position_coeur = position_coeur.move(-100, -100)
            player_health = player_health + 25

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(murY, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(coeur, position_coeur)
        menu.blit(vent, position_vent)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        pygame.display.flip()

def salle6():

    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc - 6.png").convert()
    menu.blit(fond, (0, 0))
    murY = pygame.image.load("code/mur.png").convert()
    position_murY = murY.get_rect()
    menu.blit(murY, position_murY)

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(50, 300)
    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

    # chargement et collage des murs
    mur = pygame.image.load("code/mur.png").convert_alpha()
    position_mur = mur.get_rect()
    mur.set_colorkey((255, 255, 255))  # Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
    menu.blit(mur, (0, 0))

    # Montgolfière
    mont = pygame.image.load("code/montgolfiere.png").convert_alpha()
    position_mont = mont.get_rect()
    menu.blit(mont, position_mont)
    position_mont = position_mont.move(300, 200)

    # health bar
    health_bar(player_health)

    # barre de gaz
    gaz_bar(niveau_gaz)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    pygame.key.set_repeat(1, 300)

    # BOUCLE INFINIE
    continuer = 1

    up = False
    down = False
    left = False
    right = False
    space = False

    while continuer:
        montRect = pygame.Rect(position_mont.x, position_mont.y, 400, 465)
        sortieGauche = pygame.Rect(0, 250, 3, 300)
        pygame.draw.rect(fond, (255, 0, 0), sortieGauche)

        if sortieGauche.collidepoint((position_perso.x, position_perso.y)):
            salle5()

        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                continuer = 0
                sys.exit()


            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    space = True
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
                if event.key == K_SPACE:  # Si "flèche bas"
                    # On descend le perso
                    space = False
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
        if left and ((250 < position_perso.y < 385) or (0 < position_perso.y < 250 and position_perso.x > 20) or (
                385 < position_perso.y < 739 and position_perso.x > 20)):
            position_perso = position_perso.move(-1, 0)
            koopa = pygame.image.load("code/magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and position_perso.x < 900:
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



        if left and space:
            mur = pygame.image.load("code/VentGauche.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.x > 45:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(-4, 0)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.wait(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if right and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.x < 950:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(4, 0)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if up and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.y > 100:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(0, -4)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")

        if down and space:
            mur = pygame.image.load("code/Vent.png")
            position_mur = position_perso.move(0, 0)

            while position_mur.y < 700:
                menu.blit(fond, (0, 0))
                position_mur = position_mur.move(0, 4)
                menu.blit(mur, position_mur)
                menu.blit(koopa, position_perso)
                pygame.display.update()
                # pygame.time.delay(100)
            space = False
            mur = pygame.image.load("code/Vide.png")



        # si le rect perso touche le rect mur alors il y a colision
        if (position_perso.colliderect(position_mur)) == True:
            print("Colision!")

        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        if hit_box_objet.colliderect(montRect) and niveau_gaz == 100:
            fin()
        elif hit_box_objet.colliderect(montRect) and niveau_gaz < 100:
            coeur = pygame.image.load("code/Vide.png")
            position_coeur = position_coeur.move(-100, -100)
            player_health = player_health + 25

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(murY, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(mont, position_mont)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        pygame.display.flip()


def fin():
    # Ouverture de la fenêtre Pygame

    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc - fin.png").convert()
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

    # health bar
    vie = pygame.image.load("code/vie 20.png").convert_alpha()
    menu.blit(vie, (100, 10))

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
                sys.exit()

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






