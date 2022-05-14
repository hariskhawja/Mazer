import pygame

class Obstacle:
    def __init__(self, colour, x, y, xLen, yLen):
        self.colour = colour
        self.x = x
        self.y = y
        self.xLen = xLen
        self.yLen = yLen

    def obstacleDraw(self, screen):
        self.obstacleRect = pygame.draw.rect(screen, self.colour, (self.x, self.y, self.xLen, self.yLen))