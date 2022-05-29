import obstacleControl

# vertical obstacles
vertObstacle1 = obstacleControl.Obstacle('white', 40, 0, 10, 250)
vertObstacle2 = obstacleControl.Obstacle('white', 40, 290, 10, 280)

# vertical moving obstacles
vertMovObst1 = obstacleControl.VerticalMovingObstacle('white', 80, -100, 10, 300, 0, 2)
vertMovObst2 = obstacleControl.VerticalMovingObstacle('white', 80, 240, 10, 450, 340, 2)

# horizontal obstacles
#horzObstacle1 = obstacleControl.Obstacle('white',)

# horizontal moving obstacles
horzMovObst1 = obstacleControl.HorizontalMovingObstacle('white', 200, 40, 100, 10, 400, 2)

obstaclesList = [
    vertObstacle1,
    vertObstacle2,
    vertMovObst1,
    vertMovObst2,
    horzMovObst1
]