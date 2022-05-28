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

obstacle1 = obstacleControl.Obstacle('white', 40, 0, 10, 250)
obstacle2 = obstacleControl.Obstacle('white', 40, 290, 10, 280)
vertMovObst1 = obstacleControl.VerticalMovingObstacle('white', 80, 0, 10, 300, -100, 1, 2)
vertMovObst2 = obstacleControl.VerticalMovingObstacle('white', 80, 300, 10, 300, 300, 500, 2)

walls = [
    obstacle1,
    obstacle2,
    vertMovObst1,
    vertMovObst2
]

quitVar = True

while quitVar:
    screen.fill('black')

    player.playerDraw(screen)
    
    for wall in walls:
        wall.obstacleDraw(screen)
        if player.playerRect.colliderect(wall.obstacleRect):
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