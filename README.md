# UBTech
UBTech robot Bluetooth communication protocal

﻿有高手分析出几条协议，如下：
通讯协议格式（固定长度10字节）：
帧头（2字节）ID（1字节）命令(1字节)参数(4字节) SUM(1字节)帧尾(1字节)
帧头:FA AF，帧尾:ED，SUM=ID+命令+参数，取最低位1字节
命令可以按01..FF，顺序实验。
目前已实验的命令（CD命令是修改舵机id）：
读数据：FA AF id 02 00 00 00 00 SUM ED
舵机应答：FA AF id AA     实际角度 sum ED
写舵机：FA AF id 01 角度       SUM ED
FA AF 01 04 01 00 00 00 06 ED 关闭led灯
FA AF 01 04 00 00 00 00 05 ED 打开led灯
修改舵机ID：FA AF ID CD 0 newid 0 0 SUM ED


蓝牙通讯:

BT握手机器
fb bf 06 01 00 07 ed
获取动作表
fb bf 06 02 00 08 ed
心跳包
fb bf 06 08 00 0E ed
读取机器状态
fb bf 06 0A 00 10 ed
音量调节//val=00-ff
fb bf 06 0B val chk ed
所有舵机掉电
fb bf 06 0C 00 12 ed
所有舵机灯控制//00关,01开
fb bf 06 0D 00 13 ed
fb bf 06 0D 01 14 ed

读机器电池电量
fb bf 06 18 00 1e ed
返回:FB BF 09 18 22 DD 01 64 85 ED
参数1（2B）：电压值（mV）
参数2（1B）：是否充电 （0X00-否，0X01-是 ，0X02-没有电池）
参数3（1B）： 电量百分比(0~100)

控制单一舵机运动
//01号舵机转向到40度(0x28),时间255*20ms(0xff)
fb bf 0a 22 01 28 ff 00 ff 53 ed
//01舵机转到0度,时间1秒
fb bf 0a 22 01 00 32 00 ff 5e ed
//01舵机转到180度,时间1秒
fb bf 0a 22 01 b4 32 00 ff 12 ed
//01舵机转到180度,时间255*20ms(0xff)
fb bf 0a 22 01 b4 ff 00 ff df ed

回读单个舵机角度（掉电）
fb bf 06 24 01 2b ed

设置单个舵机偏移值
//13号舵机偏移值设置为ff f2
fb bf 08 26 0d ff f2 2c ed
fb bf 08 26 0b 00 10 49 ed

读取单个舵机偏移值
fb bf 06 28 01 2f ed
fb bf 06 28 02 30 ed
fb bf 06 28 0d 3b ed
fb bf 06 28 0b 39 ed
