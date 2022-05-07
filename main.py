import pygame
import playerControl
import obstacleControl

pygame.init()
pygame.display.set_caption("Mazer")
screen = pygame.display.set_mode((1200, 600), pygame.RESIZABLE)

FPS = 60
fpsClock = pygame.time.Clock()

player = playerControl.Player((100, 0, 100), 10, 10, 50, 10)

quitVar = True

while quitVar:
    screen.fill([0, 100, 0])

    player.playerDraw(screen)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]: player.moveNorth() 

    if keys[pygame.K_DOWN]: player.moveSouth()

    if keys[pygame.K_RIGHT]: player.moveEast()

    if keys[pygame.K_LEFT]: player.moveWest()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()