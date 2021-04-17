# 位置设置来自：https://www.bilibili.com/read/cv6217965
import os
import time
from cnocr import CnOcr, NUMBERS

device_name = '127.0.0.1:7555' #网易MuMu模拟器
default_num = 114514

# adb -s 8854929c shell pidof com.hypergryph.arknights.bilibili
# adb -s 8854929c shell dumpsys package com.hypergryph.arknights
# adb logcat | findstr com.hypergryph.arknights >d:\hyper.log
# adb logcat | findstr com.hypergryph.arknights.bilibili >d:\bili.log
# adb logcat | findstr 1548
# adb shell am start com.hypergryph.arknights.bilibili/com.u8.sdk.SplashActivity
'''
①选择服务器，打开app
目前仅适合未有更新、未有活动的状态
'''
def startapp(serverid):
	serverid = input('请输入服务器：官服（1）/B服（2）')
	if (serverid == '1' or serverid == '官服'):
		appactivity = 'com.hypergryph.arknights/com.u8.sdk.U8UnityContext'
		i = 1
	else:
		appactivity = 'com.hypergryph.arknights.bilibili/com.u8.sdk.SplashActivity'
		i = 2
	command1 = 'adb -s %s shell am start %s' % (device_name, appactivity)
	os.system(command1)
	for i in range(2):
		time.sleep(15)
		command2 = 'adb -s %s shell input tap %d %d' % (device_name, 640,560)
		os.system(command2)
		i = i + 1
def fight():
	num = int(input('请输入要代理作战的次数：'))
	wait = int(input('请输入每局作战时间：'))
	pos_dict = {
		'开始': (1108,656)
	}
	def click(pos, sleep=0.5):
		command = 'adb -s %s shell input tap %d %d' % (device_name, int(pos[0]), int(pos[1]))
		#print(command)
		os.system(command)
		time.sleep(sleep)
	for k in range(num):
		for i in range(2):
			click(pos_dict['开始'],1)
			i = i+1
		time.sleep(wait)
		click(pos_dict['开始'],1)
		k = k+1
	print('\n已完成%d次代理作战，退出...' % num)
'''
①截图，识别当前理智、本次作战所需理智
②计算能够作战次数
'''
if __name__ == '__main__':
	#startapp(serverid)
	fight()
	