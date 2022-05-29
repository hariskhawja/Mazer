import pygame
import playerControl
import obstacleControl 
import obstacleInitialise

pygame.init()
pygame.display.set_caption("Mazer")
screen = pygame.display.set_mode((1200, 600), pygame.RESIZABLE)

FPS = 60
fpsClock = pygame.time.Clock()

player = playerControl.Player('white', [10, 10], 20, 5)

quitVar = True

while quitVar:
    screen.fill('black')

    player.playerDraw(screen)
    
    for obstacle in obstacleInitialise.obstaclesList:
        obstacle.obstacleDraw(screen)
        if player.playerRect.colliderect(obstacle.obstacleRect):
            player.playerDelay = 25
            player.pos = [10, 10]

    keys = pygame.key.get_pressed()

    if player.playerDelay <= 0:
        if keys[pygame.K_UP]: player.moveNorth()

        if keys[pygame.K_DOWN]: player.moveSouth()

        if keys[pygame.K_RIGHT]: player.moveEast()

        if keys[pygame.K_LEFT]: player.moveWest()

    else:
        player.playerDelay -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()