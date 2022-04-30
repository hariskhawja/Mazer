import pygame
import playerControl
import obstacleControl

pygame.init()
pygame.display.set_caption("Mazer")
screen = pygame.display.set_mode((1200, 600), pygame.RESIZABLE)

FPS = 60
fpsClock = pygame.time.Clock()

quitVar = True

playerStats = [250, 250]
# player = playerControl.Player(255, 255)


while quitVar:
    screen.fill([0, 100, 0])
    player = pygame.draw.rect(screen, (255, 0, 0), (playerStats[0], playerStats[1], 100, 100))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        playerStats[1] -= 10

    if keys[pygame.K_DOWN]:
        playerStats[1] += 10
    
    if keys[pygame.K_RIGHT]:
        playerStats[0] += 10
    
    if keys[pygame.K_LEFT]:
        playerStats[0] -= 10


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False
        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerStats[1] += 1
            
            if event.key == pygame.K_DOWN:
                playerStats[1] -= 1

            if event.key == pygame.K_RIGHT:
                playerStats[0] += 1
            
            if event.key == pygame.K_LEFT:
                playerStats[0] -= 1'''

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()