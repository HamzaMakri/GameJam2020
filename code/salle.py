import pygame
import math
import random
import time
from pygame.locals import *

pygame.init()

# Ouverture de la fenêtre Pygame
size = (1024, 768)
fenetre = pygame.display.set_mode((size), RESIZABLE)

# Chargement et collage du fond
fond = pygame.image.load("backgroundBlanc.png").convert()
fenetre.blit(fond, (0, 0))
WHITE = (255, 255, 255)
zombie_list = []
zombie_dist = (200, 900)

class Zombie:

    def __init__(self2, x, y):
        self2.x = x
        self2.y = y

    def draw(self2):
        self2.rect.center = pygame.image.load("mur.png")
        fenetre.blit(self2.image, self2.rect)

    def move_towards_Char(self2, perso):
        # Movement along x direction
        dirvect = pygame.math.Vector2(perso.rect.x - self2.rect.x,
                                      perso.rect.y - self2.rect.y)
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(self2.speed)
        self2.rect.move_ip(dirvect)

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
space= False

while continuer:
    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = 0

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
            if event.key == K_SPACE:  # Si "flèche bas"
                # On descend le perso
                space = False

    if left and position_perso.x > 20:
        position_perso = position_perso.move(-1, 0)
        koopa = pygame.image.load("magicienGauche.png").convert_alpha()
        pygame.time.wait(0)

    if left and space:
        mur = pygame.image.load("mur.png")
        position_mur = position_perso.move(0, 0)

        while position_mur.x > 45:
            fenetre.blit(fond,  (0, 0))
            position_mur = position_mur.move(-10, 0)
            fenetre.blit(mur, position_mur)
            fenetre.blit(koopa, position_perso)
            pygame.display.update()
        space = False
        mur = pygame.image.load("Vide.png")

    if right and position_perso.x < 900:
        position_perso = position_perso.move(1, 0)
        koopa = pygame.image.load("magicienDroite.png").convert_alpha()
        pygame.time.wait(0)

    if right and space :
        mur = pygame.image.load("mur.png")
        position_mur = position_perso.move(0, 0)

        while position_mur.x < 950:
            fenetre.blit(fond, (0, 0))
            position_mur = position_mur.move(10, 0)
            fenetre.blit(mur, position_mur)
            fenetre.blit(koopa, position_perso)
            pygame.display.update()
            pygame.time.delay(100)
        space = False
        mur = pygame.image.load("Vide.png")

    if up and position_perso.y > 0:
        position_perso = position_perso.move(0, -1)
        koopa = pygame.image.load("magicienDos.png").convert_alpha()
        pygame.time.wait(0)

    if up and space :
        mur = pygame.image.load("mur.png")
        position_mur = position_perso.move(0, 0)

        while position_mur.y > 100:
            fenetre.blit(fond, (0, 0))
            position_mur = position_mur.move(0, -10)
            fenetre.blit(mur, position_mur)
            fenetre.blit(koopa, position_perso)
            pygame.display.update()
            pygame.time.delay(100)
        space = False
        mur = pygame.image.load("Vide.png")

    if down and position_perso.y < 650:
        position_perso = position_perso.move(0, 1)
        koopa = pygame.image.load("magicienFace.png").convert_alpha()
        pygame.time.wait(0)

    if down and space:
        mur = pygame.image.load("mur.png")
        position_mur = position_perso.move(0, 0)

        while position_mur.y < 700:
            fenetre.blit(fond, (0, 0))
            position_mur = position_mur.move(0, 10)
            fenetre.blit(mur, position_mur)
            fenetre.blit(koopa, position_perso)
            pygame.display.update()
            pygame.time.delay(100)
        space = False
        mur = pygame.image.load("Vide.png")

    zombie = pygame.image.load("mur.png").convert()
    zombie_pos = zombie.get_rect()
    #fenetre.blit(zombie, zombie_pos)
    zombie_pos = zombie_pos.move(-1, -1)
    while not zombie_pos.colliderect(position_perso):
        dist = random.randint(*zombie_dist)
        angle = random.random() * math.pi * 2
        p_pos = (position_perso.centerx, position_perso.centery)
        zombie_pos.x = int(p_pos[0] + dist * math.sin(angle))
        zombie_pos.y = int(p_pos[1] + dist * math.cos(angle))

    new_pos = (random.randrange(0, size[0]), random.randrange(0, size[1]))
    new_zombie = Zombie(zombie_pos.x, zombie_pos.y)
    zombie_list.append(new_zombie)

    # update all the positions of the zombies
    for i in zombie_list:
        i.move_towards_Char(koopa)

    for i in zombie_list:
        i.draw()

    # Re-collage
    fenetre.blit(fond, (0, 0))
    #fenetre.blit(mur, (0, 0))
    fenetre.blit(koopa, position_perso)
    fenetre.blit(mur, position_mur)
    # Rafraichissement
    pygame.display.flip()

print("Hello World")

pygame.init()
