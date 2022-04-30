import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveNorth(self):
        self.y -= 1
    
    def moveSouth(self):
        self.y += 1

    def moveEast(self):
        self.x += 1
    
    def moveWest(self):
        self.x -= 1