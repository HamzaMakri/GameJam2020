import pygame
import sys
from pygame.locals import *


def __init__(self):
    # Call the parent class (Sprite) constructor

    self.image = pygame.image.load("code/VentGauche.png").convert_alpha()
    self.rect = self.image.get_rect()

    self.x = position_perso.x
    self.y = position_perso.y
    self.rect.center = (self.x, self.y)


def update(self):
    self.x -= 10
    self.rect.center = (self.x, self.y)

    global listMonstreSalle1
    bullet = Bullet()
    bulletSprites = pygame.sprite.Group(bullet)

    if left and space:
        # Fire a bullet if the user clicks the mouse button
        # Set the bullet so it is where the player is
        # Add the bullet to the lists
        menu.blit(fond, (0, 0))
        while bullet.rect.x < 20:
            bulletSprites.clear(menu, fond)
            bulletSprites.update()
            bulletSprites.draw(menu)


pygame.init()

menu = pygame.display.set_mode((1024, 768), RESIZABLE)
fond = pygame.image.load("code/menuBeta.png").convert()
menu.blit(fond, (0, 0))

player_health = 100
niveau_gaz = 0
open_coffre = False
used_bombonne1 = False
used_bombonne4= False
used_coeur1 = False
used_coeur2 = False
used_coeur5= False
touche_enemy= False

rafale = pygame.mixer.Sound('code/Rafale-LaRafale.wav')
checkez = pygame.mixer.Sound('code/Rafale-Checkez.wav')
pickup = pygame.mixer.Sound('code/Rafale-RegardezPickup.wav')
musique = pygame.mixer.music.load('code/musique.wav')
pygame.mixer.music.play(-1)

# Chargement et collage du personnage
koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
position_perso = koopa.get_rect()
menu.blit(koopa, position_perso)
position_perso = position_perso.move(500, 400)

# BOMBONNE
gaz = pygame.image.load("code/bombonne.png").convert_alpha()
position_gaz = gaz.get_rect()
menu.blit(gaz, position_gaz)
position_gaz = position_gaz.move(200, 400)
######
gazBarre = pygame.image.load("code/gaz 0.png").convert_alpha()
position_gazBarre = gazBarre.get_rect()
position_gazBarre = position_gazBarre.move(200, 20)
menu.blit(gazBarre, position_gazBarre)

# Coeur
coeur = pygame.image.load("code/Coeur.png").convert_alpha()
position_coeur = coeur.get_rect()
menu.blit(coeur, position_gaz)
position_coeur = position_coeur.move(300, 200)
#####
vie = pygame.image.load("code/vie 20.png").convert_alpha()
position_vie = vie.get_rect()
position_vie = position_vie.move(100, 20)
menu.blit(vie, position_vie)

# VENT
vent = pygame.image.load("code/Vide.png").convert_alpha()
position_vent = vent.get_rect()
menu.blit(vent, position_vent)

click = False
up = False
down = False
left = False
right = False
space = False

clock = pygame.time.Clock()

class Enemy ():

    image = pygame.image.load("code/ennemieDroite.png").convert_alpha()
    rect = image.get_rect()
    x = 300
    y = 200
    position_image= (x,y)

    if x < (position_perso.x + 50):
        x += 1
        position_image = (x, y)

    elif x > (position_perso.x + 50):
        x -= 1
        position_image = (x, y)

    if y < (position_perso.y + 93):
        y += 1
        position_image = (x, y)

    elif y > (position_perso.y +93):
        y -= 1
        position_image = (x, y)


def attaque():
    global space
    global vent
    global rafale

    if left and space:
        vent = pygame.image.load("code/VentGauche.png")
        position_mur = position_perso.move(0, 0)
        rafale.play()
        while position_mur.x > 45:
            menu.blit(fond, (0, 0))
            position_mur = position_mur.move(-4, 0)
            menu.blit(vent, position_mur)
            menu.blit(koopa, position_perso)
            menu.blit(coeur, position_coeur)
            menu.blit(gaz, position_gaz)
            menu.blit(vie, position_vie)
            menu.blit(gazBarre, position_gazBarre)
            pygame.display.update()
        space = False
        vent = pygame.image.load("code/Vide.png")

    if right and space:
        vent = pygame.image.load("code/Vent.png")
        position_mur = position_perso.move(0, 0)
        rafale.play()
        while position_mur.x < 950:
            menu.blit(fond, (0, 0))
            position_mur = position_mur.move(4, 0)
            menu.blit(vent, position_mur)
            menu.blit(koopa, position_perso)
            menu.blit(coeur, position_coeur)
            menu.blit(gaz, position_gaz)
            menu.blit(vie, position_vie)
            menu.blit(gazBarre, position_gazBarre)
            pygame.display.update()
        space = False
        vent = pygame.image.load("code/Vide.png")

    if up and space:
        vent = pygame.image.load("code/VentHaut.png")
        position_mur = position_perso.move(0, 0)
        rafale.play()
        while position_mur.y > 100:
            menu.blit(fond, (0, 0))
            position_mur = position_mur.move(0, -4)
            menu.blit(vent, position_mur)
            menu.blit(koopa, position_perso)
            menu.blit(coeur, position_coeur)
            menu.blit(gaz, position_gaz)
            menu.blit(vie, position_vie)
            menu.blit(gazBarre, position_gazBarre)
            pygame.display.update()
        space = False
        vent = pygame.image.load("code/Vide.png")

    if down and space:
        vent = pygame.image.load("code/VentBas.png")
        position_mur = position_perso.move(0, 0)
        rafale.play()
        while position_mur.y < 700:
            menu.blit(fond, (0, 0))
            position_mur = position_mur.move(0, 4)
            menu.blit(vent, position_mur)
            menu.blit(koopa, position_perso)
            menu.blit(coeur, position_coeur)
            menu.blit(gaz, position_gaz)
            menu.blit(vie, position_vie)
            menu.blit(gazBarre, position_gazBarre)
            pygame.display.update()
        space = False
        vent = pygame.image.load("code/Vide.png")


def mouvement():

    global up
    global down
    global left
    global right
    global space

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


def main_menu():
    while True:
        clock.tick(120)
        global fond
        global menu
        fond = pygame.image.load("code/menuBeta.png").convert()
        menu.blit(fond, (0, 0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(150, 600, 200, 50)
        button_2 = pygame.Rect(650, 600, 200, 50)
        if button_1.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                sys.exit()
        if button_2.collidepoint((mx, my)):
            if  event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                 salle1(450, 310)

        pygame.draw.rect(menu, (255, 0, 0), button_1)
        pygame.draw.rect(menu, (255, 0, 0), button_2)

        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

def health_bar(player_health):
    global vie
    if player_health <= 1:
        vie = pygame.image.load("code/vie 0.png").convert_alpha()
        menu.blit(vie, position_vie)
        perdu = pygame.image.load("code/backgroundBlanc - perdu.png").convert()
        menu.blit(perdu, (0, 0))
    if player_health == 25:
        vie = pygame.image.load("code/vie 20.png").convert_alpha()
        menu.blit(vie, position_vie)
    if player_health == 50:
        vie = pygame.image.load("code/vie 40.png").convert_alpha()
        menu.blit(vie, position_vie)
    if player_health == 75:
        vie = pygame.image.load("code/vie 70.png").convert_alpha()
        menu.blit(vie, position_vie)
    if player_health >= 100:
        vie = pygame.image.load("code/vie 100.png").convert_alpha()
        menu.blit(vie, position_vie)


def gaz_bar(niveau_gaz):
    global gazBarre
    if niveau_gaz == 0:
        gazBarre = pygame.image.load("code/gaz 0.png").convert_alpha()
        menu.blit(gazBarre, position_gazBarre)
    elif niveau_gaz == 50:
        gazBarre = pygame.image.load("code/gaz 50.png").convert_alpha()
        menu.blit(gazBarre, position_gazBarre)
    else:
        gazBarre = pygame.image.load("code/gaz 100.png").convert_alpha()
        menu.blit(gazBarre, position_gazBarre)

def salle1(x,y):

    # Chargement et collage du fond
    global fond
    global menu
    global koopa
    global position_perso
    global coeur
    global position_coeur
    global gaz
    global position_gaz
    global used_bombonne1
    global used_coeur1

    fond = pygame.image.load("code/backgroundBlanc.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(x, y)

    # chargement ennemie
    ennemi = pygame.image.load("code/ennemieGauche.png").convert_alpha()
    position_ennemi = ennemi.get_rect()
    menu.blit(ennemi, position_ennemi)
    position_ennemi = position_ennemi.move(800, 500)



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

    # Rafraîchissement de l'écran
    pygame.display.flip()

    pygame.key.set_repeat(1, 300)

    # BOUCLE INFINIE
    continuer = 1

    global up
    global down
    global left
    global right
    global space



    while continuer:

        sortieDroite = pygame.Rect(1024, 250, 3, 300)

        coeurRect = pygame.Rect(position_coeur.x, position_coeur.y, 32, 32)
        gazRect = pygame.Rect(position_gaz.x, position_gaz.y, 32, 32)
        ennemiRect = pygame.Rect(position_ennemi.x, position_ennemi.y, 32, 32)

        # if sortieDroite.collidepoint((position_perso.x , position_perso.y )):
            # salle2(30, position_perso.y)

        mouvement()  # ############################################################

        if left and (position_perso.x > 20):
            position_perso = position_perso.move(-5, 0)
            koopa = pygame.image.load("code/magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and ((0 < position_perso.y < 250 and position_perso.x < 900) or (250 < position_perso.y < 385) or (385 < position_perso.y < 739 and position_perso.x < 900)):
            position_perso = position_perso.move(5, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920 :
            position_perso = position_perso.move(0, -5)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and position_perso.y < 650 and position_perso.x < 920:
            position_perso = position_perso.move(0, 5)
            koopa = pygame.image.load("code/magicienFace.png").convert_alpha()
            pygame.time.wait(0)

        attaque()  # #############################################################
        Enemy()

        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)


        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(coeurRect) and player_health < 99 and used_coeur1 == False:
            used_coeur1 = True
            coeur = pygame.image.load("code/Vide.png")
            position_coeur = position_coeur.move(-100, -100)
            player_health = player_health + 25

        if hit_box_objet.colliderect(gazRect) and niveau_gaz < 99 and used_bombonne1 == False:
            used_bombonne1 = True
            gaz = pygame.image.load("code/bombonne.png")
            position_gaz = position_gaz.move(-500, -100)
            niveau_gaz = niveau_gaz + 50

        if hit_box_objet.colliderect(Enemy.position_image) or hit_box_objet.colliderect(position_ennemi):
            ennemi = pygame.image.load("code/ennemieGauche.png")
            # = position_ennemi.move(-10000, -10000)
            position_ennemi = position_ennemi.move(-10000, -10000)
            player_health = player_health - 25

        if position_vent.x == position_ennemi.x and position_vent.y== position_ennemi.y:
            print("ennemi touché")
            ennemi = pygame.image.load("code/ennemieGauche.png")
            position_ennemi = position_ennemi.move(-10000, -10000)

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(ennemi, position_ennemi)
        if not used_bombonne1:
            menu.blit(gaz, position_gaz)
        if not used_coeur1:
            menu.blit(coeur, position_coeur)
        menu.blit(Enemy.image, Enemy.position_image)
        health_bar(player_health)
        gaz_bar(niveau_gaz)
