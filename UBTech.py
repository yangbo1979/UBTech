#MIT license, http://opensource.org/licenses/MIT
#wrote by yangbo
#gyangbo@gmail.com
#feel free to use

import serial
from enum import Enum

class UBTech:
    'UBTech Robot BlueTooth Communication Protocol'
    ser=None
    serial_port = 1
    #serial_port="/dev/ttyUSB0"
    #serial_port=5#serial_port = 8  means serial id 9 in windows
    serial_timeout=1
    serial_baud = 256000
    def __init__(self,port):
        UBTech.serial_port = port
        ser = serial.Serial(port=serial_port, baudrate=serial_baud, bytesize=8, parity="N", stopbits=1, xonxoff=0)

    #BT握手机器
    def handShack(self):
        self.__sendCmd(COMMAND.handShack)
    #获取动作表
    def getActionList(self):
        self.__sendCmd(COMMAND.getActionList)
    #执行动作表
    #停止播放
    def stopPlay(self):
        self.__sendCmd(COMMAND.stopPlay)
    #声音开关,0 off 1 on
    def soundSwitch(self,switch):
        self.__sendCmd(COMMAND.soundSwitch,[hex(switch)])
    #播放控制,0 pause 1 continue
    def playControl(self,switch):
        self.__sendCmd(COMMAND.playControl,[hex(switch)])
    #心跳包
    def heartBeat(self):
        self.__sendCmd(COMMAND.heartBeat)
    #读取机器状态
    def getStatus(self):
        self.__sendCmd(COMMAND.getStatus)
    #音量调节,0~100
    def setVolumn(self,switch):
        self.__sendCmd(COMMAND.setVolumn,[hex(int(switch*25.5)%256)])
    #所有舵机掉电
    def allServoDown(self):
        self.__sendCmd(COMMAND.allServoDown)
    #所有舵机灯控制
    def allLightControl(self,switch):
        self.__sendCmd(COMMAND.allLightControl,[hex(switch)])
    #时钟校准,to be tested
    def timeAdjust(self,Y,M,d,h,m,s):
        arg = [hex(Y),hex(M),hex(d),hex(h),hex(m),hex(s)]
        self.__sendCmd(COMMAND.timeAdjust,arg)
    #读取闹钟参数
    def getAlarmPrams(self):
        self.__sendCmd(COMMAND.getAlarmPrams)
    #设置闹钟参数
    #读机器软件版本号
    def getVersion(self):
        self.__sendCmd(COMMAND.getVersion)
    #读机器电池电量
    def getBatt(self):
        self.__sendCmd(COMMAND.getBatt)
    #读机器硬件版本号
    def getHWVersion(self):
        self.__sendCmd(COMMAND.getHWVersion)
    #控制单一舵机运动
    def controlSigleServo(self,id,angle,time,timeout):
        arg = [hex(id),hex(angle),hex(int(time/20)),hex(int(timeout/20)//256),hex(int(timeout/20)%256)]
        self.__sendCmd(COMMAND.controlSigleServo,arg)
    #控制多个舵机运动,to be tested
    def controlMultiServo(self,angles,time,timeout):
        arg = []
        for i in angles:
            arg.append(hex(i))
        arg.append([hex(int(time/20)),hex(int(timeout/20)//256),hex(int(timeout/20)%256)])
        self.__sendCmd(COMMAND.controlMultiServo,arg)
    #回读单个舵机角度（掉电）
    def getServoAngle(self,id):
        self.__sendCmd(COMMAND.getServoAngle,[hex(id)])
    #回读多个舵机角度（掉电）
    def getServoesAngle(self):
        self.__sendCmd(COMMAND.getServoesAngle)
    #设置单个舵机偏移值
    def setSingleServoOffset(self,id,offset):
        offset = offset + 65536
        self.__sendCmd(COMMAND.setSingleServoOffset,[hex(id),hex(int(offset)//256),hex(int(offset)%256)])
    #设置多个舵机偏移值
    #读取单个舵机偏移值
    def getSingleServoOffset(self,id):
        self.__sendCmd(COMMAND.getSingleServoOffset,[hex(id)])
    #读取多个舵机偏移值
    def getMultiServoeOffset(self):
        self.__sendCmd(COMMAND.getMultiServoeOffset)
    #读单个舵机版本
    def getSingleServoVersion(self,id):
        self.__sendCmd(COMMAND.getSingleServoVersion,[hex(id)])
    #读多个舵机版本
    def getMultiServoesVersion(self):
        self.__sendCmd(COMMAND.getMultiServoesVersion)
    #读机器SN号
    def getSN(self):
        self.__sendCmd(COMMAND.getSN)
    #读主芯片UDID号
    def getUDID(self):
        self.__sendCmd(COMMAND.getUDID)




    def __sendCmd(self,cmd,paras=['0x00']):
        result = [hex(0xfb),hex(0xbf)]
        cmdLen = len(paras)+5
        chk = cmdLen
        result.append(hex(cmdLen))
        result.append(hex(cmd.value))
        chk += cmd.value
        for i in paras:
            result.append(i)
            chk += int(i,16)
        chk = chk%256
        result.append(hex(chk))
        result.append(hex(0xed))
        ser.write(result)
        #print(result)


class COMMAND(Enum):
    handShack = 0x01
    getActionList = 0x02
    execAction = 0x03
    stopPlay = 0x05
    soundSwitch = 0x06
    playControl = 0x07
    heartBeat = 0x08
    getStatus = 0x0a
    setVolumn = 0x0b
    allServoDown = 0x0c
    allLightControl = 0x0d
    timeAdjust = 0x0e
    getAlarmPrams = 0x0f
    setAlarmPrams = 0x10
    getVersion = 0x11
    getBatt = 0x18
    getHWVersion = 0x20
    controlSigleServo = 0x22
    controlMultiServo = 0x23
    getServoAngle = 0x24
    getServoesAngle = 0x25
    setSingleServoOffset = 0x26
    getSingleServoOffset = 0x27
    getMultiServoeOffset = 0x29
    getSingleServoVersion = 0x2a
    getMultiServoesVersion = 0x2b
    getSN = 0x33
    getUDID = 0x34
