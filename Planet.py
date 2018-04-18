import pygame
WHITE = (255, 255, 255)

class Planets(pygame.sprite.Sprite):

    def __init__(self, colour, width, height, speed):
                 super().__init__()

                 self.image = pygame.Surface([width, height])
                 self.image.fill(WHITE)
                 self.image.set_colorkey(WHITE)

                 self.width = width
                 self.height = height
                 self.colour = colour
                 self.speed = speed

                 pygame.draw.ellipse(self.image, self.colour, [0, 0, self.width, self.height])

                 self.rect = self.image.get_rect()

                 
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
