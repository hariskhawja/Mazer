import pygame

class Player:
    def __init__(self, colour, x, y, length, speed):
        self.colour = colour
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed

    def playerDraw(self, screen): 
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.length, self.length))
        self.w, self.h = pygame.display.get_surface().get_size()

    def moveNorth(self):
        if self.y > 0: self.y -= self.speed
    
    def moveSouth(self):
        if self.y < self.h - self.length: self.y += self.speed

    def moveEast(self):
        if self.x < self.w - self.length: self.x += self.speed
    
    def moveWest(self):
        if self.x > 0: self.x -= self.speed