import pygame

class Planets(pygame.sprite.Sprite):

    def __init__(self, colour, width, height, speed):
                 super().__init__()

                 self.image = pygame.Surface([width, height])

                 self.width = width
                 self.height = height
                 self.colour = colour
                 self.speed = speed

                 pygame.draw.ellipse(self.image, self.colour, [0, 0, self.width, self.height])

                 self.ellipse = self.image.get_ellipse()
