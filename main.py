import pygame
import playerControl
import obstacleInitialise

pygame.init()
pygame.display.set_caption("Mazer")
screen = pygame.display.set_mode((1200, 600), pygame.RESIZABLE)

FPS = 60
fpsClock = pygame.time.Clock()

player = playerControl.Player('white', [10, 10], 20, 3)

cheats = False

gameOver = False

quitVar = True

while quitVar:
    screen.fill('black')

    w, h = pygame.display.get_surface().get_size()

    if gameOver:
        pygame.draw.rect(screen, "gold", (w / 2 - 150, h / 2 + 100, 300, 10))
        pygame.draw.rect(screen, "gold", (w / 2 - 150, h / 2 - 100, 10, 200))
        pygame.draw.rect(screen, "gold", (w / 2 + 140, h / 2 - 100, 10, 200))
        pygame.draw.rect(screen, "gold", (w / 2 - 140, h / 2 - 100, 50, 10))
        pygame.draw.rect(screen, "gold", (w / 2 + 90, h / 2 - 100, 50, 10))
        pygame.draw.rect(screen, "gold", (w / 2 - 90, h / 2 - 100, 10, 75))
        pygame.draw.rect(screen, "gold", (w / 2 + 80, h / 2 - 100, 10, 75))
        pygame.draw.rect(screen, "gold", (w / 2 - 90, h / 2 - 25, 50, 10))
        pygame.draw.rect(screen, "gold", (w / 2 + 40, h / 2 - 25, 50, 10))
        pygame.draw.rect(screen, "gold", (w / 2 - 40, h / 2 - 150, 10, 135))
        pygame.draw.rect(screen, "gold", (w / 2 + 30, h / 2 - 150, 10, 135))
        pygame.draw.rect(screen, "gold", (w / 2 - 40, h / 2 - 150, 75, 10))

    else:
        player.playerDraw(screen)
    
        for obstacle in obstacleInitialise.obstaclesList:
            obstacle.obstacleDraw(screen)
            if player.playerRect.colliderect(obstacle.obstacleRect):
                if obstacle.colour == "green": gameOver = True
            
                if not cheats:
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c: cheats = not cheats

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()