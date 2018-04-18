from UBTech import *

robot = UBTech('COM15')
#robot.handShack()
#robot.controlSigleServo(1,135,100,5100)
robot.controlMultiServo([45,89,91,45,92,85,80],1000,5100)
#robot.soundSwitch(1)
#robot.setVolumn(100)
#robot.timeAdjust(18,4,16,9,28,30)
#robot.setSingleServoOffset(-1)


#robot.disconnect()
