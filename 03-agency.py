# 位置设置来自：https://www.bilibili.com/read/cv6217965
import os
import re
import time
import datetime
import subprocess

device_name = '127.0.0.1:7555' #网易MuMu模拟器
default_num = 114514

# adb -s 127.0.0.1:7555 shell pidof com.hypergryph.arknights.bilibili
# adb -s 8854929c shell dumpsys package com.hypergryph.arknights
# adb logcat | findstr com.hypergryph.arknights >d:\hyper.log
# adb logcat | findstr com.hypergryph.arknights.bilibili >d:\bili.log
# adb logcat -D | findstr HGGameBi POST
# adb logcat | findstr 1548
# adb shell am start com.hypergryph.arknights.bilibili/com.u8.sdk.SplashActivity

def deal_cmd(cmd):
	'''
	创建子进程管道，以获取adb命令执行的结果
	'''
	pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	return pi.stdout.read()

def fight(wait_time):
	num = int(input('请输入要代理作战的次数：'))
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
			click(pos_dict['开始'],2)
			i = i+1
		time.sleep(wait_time)
		click(pos_dict['开始'],2)
		k = k+1
		print('\n第%d次代理完成，等待%d秒' %(k, wait_time))
	print('\n已完成%d次代理作战，退出...' % num)
'''
①截图，识别当前理智、本次作战所需理智
②计算能够作战次数，通过网络上传时间计算
'''
def wait():
	a = deal_cmd('adb logcat -t "400" -s WifiService:E')
	a = a.decode("utf-8")
	a = re.sub(r'\--.+\n','',a)
	a = a.strip().split('\n')
	#os.system('adb logcat -c')
	c = {}
	for i in range(0,4):
		b = a[i].split()[1]
		b = datetime.datetime.strptime(b.split('.')[0],'%H:%M:%S')
		c[i] = b
	wait_time = datetime.timedelta.total_seconds(c[3] - c[0])
	print(wait_time)
	return wait_time

if __name__ == '__main__':
	wait_time = int(wait())
	fight(wait_time)
	