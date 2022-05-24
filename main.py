import pygame
import playerControl
import obstacleControl

pygame.init()
pygame.display.set_caption("Mazer")
screen = pygame.display.set_mode((1200, 600), pygame.RESIZABLE)

FPS = 60
fpsClock = pygame.time.Clock()

player = playerControl.Player('white', [10, 10], 20, 5)

# plan out the actual outline of the maze, then create the walls for the maze
# consider any other types of objects - a moving wall, keys, items

walls = [
]

playerDelay = 0

quitVar = True

while quitVar:
    screen.fill('black')

    player.playerDraw(screen)
    
    for wall in walls:
        wall.obstacleDraw(screen)
        if player.playerRect.colliderect(wall.obstacleRect):
            playerDelay = 25
            player.pos = [10, 10]

    keys = pygame.key.get_pressed()

    if playerDelay <= 0:
        if keys[pygame.K_UP]: player.moveNorth()

        if keys[pygame.K_DOWN]: player.moveSouth()

        if keys[pygame.K_RIGHT]: player.moveEast()

        if keys[pygame.K_LEFT]: player.moveWest()

    else:
        playerDelay -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()