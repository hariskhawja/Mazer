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

class VerticalMovingObstacle(Obstacle):
    def __init__(self, colour, x, y, xLen, yLen, targ, speed):
        Obstacle.__init__(self, colour, x, y, xLen, yLen)

        self.targ1 = self.y
        self.targ2 = targ
        self.speed = speed

    def obstacleDraw(self, screen):
        self.obstacleRect = pygame.draw.rect(screen, self.colour, (self.x, self.y, self.xLen, self.yLen))
        self.y += self.speed

        if self.y <= self.targ1 or self.y >= self.targ2: self.speed *= -1

class HorizontalMovingObstacle(VerticalMovingObstacle):
    def __init__(self, colour, x, y, xLen, yLen, targ, speed):
        VerticalMovingObstacle.__init__(self, colour, x, y, xLen, yLen, targ, speed)

        self.targ1 = self.x
    
    def obstacleDraw(self, screen):
        self.obstacleRect = pygame.draw.rect(screen, self.colour, (self.x, self.y, self.xLen, self.yLen))
        self.x += self.speed

        if self.x <= self.targ1 or self.x >= self.targ2: self.speed *= -1