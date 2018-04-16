from UBTech import *

robot = UBTech(12)
#robot.sendCmd(COMMAND.controlSigleServo,[0x01,0x00,0x32,0x00,0xff])
#robot.controlSigleServo(1,180,1000,5100)
#robot.handShack()
#robot.soundSwitch(1)
#robot.setVolumn(100)
robot.timeAdjust(18,4,16,9,28,30)
robot.setSingleServoOffset(-1)
