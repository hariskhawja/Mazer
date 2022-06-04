import obstacleControl

obstaclesFile = open("obstacles.txt", "r")

obstaclesList = []

while True:
    currentLine = obstaclesFile.readline().split()

    if not currentLine:
        obstaclesFile.close()
        break

    if currentLine[0] == "VERTICAL":
        obstaclesList.append(obstacleControl.VerticalMovingObstacle(currentLine[1], int(currentLine[2]), int(currentLine[3]), int(currentLine[4]), int(currentLine[5]), int(currentLine[6]), int(currentLine[7])))

    elif currentLine[0] == "HORIZONTAL":
        obstaclesList.append(obstacleControl.HorizontalMovingObstacle(currentLine[1], int(currentLine[2]), int(currentLine[3]), int(currentLine[4]), int(currentLine[5]), int(currentLine[6]), int(currentLine[7])))

    else:
        obstaclesList.append(obstacleControl.Obstacle(currentLine[1], int(currentLine[2]), int(currentLine[3]), int(currentLine[4]), int(currentLine[5])))