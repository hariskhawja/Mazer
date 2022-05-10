import pygame

class Obstacle:
    def __init__(self, colour, x, y, length, extender):
        self.colour = colour
        self.x = x
        self.y = y
        self.length = length
        self.extender = extender

    def obstacleDraw(self, screen):
        if self.extender:
            pygame.draw.rect(screen, self.colour, (self.x, self.y, self.length, 10))