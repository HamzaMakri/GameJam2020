import pygame

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("magicienDroite.png").convert()
        self.rect = self.image.get_rect()

        self.x = 300
        self.y = 300
        self.rect.center = (self.x, self.y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 5
        if keys[pygame.K_DOWN]:
            self.y += 5
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5

        self.rect.center = (self.x, self.y)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("ennemieGauche.png")
        self.rect = self.image.get_rect()

        self.x = 300
        self.y = 200
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.x < player.x:
            self.x += 1
            self.rect.center = (self.x, self.y)

        elif self.x > player.x:
            self.x -= 1
            self.rect.center = (self.x, self.y)

        if self.y < player.y:
            self.y += 1
            self.rect.center = (self.x, self.y)

        elif self.y > player.y:
            self.y -= 1
            self.rect.center = (self.x, self.y)


def main():
    global player
    'Create the screen'
    screen = pygame.display.set_mode((640, 480))

    'Set the background'
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))

    'call the object'
    player = Player()
    enemy = Enemy()
    'add object to group'
    allSprites = pygame.sprite.Group(player)
    enemySprites = pygame.sprite.Group(enemy)

    clock = pygame.time.Clock()

    keepGoing = True
    while keepGoing:
        clock.tick(30)

        ' handle events'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        allSprites.clear(screen, background)
        enemySprites.clear(screen, background)
        allSprites.update()
        enemySprites.update()
        allSprites.draw(screen)
        enemySprites.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()