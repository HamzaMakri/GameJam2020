import pygame
import time
from pygame.locals import *

pygame.init()
#class Salle:

    #def __init__(self, type):
        #self.type

    #def salle(self):
# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1024, 768), RESIZABLE)

# Chargement et collage du fond
fond = pygame.image.load("backgroundBlanc1.png").convert()
fenetre.blit(fond, (0, 0))

# Chargement et collage du personnage
koopa = pygame.image.load("magicienDroite.png").convert_alpha()
position_perso = koopa.get_rect()
fenetre.blit(koopa, position_perso)
position_perso = position_perso.move(500, 400)

# chargement et collage des murs
mur = pygame.image.load("mur.png").convert_alpha()
position_mur = mur.get_rect()
#mur.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
fenetre.blit(mur, position_mur)
position_mur = position_perso.move(1050, 800)

# Rafraîchissement de l'écran
pygame.display.flip()

continuer = 1

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
            if event.key == K_SPACE:
                y = 100
                position_mur = position_perso.move(30, y)
                while position_mur.y < 500:
                    position_mur.y += 10
                    fenetre.blit(mur, position_mur)
                    time.sleep(0.05)
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

    if left and position_perso.x > 20 :
        position_perso = position_perso.move(-1, 0)
        koopa = pygame.image.load("magicienGauche.png").convert_alpha()
        pygame.time.wait(0)

    if right and position_perso.x < 900:
        position_perso = position_perso.move(1, 0)
        koopa = pygame.image.load("magicienDroite.png").convert_alpha()
        pygame.time.wait(0)
    if up and position_perso.y > 0:
        position_perso = position_perso.move(0, -1)
        koopa = pygame.image.load("magicienDos.png").convert_alpha()
        pygame.time.wait(0)
    if down and position_perso.y < 650:
        position_perso = position_perso.move(0, 1)
        koopa = pygame.image.load("magicienFace.png").convert_alpha()
        pygame.time.wait(0)




    # Re-collage
    fenetre.blit(fond, (0, 0))
    #fenetre.blit(mur, (0, 0))
    fenetre.blit(koopa, position_perso)
    fenetre.blit(mur, position_mur)
    # Rafraichissement
    pygame.display.flip()

print("Hello World")

pygame.init()
