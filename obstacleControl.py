import pygame

class Obstacle:
    def __init__(self, colour, points):
        self.colour = colour
        self.points = points

    def obstacleDraw(self, screen):
        # this only applies to polygons with 4 points (need to be more versatile)
        pygame.draw.polygon(screen, self.colour, ((self.points[0], self.points[1]), (self.points[2], self.points[3]), (self.points[4], self.points[5]), (self.points[6], self.points[7])))