import pygame
import math


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
        if key == 'right':
            self.x = self.x + 10

        if key == 'left':
            self.x = self.x - 10

        if key == 'up':
            self.y = self. y + 10

        if key == 'down':
            self.y = self.y - 10

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Bullet(pygame.sprite.Sprite):

    speed = 10

    # initialize the bullet
    def __init__(self, surface, player):
        pygame.sprite.Sprite.__init__(self)
        self.x = player.x
        self.y = player.y
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = [self.x, self.y]

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def is_colliding(self):
        if self.y >= 550 or self.y <= 0:
            return True
        return False


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
    ship = pygame.image.load('images\ship.png')
    ship = pygame.transform.scale(ship, (player_scale, player_scale))
    p1_spawnx = 700
    p1_spawny = 400

    # Player 2
    elephant = pygame.image.load('Elephant.png')
    elephant = pygame.transform.scale(elephant, (player_scale, player_scale))
    p2_spawnx = 100
    p2_spawny = 400

    # Bullets
    bulletbill = pygame.image.load('images\shot.png')
    bulletbill = pygame.transform.scale(bulletbill, (bull_scale, bull_scale))

    player1 = player(ship, p1_spawnx, p1_spawny)
    player2 = player(elephant, p2_spawnx, p2_spawny)
    p1_bullets = []
    p2_bullets = []

    # define startup as running
    running = True
    pygame.key.set_repeat(500, 30)

    # define game
    while running:
        # draw players every update
        screen.blit(scaled_img, (0, 0))
        for bullet in p1_bullets:
            if bullet.x > 800:
                p1_bullets.remove(bullet)
            bullet.x += 1
            bullet.y += 0.25
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
            if keys[pygame.K_m]:
                bullet = Bullet(bulletbill, player2)
                p1_bullets.append(bullet)

        pygame.display.update()

    pygame.quit()
