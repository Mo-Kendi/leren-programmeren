from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 5
robotArm.moveRight()
for y in range(3):
    for x in range(1):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for i in range(1):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()