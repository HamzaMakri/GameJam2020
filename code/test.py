import pygame
from pygame.locals import *

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1280, 720), RESIZABLE)

# Chargement et collage du fond
fond = pygame.image.load("image/imageTest.jpg").convert()
fenetre.blit(fond, (0, 0))

# Chargement et collage du personnage
koopa = pygame.image.load("image/perso.png").convert_alpha()
position_perso = koopa.get_rect()
fenetre.blit(koopa, position_perso)

# chargement et collage des murs
mur = pygame.image.load("image/mur.png").convert_alpha()
position_mur = mur.get_rect()
mur.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
fenetre.blit(mur, (0, 0))



# Rafraîchissement de l'écran
pygame.display.flip()

continuer = 1


pygame.key.set_repeat(1, 30)

# BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:  # Si "flèche bas"
                # On descend le perso
                position_perso = position_perso.move(0, 3)
            if event.key == K_UP:  # Si "flèche bas"
                # On descend le perso
                position_perso = position_perso.move(0, -3)
            if event.key == K_LEFT:  # Si "flèche bas"
                # On descend le perso
                position_perso = position_perso.move(-3, 0)
            if event.key == K_RIGHT:  # Si "flèche bas"
                # On descend le perso
                position_perso = position_perso.move(3, 0)

    # Re-collage
    fenetre.blit(fond, (0, 0))
    fenetre.blit(koopa, position_perso)

    # Rafraichissement
    pygame.display.flip()

print("Hello World")


pygame.init()






