import pygame
from pygame.locals import *

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1024, 768), RESIZABLE)

# Chargement et collage du fond
fond = pygame.image.load("image/background.png").convert()
fenetre.blit(fond, (0, 0))
mur = pygame.image.load("image/mur.png").convert()
position_mur = mur.get_rect()
fenetre.blit(mur, position_mur)

# Chargement et collage du personnage
koopa = pygame.image.load("image/magicienDroite.png").convert_alpha()
position_perso = koopa.get_rect()
fenetre.blit(koopa, position_perso)
position_perso = position_perso.move(500, 400)

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

    if left:
        position_perso = position_perso.move(-1, 0)
        koopa = pygame.image.load("image/magicienGauche.png").convert_alpha()
        pygame.time.wait(2)

    if right:
        position_perso = position_perso.move(1, 0)
        koopa = pygame.image.load("image/magicienDroite.png").convert_alpha()
        pygame.time.wait(2)
    if up:
        position_perso = position_perso.move(0, -1)
        koopa = pygame.image.load("image/magicienDos.png").convert_alpha()
        pygame.time.wait(2)
    if down:
        position_perso = position_perso.move(0, 1)
        koopa = pygame.image.load("image/magicienFace.png").convert_alpha()
        pygame.time.wait(2)
    #si le rect perso touche le rect mur alors il y a colision
    if (position_perso.colliderect(position_mur)) == True:
        print("Colision!")

    # Re-collage
    fenetre.blit(fond, (0, 0))
    fenetre.blit(mur, (0, 0))
    fenetre.blit(koopa, position_perso)
    # Rafraichissement
    pygame.display.flip()

print("Hello World")

pygame.init()
