from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
place = 9
move = True
while move:
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        print('nothing to grab')
        move = False    
    else:
        for arm in range(place):
            robotArm.moveRight()
        robotArm.drop()
        for arm in range(place):
            robotArm.moveLeft()
        place -=1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()