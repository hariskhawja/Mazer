import pygame

class Player:
    def __init__(self, colour, pos, length, speed):
        self.colour = colour
        self.pos = pos
        self.length = length
        self.speed = speed

    def playerDraw(self, screen): 
        self.playerRect = pygame.draw.rect(screen, self.colour, (self.pos[0], self.pos[1], self.length, self.length))
        self.w, self.h = pygame.display.get_surface().get_size()

    def moveNorth(self):
        if self.pos[1] > 0: self.pos[1] -= self.speed
    
    def moveSouth(self):
        if self.pos[1] < self.h - self.length: self.pos[1] += self.speed

    def moveEast(self):
        if self.pos[0] < self.w - self.length: self.pos[0] += self.speed
    
    def moveWest(self):
        if self.pos[0] > 0: self.pos[0] -= self.speed