
import pygame
import sys
from pygame.locals import *

pygame.init()

menu = pygame.display.set_mode((1024, 768), RESIZABLE)
fond = pygame.image.load("menuBeta.png").convert()
menu.blit(fond, (0, 0))

player_health = 100
niveau_gaz = 0
open_coffre = False

used_bombonne1 = False
used_bombonne2 = True
used_bombonne3 = True
used_bombonne4= False
used_bombonne5 = True
used_bombonne6 = True
used_bombonnefin = True

used_coeur1 = False
used_coeur2 = False
used_coeur3 = True
used_coeur4 = True
used_coeur5= False
used_coeur6= True
used_coeurfin = True

enemy1Mort = False


rafale = pygame.mixer.Sound('Rafale-LaRafale.wav')
checkez = pygame.mixer.Sound('Rafale-Checkez.wav')
pickup = pygame.mixer.Sound('Rafale-RegardezPickup.wav')
musique = pygame.mixer.music.load('musique.wav')
pygame.mixer.music.play(-1)

# Chargement et collage du personnage
koopa = pygame.image.load("magicienDroite.png").convert_alpha()
position_perso = koopa.get_rect()
menu.blit(koopa, position_perso)
position_perso = position_perso.move(500, 400)

# BOMBONNE
gaz = pygame.image.load("bombonne.png").convert_alpha()
position_gaz = gaz.get_rect()
menu.blit(gaz, position_gaz)
position_gaz = position_gaz.move(200, 400)
######
gazBarre = pygame.image.load("gaz 0.png").convert_alpha()
position_gazBarre = gazBarre.get_rect()
position_gazBarre = position_gazBarre.move(200, 20)
menu.blit(gazBarre, position_gazBarre)

# Coeur
coeur = pygame.image.load("Coeur.png").convert_alpha()
position_coeur = coeur.get_rect()
menu.blit(coeur, position_gaz)
position_coeur = position_coeur.move(300, 200)
#####
vie = pygame.image.load("vie 20.png").convert_alpha()
position_vie = vie.get_rect()
position_vie = position_vie.move(100, 20)
menu.blit(vie, position_vie)

# VENT
vent = pygame.image.load("Vide.png").convert_alpha()
position_vent = vent.get_rect()
menu.blit(vent, position_vent)

click = False
up = False
down = False
left = False
right = False
space = False

clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):
    """ This class represents the block. """

    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image =  pygame.image.load("VentGauche.png").convert_alpha()

        self.rect = self.image.get_rect()

        self.x = position_perso.x
        self.y = position_perso.y

    def update(self):
        """ Move the bullet. """
        self.rect.x -= 10
        self.x -=3

class Bullet2(pygame.sprite.Sprite):
    """ This class represents the block. """

    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([4, 10])
        self.image.fill((0,0,0))

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.x += 3

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("ennemieDroite.png").convert_alpha()
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

        elif self.y > (position_perso.y + 93):
            self.y -= 1
            self.rect.center = (self.x, self.y)


enemy = Enemy()
enemySprites = pygame.sprite.Group(enemy)
listMonstreSalle1 = [enemySprites]


def attaque(coeurpris, bombonnepris):
    global space
    global vent
    global position_vent
    global rafale
    global koopa
    global position_perso
    global listMonstreSalle1

    if left and space:
        # Fire a bullet if the user clicks the mouse button
        bullet = Bullet()
        # Set the bullet so it is where the player is
        bullet.rect.x = position_perso.x
        bullet.rect.y = position_perso.y
        # Add the bullet to the lists
        all_sprites_list.add(bullet)
        bullet_list.add(bullet)
        print("test")
        menu.blit(fond, (0, 0))
        if bullet.rect.x < 20:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    if right and space:
        # Fire a bullet if the user clicks the mouse button
        bullet = Bullet2()
        # Set the bullet so it is where the player is
        bullet.rect.x = position_perso.x
        bullet.rect.y = position_perso.y
        # Add the bullet to the lists
        all_sprites_list.add(bullet)
        bullet_list.add(bullet)
        print("test")
        menu.blit(fond, (0, 0))

    if up and space:
        koopa = pygame.image.load("magicienDos.png")
        menu.blit(koopa, position_perso)
        vent = pygame.image.load("VentHaut.png")
        position_vent = position_perso.move(0, 0)
        rafale.play()
        while position_vent.y > 100:
            menu.blit(fond, (0, 0))
            position_vent = position_vent.move(0, -4)
            menu.blit(vent, position_vent)
            menu.blit(koopa, position_perso)
            if not coeurpris:
                menu.blit(coeur, position_coeur)
            if not bombonnepris:
                menu.blit(gaz, position_gaz)
            menu.blit(vie, position_vie)
            menu.blit(gazBarre, position_gazBarre)
            pygame.display.update()
        space = False
        vent = pygame.image.load("Vide.png")
        koopa = pygame.image.load("magicienDos.png")
        menu.blit(koopa, position_perso)

    if down and space:
        koopa = pygame.image.load("magicienFace.png")
        menu.blit(koopa, position_perso)
        vent = pygame.image.load("VentBas.png")
        position_vent = position_perso.move(0, 0)
        rafale.play()
        while position_vent.y < 700:
            menu.blit(fond, (0, 0))
            position_vent = position_vent.move(0, 4)
            menu.blit(vent, position_vent)
            menu.blit(koopa, position_perso)
            if not coeurpris:
                menu.blit(coeur, position_coeur)
            if not bombonnepris:
                menu.blit(gaz, position_gaz)
            menu.blit(vie, position_vie)
            menu.blit(gazBarre, position_gazBarre)
            pygame.display.update()
        space = False
        vent = pygame.image.load("Vide.png")
        koopa = pygame.image.load("magicienFace.png")
        menu.blit(koopa, position_perso)


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
        fond = pygame.image.load("menuBeta.png").convert()
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

        pygame.draw.rect(fond, (255, 0, 0), button_1)
        pygame.draw.rect(fond, (255, 0, 0), button_2)

        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

def health_bar(player_health):
    global vie
    if player_health <= 1:
        vie = pygame.image.load("vie 0.png").convert_alpha()
        menu.blit(vie, position_vie)
        perdu = pygame.image.load("backgroundBlanc - perdu.png").convert()
        menu.blit(perdu, (0, 0))
    if player_health == 25:
        vie = pygame.image.load("vie 20.png").convert_alpha()
        menu.blit(vie, position_vie)
    if player_health == 50:
        vie = pygame.image.load("vie 40.png").convert_alpha()
        menu.blit(vie, position_vie)
    if player_health == 75:
        vie = pygame.image.load("vie 70.png").convert_alpha()
        menu.blit(vie, position_vie)
    if player_health >= 100:
        vie = pygame.image.load("vie 100.png").convert_alpha()
        menu.blit(vie, position_vie)

def gaz_bar(niveau_gaz):
    global gazBarre
    if niveau_gaz == 0:
        gazBarre = pygame.image.load("gaz 0.png").convert_alpha()
        menu.blit(gazBarre, position_gazBarre)
    elif niveau_gaz == 50:
        gazBarre = pygame.image.load("gaz 50.png").convert_alpha()
        menu.blit(gazBarre, position_gazBarre)
    else:
        gazBarre = pygame.image.load("gaz 100.png").convert_alpha()
        menu.blit(gazBarre, position_gazBarre)

def salle1(x,y):

    # Chargement et collage du menu
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
    global position_vent

    fond = pygame.image.load("backgroundBlanc.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(x, y)

    # chargement ennemie
    ennemi = pygame.image.load("ennemieGauche.png").convert_alpha()
    position_ennemi = ennemi.get_rect()
    menu.blit(ennemi, position_ennemi)
    position_ennemi = position_ennemi.move(800, 500)

    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

    # BOMBONNE
    gaz = pygame.image.load("bombonne.png").convert_alpha()
    position_gaz = gaz.get_rect()
    menu.blit(gaz, position_gaz)
    position_gaz = position_gaz.move(200, 400)

    # Coeur
    coeur = pygame.image.load("Coeur.png").convert_alpha()
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

    global enemy
    global enemySprites
    global enemy1Mort

    clock2 = pygame.time.Clock()

    while continuer:
        clock2.tick(30)
        sortieDroite = pygame.Rect(1024, 250, 3, 300)

        coeurRect = pygame.Rect(position_coeur.x, position_coeur.y, 32, 32)
        gazRect = pygame.Rect(position_gaz.x, position_gaz.y, 32, 32)
        ennemiRect = pygame.Rect(position_ennemi.x, position_ennemi.y, 32, 32)

        if sortieDroite.collidepoint((position_perso.x , position_perso.y )):
            salle2(30, position_perso.y)

        mouvement()  # ############################################################

        if left and (position_perso.x > 20):
            position_perso = position_perso.move(-5, 0)
            koopa = pygame.image.load("magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and ((0 < position_perso.y < 250 and position_perso.x < 900) or (250 < position_perso.y < 385) or (385 < position_perso.y < 739 and position_perso.x < 900)):
            position_perso = position_perso.move(5, 0)
            koopa = pygame.image.load("magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920 :
            position_perso = position_perso.move(0, -5)
            koopa = pygame.image.load("magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and position_perso.y < 650 and position_perso.x < 920:
            position_perso = position_perso.move(0, 5)
            koopa = pygame.image.load("magicienFace.png").convert_alpha()
            pygame.time.wait(0)

        attaque(used_coeur1,used_bombonne1)  ##############################################################

        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)


        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(coeurRect) and player_health < 99 and used_coeur1 == False:
            used_coeur1 = True
            coeur = pygame.image.load("Vide.png")
            position_coeur = position_coeur.move(-100, -100)
            player_health = player_health + 25

        if hit_box_objet.colliderect(gazRect) and niveau_gaz < 99 and used_bombonne1 == False:
            used_bombonne1 = True
            gaz = pygame.image.load("bombonne.png")
            position_gaz = position_gaz.move(-500, -100)
            niveau_gaz = niveau_gaz + 50

        if hit_box_objet.colliderect(enemy):
            player_health = player_health - 25
            enemy1Mort = True
            enemy.rect.center = (-500,-500)

        if position_vent.colliderect(enemy):
            print("ennemi touché")


        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(ennemi, position_ennemi)
        if not used_bombonne1:
            menu.blit(gaz, position_gaz)
        if not used_coeur1:
            menu.blit(coeur, position_coeur)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        if 'enemySprites' in globals():
            enemySprites.clear(fond, menu)
            if enemy1Mort:
                del enemySprites

        if not enemy1Mort:
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
    global  used_coeur2
    global used_bombonne2

    # Chargement et collage du menu
    fond = pygame.image.load("backgroundBlanc - 2.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(x, y)

    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

    # BOMBONNE
    gaz = pygame.image.load("bombonne.png").convert_alpha()
    position_gaz = gaz.get_rect()
    menu.blit(gaz, position_gaz)
    position_gaz = position_gaz.move(200, 400)

    # Coeur
    coeur = pygame.image.load("Coeur.png").convert_alpha()
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

        mouvement()  #############################################################

        if left and ((250 < position_perso.y < 385) or (0 < position_perso.y < 250 and position_perso.x > 20) or (
                385 < position_perso.y < 739 and position_perso.x > 20)):
            position_perso = position_perso.move(-1, 0)
            koopa = pygame.image.load("magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and ((0 < position_perso.y < 250 and position_perso.x < 900) or (250 < position_perso.y < 385) or (
                385 < position_perso.y < 739 and position_perso.x < 900)):
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920:
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and ((position_perso.y < 650 and position_perso.x > 20) or (380 < position_perso.x < 550)):
            position_perso = position_perso.move(0, 1)
            koopa = pygame.image.load("magicienFace.png").convert_alpha()
            pygame.time.wait(0)

        attaque(used_coeur2, used_bombonne2)  ##############################################################

        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(coeurRect) and player_health < 99 and used_coeur2 == False:
            used_coeur2 = True
            coeur = pygame.image.load("Vide.png")
            position_coeur = position_coeur.move(-1000, -1000)
            player_health = player_health + 25

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        if not used_coeur2 :
            menu.blit(coeur, position_coeur)
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
    global open_coffre
    global used_bombonne3
    global used_coeur3


    # Chargement et collage du menu
    fond = pygame.image.load("backgroundBlanc - 3.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(x, y)

    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)


    # BOMBONNE
    gaz = pygame.image.load("bombonne.png").convert_alpha()
    position_gaz = gaz.get_rect()
    menu.blit(gaz, position_gaz)
    position_gaz = position_gaz.move(-1000, -1000)

    # COFFRE

    coffre = pygame.image.load("coffre.png").convert_alpha()
    position_coffre = coffre.get_rect()
    menu.blit(coffre, position_coffre)
    position_coffre = position_coffre.move(500, 400)



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
        coffreRect = pygame.Rect(position_coffre.x, position_coffre.y, 32, 32)

        sortieGauche = pygame.Rect(0, 250, 3, 300)

        if sortieGauche.collidepoint((position_perso.x + 100 , position_perso.y)):
            salle2(1000, position_perso.y)

        mouvement()  #############################################################

        if left and ((250 < position_perso.y < 385) or (0 < position_perso.y < 250 and position_perso.x > 20) or (
                385 < position_perso.y < 739 and position_perso.x > 20)):
            position_perso = position_perso.move(-1, 0)
            koopa = pygame.image.load("magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920:
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and position_perso.y < 650 and position_perso.x < 920:
            position_perso = position_perso.move(0, 1)
            koopa = pygame.image.load("magicienFace.png").convert_alpha()
            pygame.time.wait(0)

        attaque(used_coeur3, used_bombonne3)  ##############################################################


        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        if hit_box_objet.colliderect(coffreRect) and open_coffre == False:
            open_coffre = True
            checkez.play()
            gaz = pygame.image.load("bombonne.png")
            position_gaz = position_coffre.move(-50, -50)


        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(gazRect) and niveau_gaz < 99:
            gaz = pygame.image.load("bombonne.png")
            position_gaz = position_gaz.move(-1000, -1000)
            niveau_gaz = niveau_gaz + 50

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(gaz, position_gaz)
        health_bar(player_health)
        gaz_bar(niveau_gaz)
        if open_coffre:
            coffre_ouvert= pygame.image.load("coffre_ouvert.png").convert_alpha()
            menu.blit(coffre_ouvert, (500, 365))

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
    global used_bombonne4
    global used_coeur4

    # Chargement et collage du menu
    fond = pygame.image.load("backgroundBlanc - 4.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(x, y)

    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

    # BOMBONNE
    gaz = pygame.image.load("bombonne.png").convert_alpha()
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
            koopa = pygame.image.load("magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and ((position_perso.x < 525 and (position_perso.y+93 < 100) ) or (position_perso.x < 525 and (position_perso.y+93 > 738) ) or (position_perso.x < 900 and 738 > position_perso.y +93 > 100) ):
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and ((position_perso.x > 380 and position_perso.x < 525) or ( position_perso.x <= 380 and position_perso.y > 0) or ( position_perso.x > 525 and position_perso.y > 0)) :#( (position_perso.y > 0 and position_perso.x < 900) or (380 < position_perso.x < 550) )
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and ((position_perso.x > 380 and position_perso.x < 525) or ( position_perso.x <= 380 and position_perso.y+93 < 738) or ( position_perso.x > 525 and position_perso.y+93 < 738)) :#( (position_perso.y > 0 and position_perso.x < 900) or (380 < position_perso.x < 550) )
            position_perso = position_perso.move(0, 1)
            koopa = pygame.image.load("magicienFace.png").convert_alpha()
            pygame.time.wait(0)

        attaque(used_coeur4, used_coeur4)  ##############################################################


        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):

        if hit_box_objet.colliderect(gazRect) and niveau_gaz < 99 and used_bombonne4 == False :
            used_bombonne4= True
            gaz = pygame.image.load("bombonne.png")
            position_gaz = position_gaz.move(-500, -1000)
            niveau_gaz = niveau_gaz + 50

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        if not used_bombonne4:
            menu.blit(gaz, position_gaz)
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
    global used_coeur5
    global used_coeur5

    # Chargement et collage du menu
    fond = pygame.image.load("backgroundBlanc - 5.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(x, y)
    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

    # Coeur
    coeur = pygame.image.load("Coeur.png").convert_alpha()
    position_coeur = coeur.get_rect()
    menu.blit(coeur, position_coeur)
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
            koopa = pygame.image.load("magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and ((0 < position_perso.y < 250 and position_perso.x < 900) or (250 < position_perso.y < 385) or (
                385 < position_perso.y < 739 and position_perso.x < 900)):
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and ((position_perso.x > 380 and position_perso.x < 525) or ( position_perso.x <= 380 and position_perso.y > 0) or ( 920 > position_perso.x > 525 and position_perso.y > 0)) :#( (position_perso.y > 0 and position_perso.x < 900) or (380 < position_perso.x < 550) )
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and position_perso.y < 650 and position_perso.x < 920:
            position_perso = position_perso.move(0, 1)
            koopa = pygame.image.load("magicienFace.png").convert_alpha()
            pygame.time.wait(0)

        attaque(used_coeur5, used_bombonne5)  ##############################################################

        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(coeurRect) and player_health < 99 and used_coeur5 == False:
            used_coeur5= True
            coeur = pygame.image.load("Vide.png")
            position_coeur = position_coeur.move(-1000, -1000)
            player_health = player_health + 25

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        if not used_coeur5:
            menu.blit(coeur, position_coeur)
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
    global used_coeur6
    global used_bombonne6

    # Chargement et collage du menu
    fond = pygame.image.load("backgroundBlanc - 6.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(x, y)

    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

    pickup.play()

    # Montgolfière
    mont = pygame.image.load("montgolfiere.png").convert_alpha()
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
            koopa = pygame.image.load("magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and position_perso.x < 900:
            position_perso = position_perso.move(1, 0)
            koopa = pygame.image.load("magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920:
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and position_perso.y < 650 and position_perso.x < 920:
            position_perso = position_perso.move(0, 1)
            koopa = pygame.image.load("magicienFace.png").convert_alpha()
            pygame.time.wait(0)

        attaque(used_coeur6, used_bombonne6)  ##############################################################

        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        if hit_box_objet.colliderect(montRect) and niveau_gaz == 100:
            fin()
        elif hit_box_objet.colliderect(montRect) and niveau_gaz < 100:
            manque = pygame.image.load("manqueGaz.png").convert()
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
    global used_bombonnefin
    global used_coeurfin

    # Chargement et collage du menu
    fond = pygame.image.load("backgroundBlanc - fin.png").convert()
    menu.blit(fond, (0, 0))

    # Chargement et collage du personnage
    koopa = pygame.image.load("magicienDroite.png").convert_alpha()
    position_perso = koopa.get_rect()
    menu.blit(koopa, position_perso)
    position_perso = position_perso.move(480, 500)
    global niveau_gaz
    gaz_bar(niveau_gaz)

    global player_health
    health_bar(player_health)

    # Montgolfière
    mont = pygame.image.load("montgolfiere.png").convert_alpha()
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

        attaque(used_coeurfin, used_bombonnefin)  # #############################################################

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)

        # Rafraichissement
        pygame.display.flip()


main_menu()

print("Fin")

pygame.init()