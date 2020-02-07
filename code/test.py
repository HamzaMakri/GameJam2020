
import pygame
import sys
from pygame.locals import *

pygame.init()

menu = pygame.display.set_mode((768, 768), RESIZABLE)
fond = pygame.image.load("code/Jacket.png").convert()
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
enemy2Mort = False
enemy3Mort = False
enemy4Mort = False


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

adroite = False
aGauche = False
enHaut = False
enBas = False

clock = pygame.time.Clock()

class Enemy (pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("code/ennemieDroite.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.rect.center = (x, y)


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


enemy = Enemy(30, 300)
enemy2 = Enemy(1000, 300)
enemy3 = Enemy(30, 700)
enemy4 = Enemy(1000, 700)
enemySprites2 = pygame.sprite.Group(enemy2)
enemySprites = pygame.sprite.Group(enemy)
enemySprites3 = pygame.sprite.Group(enemy3)
enemySprites4 = pygame.sprite.Group(enemy4)
listMonstreSalle1 = [enemySprites]


class Bullet(pygame.sprite.Sprite):
    """ This class represents the block. """

    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image =  vent

        self.rect = self.image.get_rect()

        global position_vent
        position_vent = self.rect

        self.x = position_perso.x + 50
        self.y = position_perso.y + 50

    def update(self):
        """ Move the bullet. """
        if adroite:
            self.rect.x += 10
            self.x += 10
        if aGauche:
            self.rect.x -= 10
            self.x -= 10
        if enHaut:
            self.rect.y += 10
            self.y += 10
        if enBas:
            self.rect.y -= 10
            self.y -= 10


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

all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

def attaque():
    global space
    global vent
    global rafale
    global koopa
    global position_perso
    global listMonstreSalle1
    global aGauche
    global adroite
    global enHaut
    global enBas


    if left and space:
        aGauche = True
        adroite = False
        enHaut = False
        enBas = False

        koopa = pygame.image.load("code/magicienGaucheAtk.png")
        vent = pygame.image.load("code/VentGauche.png")
        rafale.play()
        bullet = Bullet()
        bullet.rect.x = position_perso.x +25
        bullet.rect.y = position_perso.y +25
        bullet_list.add(bullet)
        menu.blit(fond, (0, 0))
        if bullet.rect.x < 0:
            bullet_list.remove(bullet)

    if right and space:
        aGauche = False
        adroite = True
        enHaut = False
        enBas = False
        koopa = pygame.image.load("code/magicienDroiteAtk.png")
        vent = pygame.image.load("code/vent.png")
        rafale.play()
        bullet = Bullet()
        bullet.rect.x = position_perso.x +25
        bullet.rect.y = position_perso.y +25
        bullet_list.add(bullet)
        menu.blit(fond, (0, 0))
        if bullet.rect.x > 1024:
            bullet_list.remove(bullet)

    if up and space:
        aGauche = False
        adroite = False
        enHaut = False
        enBas = True

        vent = pygame.image.load("code/VentHaut.png")
        rafale.play()
        bullet = Bullet()
        bullet.rect.x = position_perso.x +25
        bullet.rect.y = position_perso.y +25
        bullet_list.add(bullet)
        menu.blit(fond, (0, 0))
        if bullet.rect.x < 0:
            bullet_list.remove(bullet)

    if down and space:
        aGauche = False
        adroite = False
        enHaut = True
        enBas = False

        vent = pygame.image.load("code/VentBas.png")
        position_mur = position_perso.move(0, 0)
        rafale.play()
        bullet = Bullet()
        bullet.rect.x = position_perso.x +25
        bullet.rect.y = position_perso.y +25
        bullet_list.add(bullet)
        menu.blit(fond, (0, 0))
        if bullet.rect.x < 0:
            bullet_list.remove(bullet)


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
        fond = pygame.image.load("code/Jacket.png").convert()
        menu.blit(fond, (0, 0))

        mx, my = pygame.mouse.get_pos()
        button_1_image= pygame.image.load("code/quitter.png").convert_alpha()
        button_2_image= pygame.image.load("code/jouer.png").convert_alpha()
        button_3_image = pygame.image.load("code/règles.png").convert_alpha()
        button_4_image = pygame.image.load("code/crédits.png").convert_alpha()

        button_1_rect = pygame.Rect(122, 700, 200, 50)
        button_2_rect = pygame.Rect(446, 700, 200, 50)
        button_3_rect = pygame.Rect(122, 550, 200, 50)
        button_4_rect = pygame.Rect(446, 550, 200, 50)

        if button_1_rect.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                sys.exit()
        if button_2_rect.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                menu = pygame.display.set_mode((1024, 768), RESIZABLE)
                salle1(450, 310)

        if button_3_rect.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                regles()
        if button_4_rect.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                credits()

        menu.blit(button_1_image, (122, 600))
        menu.blit(button_2_image, (446, 600))
        menu.blit(button_3_image, (122, 500))
        menu.blit(button_4_image, (446, 500))


        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

def regles():
    while True:
        menu = pygame.display.set_mode((1024, 768), RESIZABLE)
        global fond

        fond = pygame.image.load("code/backgroundBlanc - règles.png").convert()
        menu.blit(fond, (0, 0))

        mx, my = pygame.mouse.get_pos()
        button_2_image= pygame.image.load("code/jouer.png").convert_alpha()


        button_2_rect = pygame.Rect(446, 700, 200, 50)



        if button_2_rect.collidepoint((mx, my)):
            if  event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                 salle1(450, 310)

        menu.blit(button_2_image, (446, 600))

        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

def credits():
    while True:
        menu = pygame.display.set_mode((1024, 768), RESIZABLE)
        global fond

        fond = pygame.image.load("code/backgroundBlanc - credits.png").convert()
        menu.blit(fond, (0, 0))

        mx, my = pygame.mouse.get_pos()
        button_2_image = pygame.image.load("code/jouer.png").convert_alpha()

        button_2_rect = pygame.Rect(446, 700, 200, 50)

        if button_2_rect.collidepoint((mx, my)):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                salle1(450, 310)

        menu.blit(button_2_image, (446, 600))

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
    global koopa
    global position_perso
    global coeur
    global position_coeur
    global gaz
    global position_gaz
    global used_bombonne1
    global used_coeur1
    global bullet_list
    global adroite
    global aGauche
    global enHaut
    global enBas

    fond = pygame.image.load("code/backgroundBlanc.png").convert()
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


    clock2 = pygame.time.Clock()

    while continuer:
        clock2.tick(60)
        sortieDroite = pygame.Rect(1024, 250, 3, 300)

        coeurRect = pygame.Rect(position_coeur.x, position_coeur.y, 32, 32)
        gazRect = pygame.Rect(position_gaz.x, position_gaz.y, 32, 32)

        if sortieDroite.collidepoint((position_perso.x , position_perso.y )):
            salle2(30, position_perso.y)

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


        attaque()  ##############################################################

        bullet_list.update()
        bullet_list.draw(menu)

        pygame.display.flip()

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


        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        if not used_bombonne1:
            menu.blit(gaz, position_gaz)
        if not used_coeur1:
            menu.blit(coeur, position_coeur)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        pygame.display.flip()

def salle2(x,y):

    global fond
    global koopa
    global position_perso
    global coeur
    global position_coeur
    global gaz
    global position_gaz
    global used_bombonne2
    global used_coeur2
    global bullet_list
    global adroite
    global aGauche
    global enHaut
    global enBas

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

    global enemy
    global enemy2
    global enemySprites
    global enemySprites2
    global enemy1Mort
    global enemy2Mort

    clock2 = pygame.time.Clock()

    while continuer:
        clock2.tick(100)

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
            position_perso = position_perso.move(-5, 0)
            koopa = pygame.image.load("code/magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and ((0 < position_perso.y < 250 and position_perso.x < 900) or (250 < position_perso.y < 385) or (
                385 < position_perso.y < 739 and position_perso.x < 900)):
            position_perso = position_perso.move(5, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and position_perso.y > 0 and position_perso.x < 920:
            position_perso = position_perso.move(0, -5)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and ((position_perso.y < 650 and position_perso.x > 20) or (380 < position_perso.x < 550)):
            position_perso = position_perso.move(0, 5)
            koopa = pygame.image.load("code/magicienFace.png").convert_alpha()
            pygame.time.wait(0)



        attaque()  ##############################################################


        bullet_list.update()
        bullet_list.draw(menu)
        pygame.display.flip()



        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(coeurRect) and player_health < 99 and used_coeur2 == False:
            used_coeur2 = True
            coeur = pygame.image.load("code/Vide.png")
            position_coeur = position_coeur.move(-1000, -1000)
            player_health = player_health + 25

        if hit_box_objet.colliderect(enemy):
            player_health = player_health - 25
            enemy1Mort = True
            enemy.rect.center = (-500,-500)

        if hit_box_objet.colliderect(enemy2):
            player_health = player_health - 25
            enemy2Mort = True
            enemy2.rect.center = (-500,-500)

        if position_vent.colliderect(enemy):
            print("ca marche")
            enemy1Mort = True

        if position_vent.colliderect(enemy2):
            print("ca marche")
            enemy2Mort = True

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        if not used_coeur2 :
            menu.blit(coeur, position_coeur)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        if 'enemySprites' in globals():
            enemySprites.clear(menu, fond)
            if enemy1Mort:
                del enemySprites

        if not enemy1Mort:
            enemySprites.update()
            enemySprites.draw(menu)
        ##################################################
        if 'enemySprites2' in globals():
            enemySprites2.clear(menu, fond)
            if enemy2Mort:
                del enemySprites2

        if not enemy2Mort:
            enemy2.rect.center = (900, 500)
            enemySprites2.update()
            enemySprites2.draw(menu)

        pygame.display.flip()

        menu.blit(vent, position_vent)


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


    # Chargement et collage du fond
    fond = pygame.image.load("code/backgroundBlanc - 3.png").convert()
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


    # BOMBONNE
    gaz = pygame.image.load("code/bombonne.png").convert_alpha()
    position_gaz = gaz.get_rect()
    menu.blit(gaz, position_gaz)
    position_gaz = position_gaz.move(-1000, -1000)

    # COFFRE

    coffre = pygame.image.load("code/coffre.png").convert_alpha()
    position_coffre = coffre.get_rect()
    menu.blit(coffre, position_coffre)
    position_coffre = position_coffre.move(500, 400)



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

        if left and ((250 < position_perso.y < 385) or (0 < position_perso.y < 250 and position_perso.x > 20) or (
                385 < position_perso.y < 739 and position_perso.x > 20)):
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

        attaque()  ##############################################################


        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        if hit_box_objet.colliderect(coffreRect) and open_coffre == False:
            open_coffre = True
            checkez.play()
            gaz = pygame.image.load("code/bombonne.png")
            position_gaz = position_coffre.move(-50, -50)


        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(gazRect) and niveau_gaz < 99:
            gaz = pygame.image.load("code/bombonne.png")
            position_gaz = position_gaz.move(-1000, -1000)
            niveau_gaz = niveau_gaz + 50

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(gaz, position_gaz)
        health_bar(player_health)
        gaz_bar(niveau_gaz)
        if open_coffre:
            coffre_ouvert= pygame.image.load("code/coffre_ouvert.png").convert_alpha()
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

        attaque()  ##############################################################


        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):

        if hit_box_objet.colliderect(gazRect) and niveau_gaz < 99 and used_bombonne4 == False :
            used_bombonne4= True
            gaz = pygame.image.load("code/bombonne.png")
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
    global enemy2
    global enemy3
    global enemy4
    global enemySprites
    global enemySprites2
    global enemySprites3
    global enemySprites4
    global enemy1Mort
    global enemy2Mort
    global enemy3Mort
    global enemy4Mort

    clock2 = pygame.time.Clock()

    while continuer:
        clock2.tick(100)

        coeurRect = pygame.Rect(position_coeur.x, position_coeur.y, 32, 32)

        sortieDroite = pygame.Rect(1024, 250, 3, 300)

        sortieHaut = pygame.Rect(0, 0, 1000, 3)
        # position_haut = pygame.draw.rect(fond,(255,200,0), sortieHaut )

        if sortieDroite.collidepoint((position_perso.x, position_perso.y)):
            salle6(10, position_perso.y)

        if sortieHaut.collidepoint((position_perso.x, position_perso.y + 100)):
            salle4(position_perso.x, 660)
            print("change de salle vers la 4")

        mouvement()  #############################################################

        if left and (position_perso.x > 20):
            position_perso = position_perso.move(-4, 0)
            koopa = pygame.image.load("code/magicienGauche.png").convert_alpha()
            pygame.time.wait(0)

        if right and ((0 < position_perso.y < 250 and position_perso.x < 900) or (250 < position_perso.y < 385) or (
                385 < position_perso.y < 739 and position_perso.x < 900)):
            position_perso = position_perso.move(4, 0)
            koopa = pygame.image.load("code/magicienDroite.png").convert_alpha()
            pygame.time.wait(0)

        if up and ((position_perso.x > 380 and position_perso.x < 525) or ( position_perso.x <= 380 and position_perso.y > 0) or ( 920 > position_perso.x > 525 and position_perso.y > 0)) :#( (position_perso.y > 0 and position_perso.x < 900) or (380 < position_perso.x < 550) )
            position_perso = position_perso.move(0, -4)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and position_perso.y < 650 and position_perso.x < 920:
            position_perso = position_perso.move(0, 4)
            koopa = pygame.image.load("code/magicienFace.png").convert_alpha()
            pygame.time.wait(0)

        attaque()  ##############################################################
        bullet_list.update()
        bullet_list.draw(menu)
        pygame.display.flip()


        # Hit Box Objet
        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        # if position_coeur.colliderect((position_perso.x,position_perso.y)):
        if hit_box_objet.colliderect(coeurRect) and player_health < 99 and used_coeur5 == False:
            used_coeur5= True
            coeur = pygame.image.load("code/Vide.png")
            position_coeur = position_coeur.move(-1000, -1000)
            player_health = player_health + 25

        if hit_box_objet.colliderect(enemy):
            player_health = player_health - 25
            enemy1Mort = True
            enemy.rect.center = (-500,-500)

        if hit_box_objet.colliderect(enemy2):
            player_health = player_health - 25
            enemy2Mort = True
            enemy2.rect.center = (-500,-500)

        if hit_box_objet.colliderect(enemy3):
            player_health = player_health - 25
            enemy3Mort = True
            enemy3.rect.center = (-500,-500)

        if hit_box_objet.colliderect(enemy4):
            player_health = player_health - 25
            enemy4Mort = True
            enemy4.rect.center = (-500,-500)

        if position_vent.colliderect(enemy):
            print("ca marche")
            enemy1Mort = True

        if position_vent.colliderect(enemy2):
            print("ca marche")
            enemy2Mort = True

        if position_vent.colliderect(enemy3):
            print("ca marche")
            enemy3Mort = True

        if position_vent.colliderect(enemy4):
            print("ca marche")
            enemy4Mort = True



        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        if not used_coeur5:
            menu.blit(coeur, position_coeur)
        health_bar(player_health)
        gaz_bar(niveau_gaz)

        # Rafraichissement
        if 'enemySprites' in globals():
            enemySprites.clear(menu, fond)
            if enemy1Mort:
                del enemySprites

        if not enemy1Mort:
            enemySprites.update()
            enemySprites.draw(menu)

        if 'enemySprites2' in globals():
            enemySprites2.clear(menu, fond)
            if enemy2Mort:
                del enemySprites2

        if not enemy2Mort:
            enemySprites2.update()
            enemySprites2.draw(menu)

        if 'enemySprites3' in globals():
            enemySprites3.clear(menu, fond)
            if enemy3Mort:
                del enemySprites3

        if not enemy3Mort:
            enemySprites3.update()
            enemySprites3.draw(menu)

        if 'enemySprites4' in globals():
            enemySprites4.clear(menu, fond)
            if enemy4Mort:
                del enemySprites4

        if not enemy4Mort:
            enemySprites4.update()
            enemySprites4.draw(menu)


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

    manque = pygame.image.load("code/manqueGaz.png").convert_alpha()
    position_manque = manque.get_rect()
    menu.blit(manque, position_manque)
    position_manque = position_manque.move(1500, 1500)

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

        if up and position_perso.y > 0 and position_perso.x < 920:
            position_perso = position_perso.move(0, -1)
            koopa = pygame.image.load("code/magicienDos.png").convert_alpha()
            pygame.time.wait(0)

        if down and position_perso.y < 650 and position_perso.x < 920:
            position_perso = position_perso.move(0, 1)
            koopa = pygame.image.load("code/magicienFace.png").convert_alpha()
            pygame.time.wait(0)

        attaque()  ##############################################################

        hit_box_objet = pygame.Rect(position_perso.x + 34, position_perso.y + 81, 30, 12)

        if hit_box_objet.colliderect(montRect) and niveau_gaz == 100:
            fin()
        elif hit_box_objet.colliderect(montRect) and niveau_gaz < 100:
            manque = pygame.image.load("code/manqueGaz.png").convert_alpha()
            position_manque = manque.get_rect()
            menu.blit(manque, position_manque)
            position_manque = position_manque.move(80, 100)

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)
        menu.blit(mont, position_mont)
        menu.blit(manque, position_manque)
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

        attaque()  ##############################################################

        # Re-collage
        menu.blit(fond, (0, 0))
        menu.blit(koopa, position_perso)

        # Rafraichissement
        pygame.display.flip()



main_menu()

print("Fin")

pygame.init()
