import pygame
import playerControl
import obstacleControl

pygame.init()
pygame.display.set_caption("Mazer")
screen = pygame.display.set_mode((1200, 600), pygame.RESIZABLE)

FPS = 60
fpsClock = pygame.time.Clock()

player = playerControl.Player((100, 0, 100), 10, 10, 50, 5)
obstacle1 = obstacleControl.Obstacle('blue', 300, 500, 100, 25)
nav = [True, True, True, True]

quitVar = True

while quitVar:
    screen.fill([0, 100, 0])

    player.playerDraw(screen)
    obstacle1.obstacleDraw(screen)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and nav[0]: 
        if player.playerRect.colliderect(obstacle1.obstacleRect):
            nav[0] = False
        
        else:
            player.moveNorth()
            nav[1] = True

    if keys[pygame.K_DOWN] and nav[1]: 
        if player.playerRect.colliderect(obstacle1.obstacleRect):
            nav[1] = False
        
        else:
            player.moveSouth()
            nav[0] = True

    if keys[pygame.K_RIGHT] and nav[2]: 
        if player.playerRect.colliderect(obstacle1.obstacleRect):
            nav[2] = False

        else:
            player.moveEast()
            nav[3] = True

    if keys[pygame.K_LEFT] and nav[3]: 
        if player.playerRect.colliderect(obstacle1.obstacleRect):
            nav[3] = False
        
        else:
            player.moveWest()
            nav[2] = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()