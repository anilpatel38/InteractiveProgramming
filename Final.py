import pygame
# import math
import random


class player(pygame.sprite.Sprite):
    """
    Class to create a player sprite. Instantiated in the game twice, once for
    each player.
    """

    # initialize the player's sprite
    def __init__(self, surface, x, y):
        """
        Define the surface for display, abstract as a rectangle, x and y
        position. Initialize with an x and y value and a surface image.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = [self.x, self.y]

    # define steps
    def step(self, key):
        """
        Use this function to translate keystrokes into an updated location
        depending on which key is pressed. Takes in a "key" label which is
        determined in the key events section of the code.
        """

        """
        The if statements before each movement are to constrain the players
        to only move in within the view box of the game.
        """
        if self.x < 725:
            if key == 'right':
                self.x = self.x + 10
        if self.x > 5:
            if key == 'left':
                self.x = self.x - 10
        if self.y < 525:
            if key == 'down':
                self.y = self. y + 10
        if self.y > 5:
            if key == 'up':
                self.y = self.y - 10

    def draw(self):
        """
        Function used for displaying characters.
        """
        screen.blit(self.image, (self.x, self.y))


class Bullet(pygame.sprite.Sprite):
    """
    Class for bullets. Instantiated every time the player shoots.
    """

    # initialize the bullet
    def __init__(self, player, speed=1):
        """
        Define the bullets as sprites. Takes in a player object so that the
        bullet is appropriately spawned at the player who shoots it. Abstracts
        the bullet as a rectangle the size of the sprite.
        """
        pygame.sprite.Sprite.__init__(self)
        self.x = player.x
        self.y = player.y
        self.speed = speed
        """
        The following if/elif statement is used to spawn bullets moving in the
        correct direction depending on which side of the screen the player is
        on. This also generates a different surface for different direction of
        bullet travel. The random initial velocity is for fun and adds angles
        for bullets to bounce off the ceilings of the game.
        """
        if player.x > 400:
            self.image = bulletbill1
            self.dx = random.randrange(-3, -1)*self.speed
            self.dy = random.randrange(-10, 10)/50*self.speed
        elif player.x < 400:
            self.image = bulletbill
            self.dx = random.randrange(1, 3)*self.speed
            self.dy = random.randrange(-10, 10)/10*self.speed
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = [self.x, self.y]

    def draw(self):
        """draw the bullets."""
        screen.blit(self.image, (self.x, self.y))

    def is_hit(self, player):
        """Long-winded function used to check for player collision. It tracks
         overlapping pixels in the bullets and the player that is being passed
         into the function. Did it this way because we couldn't get pygame's
         sprite collision to function properly"""

        # create list of x and y values for bullet and player
        bulletx = []
        playerx = []
        bullety = []
        playery = []

        # put all x and y's in lists, there's def a better way to do this.
        # +5/-5 and +25/-25 accounts for the size of the surfaces.
        for i in range(int(self.x)-5, int(self.x) + 5):
            bulletx.append(i)
        for j in range(int(player.x)-25, int(player.x)+25):
            playerx.append(j)
        for l in range(int(self.y)-5, int(self.y) + 5):
            bullety.append(l)
        for m in range(int(player.y)-25, int(player.y)+25):
            playery.append(m)

        # check to see if x and y values are corresponding in a collision.
        for i in range(0, len(bulletx)):
            if bulletx[i] in playerx and bullety[i] in playery:
                return True
        return False

    def is_colliding(self):
        """Check for collisions with top and bottom wall. 5 and 595 account
        for size of the surface."""
        if self.y <= 5 or self.y >= 595:
            return True
        return False

    def collision(self):
        """Adjusts the velocity of the bullet if it collides with the top or
        bottom of the screen."""
        self.dy = self.dy*-1


if __name__ == "__main__":
    img = pygame.image.load('images\space.jpg')  # background image
    width = 800  # screen size
    height = 600
    player_scale = 75  # scaling for images
    bull_scale = 20
    scaled_img = pygame.transform.scale(img, (width, height))
    screen = pygame.display.set_mode((800, 600))  # define screen to blit on
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
    # Initialize lists of bullets for each player
    p1_bullets = []
    p2_bullets = []

    # define startup as running and gameover screen as false
    running = True
    endgame = False

    # define repeat key as on so that press and hold keys moves players
    pygame.key.set_repeat(500, 30)
    timer = 0
    timer1 = 0
    # define game
    while running:
        # blit background first
        screen.blit(scaled_img, (0, 0))

        # loop all the bullets in player 1's list.
        for bullet in p1_bullets:
            # check for collision with player 2
            if bullet.is_hit(player2):
                # go to endgame is player is hit.
                running = False
                endgame = True
            if bullet.x > 800 or bullet.x < 0:
                # remove bullets off screen
                p1_bullets.remove(bullet)
            if bullet.is_colliding():
                # change velocity when top/bottom wall collision.
                bullet.collision()
                print('collision!')
            # update regularly if no special events are invoked.
            bullet.x += bullet.dx
            bullet.y += bullet.dy
            # draw each bullet
            bullet.draw()

        # do the same for player2 bullets
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

        # draw current position of player 1 and 2
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

            # Player 1 movement events
            if keys[pygame.K_RIGHT]:
                player1.step('right')
            if keys[pygame.K_LEFT]:
                player1.step('left')
            if keys[pygame.K_UP]:
                player1.step('up')
            if keys[pygame.K_DOWN]:
                player1.step('down')

            # Player 2 movement events
            if keys[pygame.K_d]:
                player2.step('right')
            if keys[pygame.K_a]:
                player2.step('left')
            if keys[pygame.K_w]:
                player2.step('up')
            if keys[pygame.K_s]:
                player2.step('down')

            # Use timers to prevent spam bullets.
            if keys[pygame.K_m] and timer < 0:
                bullet = Bullet(player1)
                p1_bullets.append(bullet)
                timer = 75
            if keys[pygame.K_r] and timer1 < 0:
                bullet = Bullet(player2)
                p2_bullets.append(bullet)
                timer1 = 75

        # update timers
        timer -= 1
        timer1 -= 1
        pygame.display.update()

    # Define engame graphics
    while endgame:
        screen.fill((0, 0, 0))
        gameover = pygame.image.load('gameover.jpg')
        screen.blit(gameover, (100, 200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endgame = False

    pygame.quit()
