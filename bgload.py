import pygame


class Rectangle(object):
    def __init__(self):
        self.x = 400
        self.y = 300
        self.width = 50
        self.height = 50

    def step(self, key):
        speed = 2
        if key == 'right':
            self.x += 10

        if key == 'left':
            self.x -= 10

        if key == 'up':
            self.y += 10

        if key == 'down':
            self.y -= 10

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
    player1 = pygame.image.load('images\ship.png')
    player1 = pygame.transform.scale(player1, (50, 50))
    spritex = 400
    spritey = 300
    pygame.init()
    box = Rectangle()
    running = True
    while running:
        screen.blit(player1, (spritex, spritey))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                spritex += 10
                screen.blit(scaled_img, (0, 0))
            if keys[pygame.K_LEFT]:
                spritex -= 10
                screen.blit(scaled_img, (0, 0))
            if keys[pygame.K_UP]:
                spritey -= 10
                screen.blit(scaled_img, (0, 0))

            if keys[pygame.K_DOWN]:
                spritey += 10
                screen.blit(scaled_img, (0, 0))
        pygame.display.update()

    pygame.quit()
