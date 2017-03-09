import pygame
# import math
import random


class player(pygame.sprite.Sprite):

    # initialize the player's sprite
    def __init__(self, surface, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = [self.x, self.y]

    # define steps
    def step(self, key):
        if self.x < 750:
            if key == 'right':
                self.x = self.x + 10
        if self.x > 50:
            if key == 'left':
                self.x = self.x - 10
        if self.y > 575:
            if key == 'up':
                self.y = self. y + 10
        if self.y > 25:
            if key == 'down':
                self.y = self.y - 10

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Bullet(pygame.sprite.Sprite):

    # initialize the bullet
    def __init__(self, player, speed=1):
        pygame.sprite.Sprite.__init__(self)
        self.x = player.x
        self.y = player.y
        self.speed = speed
        if player.x > 400:
            self.image = bulletbill1
            self.dx = random.randrange(-5, -1)*self.speed
            self.dy = random.randrange(-10, 10)/50*self.speed
        elif player.x < 400:
            self.image = bulletbill
            self.dx = random.randrange(1, 5)*self.speed
            self.dy = random.randrange(-10, 10)/10*self.speed
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = [self.x, self.y]

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def is_hit(self, player):
        bulletx = []
        playerx = []
        bullety = []
        playery = []
        for i in range(int(self.x)-5, int(self.x) + 5):
            bulletx.append(i)
        for j in range(int(player.x)-25, int(player.x)+25):
            playerx.append(j)
        for l in range(int(self.y)-5, int(self.y) + 5):
            bullety.append(l)
        for m in range(int(player.y)-25, int(player.y)+25):
            playery.append(m)
        for i in range(0, len(bulletx)):
            if bulletx[i] in playerx and bullety[i] in playery:
                return True
        return False

    def is_colliding(self):
        if self.y <= 5 or self.y >= 595:
            return True
        return False

    def collision(self):
        self.dy = self.dy*-1


if __name__ == "__main__":
    img = pygame.image.load('images\space.jpg')
    width = 800
    height = 600
    player_scale = 75
    bull_scale = 20
    scaled_img = pygame.transform.scale(img, (width, height))
    screen = pygame.display.set_mode((800, 600))
    screen.blit(scaled_img, (0, 0))
    pygame.display.set_caption('PyGame App!')

    pygame.init()

    # Initialize player data and bullets
    # Player 1
    ship = pygame.image.load('images\ship(ROT_LEFT)')
    ship = pygame.transform.scale(ship, (player_scale, player_scale))
    p1_spawnx = 700
    p1_spawny = 400

    # Player 2
    elephant = pygame.image.load('images\ship(ROT_RIGHT)')
    elephant = pygame.transform.scale(elephant, (player_scale, player_scale))
    p2_spawnx = 100
    p2_spawny = 400

    # Bullets
    bulletbill = pygame.image.load('images\shot.png')
    bulletbill = pygame.transform.scale(bulletbill, (bull_scale, bull_scale))
    bulletbill1 = pygame.image.load('images\shot(ROT_LEFT)')
    bulletbill1 = pygame.transform.scale(bulletbill, (bull_scale, bull_scale))
    player1 = player(ship, p1_spawnx, p1_spawny)
    player2 = player(elephant, p2_spawnx, p2_spawny)
    p1_bullets = []
    p2_bullets = []

    # define startup as running
    running = True
    endgame = False
    pygame.key.set_repeat(500, 30)
    timer = 0
    timer1 = 0
    # define game
    while running:
        # draw players every update
        screen.blit(scaled_img, (0, 0))
        for bullet in p1_bullets:
            if bullet.is_hit(player2):
                running = False
                endgame = True
            if bullet.x > 800 or bullet.x < 0:
                p1_bullets.remove(bullet)
            if bullet.is_colliding():
                bullet.collision()
                print('collision!')
            bullet.x += bullet.dx
            bullet.y += bullet.dy
            bullet.draw()

        for bullet in p2_bullets:
            if bullet.is_hit(player1):
                running = False
                endgame = True
            if bullet.x > 800 or bullet.x < 0:
                p2_bullets.remove(bullet)
            if bullet.is_colliding():
                bullet.collision()
                print('collision!')
            bullet.x += bullet.dx
            bullet.y += bullet.dy
            bullet.draw()

        player1.draw()
        player2.draw()

        # define game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # Define all keys currently pressed
            keys = pygame.key.get_pressed()

            # Player 1 events
            if keys[pygame.K_RIGHT]:
                player1.step('right')
            if keys[pygame.K_LEFT]:
                player1.step('left')
            if keys[pygame.K_UP]:
                player1.step('down')
            if keys[pygame.K_DOWN]:
                player1.step('up')

            # Player 2 events
            if keys[pygame.K_d]:
                player2.step('right')
            if keys[pygame.K_a]:
                player2.step('left')
            if keys[pygame.K_w]:
                player2.step('down')
            if keys[pygame.K_s]:
                player2.step('up')

            # Bullet Events
            # Bullet Events
            if keys[pygame.K_m] and timer < 0:
                bullet = Bullet(player1)
                p1_bullets.append(bullet)
                timer = 75
            if keys[pygame.K_r] and timer1 < 0:
                bullet = Bullet(player2)
                p2_bullets.append(bullet)
                timer1 = 75

        timer -= 1
        timer1 -= 1
        pygame.display.update()

    while endgame:
        screen.fill((0, 0, 0))
        gameover = pygame.image.load('gameover.jpg')
        screen.blit(gameover, (100, 200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endgame = False

    pygame.quit()
