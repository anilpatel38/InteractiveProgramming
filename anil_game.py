import pygame


class Rectangle(object):
    def __init__(self):
        self.x = 400
        self.y = 300
        self.width = 50
        self.height = 50

    def step(self, key):
        if key == 'right':
            self.x = self.x + 10

        if key == 'left':
            self.x = self.x - 10

        if key == 'up':
            self.y = self.y + 10

        if key == 'down':
            self.y = self.y - 10

    def draw(self, screen):
        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (100, 100, 100), self.rectangle)


if __name__ == "__main__":
    img = pygame.image.load('images\space.jpg')
    width = 800
    height = 600
    scaled_img = pygame.transform.scale(img, (width, height))
    screen = pygame.display.set_mode((800, 600))
    screen.blit(scaled_img, (0, 0))
    pygame.display.set_caption('PyGame App!')

    pygame.init()

    # initialize 2 players
    player1 = Rectangle()
    player2 = Rectangle()

    # define startup as running
    running = True

    # define game
    while running:
        # draw players every update
        player1.draw(screen)
        player2.draw(screen)

        # define game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Player 1 events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player1.step('right')
                    screen.blit(scaled_img, (0, 0))
                if event.key == pygame.K_LEFT:
                    player1.step('left')
                    screen.blit(scaled_img, (0, 0))
                if event.key == pygame.K_UP:
                    player1.step('down')
                    screen.blit(scaled_img, (0, 0))
                if event.key == pygame.K_DOWN:
                    player1.step('up')
                    screen.blit(scaled_img, (0, 0))

            # Player 2 events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        player2.step('right')
                        screen.blit(scaled_img, (0, 0))
                    if event.key == pygame.K_a:
                        player2.step('left')
                        screen.blit(scaled_img, (0, 0))
                    if event.key == pygame.K_s:
                        player2.step('down')
                        screen.blit(scaled_img, (0, 0))
                    if event.key == pygame.K_w:
                        player2.step('up')
                        screen.blit(scaled_img, (0, 0))

        pygame.display.update()

    pygame.quit()
