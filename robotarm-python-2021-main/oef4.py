from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for i in range(5):
    robotArm.grab()
    for stapel in range(0, 2):
        robotArm.moveRight()
    robotArm.drop()
    for stapel in range(0, 2):
        robotArm.moveLeft()
robotArm.moveRight()
for i in range(5):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()