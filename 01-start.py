import subprocess
import os
import time

def deal_cmd(cmd):
	'''
	创建子进程管道，以获取adb命令执行的结果
	'''
	pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	return pi.stdout.read()

def mumu():
	'''
	将127.0.0.1:7555端口分配给MUMU模拟器
	'''
	result = deal_cmd('adb connect 127.0.0.1:7555')
	result = result.decode("utf-8")
	if result.startswith('already connected to'):
		return

def check():
	result = deal_cmd('adb devices -l')
	result = result.decode("utf-8")
	if result.startswith('List of devices attached'):
			# 查看连接设备
		result = result.strip().splitlines()
			# 查看连接设备数量，截取结果的行数
		device_size = len(result)
		if device_size > 1:
			device_dict = {}
			device_name = []
			device_num = []
			for i in range(1, device_size):
				device_detail = result[i].replace(" "*9,"\t").split("\t")	
				if 'device' in device_detail[1]:
					device_dict[device_detail[1].split()[2].split(":")[1]] = device_detail[0]
					device_name.append(device_detail[1].split()[2].split(":")[1])
					device_num.append(device_detail[0])
				elif device_detail[1] == 'offline':
					print(device_detail[0])
					print('连接出现异常，设备无响应')
				elif device_detail[1] == 'unknown':
					print(device_detail[0])
					print('没有连接设备')
				print('设备%s的序列号是%s' % (device_name[i-1],device_num[i-1]))
		else:
			print('没有可用设备')
	return device_dict

def startapp(serverid):
	'''
	①选择服务器，打开app
	目前仅适合未有更新、未有活动的状态
	'''
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

if __name__ == '__main__':
	mumu()
	device_name = check()[input('请输入将要使用的设备名：')]
	serverid = input('请输入服务器：官服（1）/B服（2）')
	startapp(serverid)