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
    box = Rectangle()
    running = True
    while running:
        box.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    box.step('right')
                    screen.blit(scaled_img, (0, 0))
                if event.key == pygame.K_LEFT:
                    box.step('left')
                    screen.blit(scaled_img, (0, 0))
                if event.key == pygame.K_UP:
                    box.step('down')
                    screen.blit(scaled_img, (0, 0))
                if event.key == pygame.K_DOWN:
                    box.step('up')
                    screen.blit(scaled_img, (0, 0))
        pygame.display.update()

    pygame.quit()
