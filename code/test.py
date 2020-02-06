
import pygame
import sys
from pygame.locals import *

pygame.init()

menu = pygame.display.set_mode((1024, 768), RESIZABLE)
fond = pygame.image.load("code/menuBeta.png").convert()
menu.blit(fond, (0, 0))

player_health = 100
niveau_gaz = 0
open_coffre = False
rafale= pygame.mixer.Sound('code/Rafale-LaRafale.wav')
checkez= pygame.mixer.Sound('code/Rafale-Checkez.wav')
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
position_gazBarre = position_gazBarre.move(200,20)
menu.blit(gazBarre, position_gazBarre)


# Coeur
coeur = pygame.image.load("code/Coeur.png").convert_alpha()
position_coeur = coeur.get_rect()
menu.blit(coeur, position_gaz)
position_coeur = position_coeur.move(300, 200)
#####
vie = pygame.image.load("code/vie 20.png").convert_alpha()
position_vie = vie.get_rect()
position_vie = position_vie.move(100,20)
menu.blit(vie, position_vie)


#VENT
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

class Enemy (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("code/ennemieGauche.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.x = 300
        self.y = 200
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.x < (position_perso.x + 50):
            self.x += 1
            self.rect.center = (self.x, self.y)

        elif self.x > (position_perso.x + 50):
            self.x -= 1
            self.rect.center = (self.x, self.y)

        if self.y < (position_perso.y + 93):
            self.y += 1
            self.rect.center = (self.x, self.y)

        elif self.y > (position_perso.y +93):
            self.y -= 1
            self.rect.center = (self.x, self.y)
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
        perdu= pygame.image.load("code/backgroundBlanc - perdu.png").convert()
        menu.blit(perdu, (0,0))
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

def gaz_bar(niveau_gaz) :
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

    fond = pygame.image.load("code/backgroundBlanc.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(x, y)

    # chargement ennemie
    ennemi = pygame.image.load("code/ennemieGauche.png").convert_alpha()
    position_ennemi= ennemi.get_rect()
    menu.blit(ennemi, position_ennemi)
    position_ennemi = position_ennemi.move(800,500)

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

    enemy = Enemy()
    enemySprites = pygame.sprite.Group(enemy)
    clock2 = pygame.time.Clock()

    while continuer:
        clock2.tick(30)
        sortieDroite = pygame.Rect(1024, 250, 3, 300)

        coeurRect = pygame.Rect(position_coeur.x, position_coeur.y, 32, 32)
        gazRect = pygame.Rect(position_gaz.x, position_gaz.y, 32, 32)
        ennemiRect= pygame.Rect(position_ennemi.x, position_ennemi.y, 32,32)

        if sortieDroite.collidepoint((position_perso.x , position_perso.y )):
            salle2(30, position_perso.y)

        mouvement()   # ############################################################

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

        attaque() # #############################################################

        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(coeurRect) and player_health < 99:
            coeur = pygame.image.load("code/Vide.png")
            position_coeur= position_coeur.move(-100, -100)
            player_health = player_health + 25

        if hit_box_objet.colliderect(gazRect) and niveau_gaz < 99:
            gaz = pygame.image.load("code/bombonne.png")
            position_gaz = position_gaz.move(-500, -100)
            niveau_gaz = niveau_gaz + 50

        if hit_box_objet.colliderect(enemy) or hit_box_objet.colliderect(position_ennemi):
            ennemi = pygame.image.load("code/ennemieGauche.png")
            # = position_ennemi.move(-10000, -10000)
            position_ennemi = position_ennemi.move(-10000, -10000)
            player_health = player_health - 25

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(ennemi, position_ennemi)
        menu.blit(gaz, position_gaz)
        menu.blit(coeur, position_coeur)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        enemySprites.clear(menu, fond)
        enemySprites.update()
        enemySprites.draw(menu)
        pygame.display.flip()

def salle2(x,y):

    global fond
    global menu
    global koopa
    global position_perso
    global coeur
    global position_coeur
    global gaz
    global position_gaz

    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc - 2.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(x, y)


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
    menu.blit(vent, position_vent)

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

        coeurRect = pygame.Rect(position_coeur.x, position_coeur.y, 32, 32)

        sortieDroite = pygame.Rect(1024, 250, 3, 300)

        sortieBas = pygame.Rect(305, 768, 300, 3)

        sortieGauche = pygame.Rect(0, 250, 3, 300)

        if sortieGauche.collidepoint((position_perso.x + 100, position_perso.y)):
            salle1(1000, position_perso.y)

        if sortieDroite.collidepoint((position_perso.x , position_perso.y )):
            salle3(30, position_perso.y)

        if sortieBas.collidepoint((position_perso.x, position_perso.y +100)):
            salle4(position_perso.x, 10)


        mouvement() #############################################################

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

        attaque() ##############################################################




        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(coeurRect) and player_health < 99:
            coeur = pygame.image.load("code/Vide.png")
            position_coeur = position_coeur.move(-1000, -1000)
            player_health = player_health + 25


        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(coeur, position_coeur)
        menu.blit(vent, position_vent)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        pygame.display.flip()

def salle3(x,y):

    global fond
    global menu
    global koopa
    global position_perso
    global coeur
    global position_coeur
    global gaz
    global position_gaz
    global checkez


    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc - 3.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(x, y)

    checkez.play()

    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)
    global open_coffre


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

    global up
    global down
    global left
    global right
    global space

    while continuer:
        gazRect = pygame.Rect(position_gaz.x, position_gaz.y, 32, 32)
        coffreRect = pygame.Rect(position_coffre.x, position_coffre.y, 32, 32)

        sortieGauche = pygame.Rect(0, 250, 3, 300)

        if sortieGauche.collidepoint((position_perso.x + 100 , position_perso.y)):
            salle2(1000, position_perso.y)

        mouvement()  #############################################################

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


        attaque() ##############################################################


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
        menu.blit(koopa, position_perso)
        menu.blit(gaz, position_gaz)
        menu.blit(vent, position_vent)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        pygame.display.flip()

def salle4(x,y):

    global fond
    global menu
    global koopa
    global position_perso
    global coeur
    global position_coeur
    global gaz
    global position_gaz

    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc - 4.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(x, y)

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
        gazRect = pygame.Rect(position_gaz.x, position_gaz.y, 32, 32)

        sortieHaut = pygame.Rect(0, 0, 1000, 3)

        sortieBas = pygame.Rect(0, 768, 1000, 3)

        if sortieHaut.collidepoint((position_perso.x, position_perso.y + 100)):
            salle2(position_perso.x , 660)
        if sortieBas.collidepoint((position_perso.x, position_perso.y)):
            salle5(position_perso.x, 10)

        mouvement()  #############################################################

        if left and ((position_perso.x > 380 and (position_perso.y+93 < 100) ) or (position_perso.x > 380 and (position_perso.y+93 > 738) ) or (position_perso.x > 20 and 738 > position_perso.y +93 > 100) ):
            position_perso = position_perso.move(-1, 0)
            koopa = pygame.image.load("code/magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and ((position_perso.x < 525 and (position_perso.y+93 < 100) ) or (position_perso.x < 525 and (position_perso.y+93 > 738) ) or (position_perso.x < 900 and 738 > position_perso.y +93 > 100) ):
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and ((position_perso.x > 380 and position_perso.x < 525) or ( position_perso.x <= 380 and position_perso.y > 0) or ( position_perso.x > 525 and position_perso.y > 0)) :#( (position_perso.y > 0 and position_perso.x < 900) or (380 < position_perso.x < 550) )
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and ((position_perso.x > 380 and position_perso.x < 525) or ( position_perso.x <= 380 and position_perso.y+93 < 738) or ( position_perso.x > 525 and position_perso.y+93 < 738)) :#( (position_perso.y > 0 and position_perso.x < 900) or (380 < position_perso.x < 550) )
            position_perso = position_perso.move(0, 1)
            koopa = pygame.image.load("code/magicienFace.png").convert_alpha()
            pygame.time.wait(0)

        attaque() ##############################################################


        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):

        if hit_box_objet.colliderect(gazRect) and niveau_gaz < 99:
            gaz = pygame.image.load("code/bombonne.png")
            position_gaz = position_gaz.move(-500, -1000)
            niveau_gaz = niveau_gaz + 50

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(gaz, position_gaz)
        menu.blit(vent, position_vent)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        pygame.display.flip()

def salle5(x,y):

    global fond
    global menu
    global koopa
    global position_perso
    global coeur
    global position_coeur
    global gaz
    global position_gaz

    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc - 5.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(x, y)
    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

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

    global up
    global down
    global left
    global right
    global space

    while continuer:
        coeurRect = pygame.Rect(position_coeur.x, position_coeur.y, 32, 32)

        sortieDroite = pygame.Rect(1024, 250, 3, 300)

        sortieHaut = pygame.Rect(0, 0, 1000, 3)



        if sortieDroite.collidepoint((position_perso.x, position_perso.y)):
            salle6(10, position_perso.y)

        if sortieHaut.collidepoint((position_perso.x, position_perso.y+93)):
            salle4(position_perso.x, 660)

        mouvement()  #############################################################

        if left and (position_perso.x > 20):
            position_perso = position_perso.move(-1, 0)
            koopa = pygame.image.load("code/magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and ((0 < position_perso.y < 250 and position_perso.x < 900) or (250 < position_perso.y < 385) or (385 < position_perso.y < 739 and position_perso.x < 900)):
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and ((position_perso.x > 380 and position_perso.x < 525) or ( position_perso.x <= 380 and position_perso.y > 0) or ( 920 > position_perso.x > 525 and position_perso.y > 0)) :#( (position_perso.y > 0 and position_perso.x < 900) or (380 < position_perso.x < 550) )
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and position_perso.y < 650 and position_perso.x < 920:
            position_perso = position_perso.move(0, 1)
            koopa = pygame.image.load("code/magicienFace.png").convert_alpha()
            pygame.time.wait(0)


        attaque() ##############################################################

        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(coeurRect) and player_health < 99:
            coeur = pygame.image.load("code/Vide.png")
            position_coeur = position_coeur.move(-1000, -1000)
            player_health = player_health + 25


        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(coeur, position_coeur)
        menu.blit(vent, position_vent)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        pygame.display.flip()

def salle6(x,y):

    global fond
    global menu
    global koopa
    global position_perso
    global coeur
    global position_coeur
    global gaz
    global position_gaz
    global pickup

    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc - 6.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(x, y)

    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

    pickup.play()

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

    global up
    global down
    global left
    global right
    global space

    while continuer:
        montRect = pygame.Rect(position_mont.x, position_mont.y, 400, 465)
        sortieGauche = pygame.Rect(0, 250, 3, 300)

        if sortieGauche.collidepoint((position_perso.x, position_perso.y)):
            salle5(1000, position_perso.y)

        mouvement()  #############################################################

        if left and  ((250 < position_perso.y < 385) or (0 < position_perso.y < 250 and position_perso.x > 20) or (385 < position_perso.y < 739 and  position_perso.x > 20) ):
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

        attaque() ##############################################################
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        if hit_box_objet.colliderect(montRect) and niveau_gaz == 100:
            fin()
        elif hit_box_objet.colliderect(montRect) and niveau_gaz < 100:
            manque = pygame.image.load("code/manqueGaz.png").convert()
            menu.blit(manque, (80, 400))

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(mont, position_mont)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        pygame.display.flip()

def fin():

    global fond
    global menu
    global koopa
    global position_perso
    global coeur
    global position_coeur
    global gaz
    global position_gaz

    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc - fin.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(480, 500)
    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

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

    global up
    global down
    global left
    global right
    global space

    while continuer:

        sortieGauche = pygame.Rect(0, 250, 3, 300)
        pygame.draw.rect(fond, (255, 0, 0), sortieGauche)

        if sortieGauche.collidepoint((position_perso.x, position_perso.y)):
            salle5()

        mouvement()  # ############################################################

        attaque()  # #############################################################

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)

        # Rafraichissement
        pygame.display.flip()
main_menu()

print("Fin")

pygame.init()