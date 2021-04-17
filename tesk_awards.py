import os
import time
from cnocr import CnOcr, NUMBERS

device_name = '127.0.0.1:7555' #网易MuMu模拟器
def getRewards():
	#pic_name = 'MRFZ' + time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
	#os.system('adb -s %s shell screencap -p /sdcard/%s.png' % (device_name, pic_name))
	ocr = CnOcr()
	screen = 'C:/Users/Si/Desktop/Snipaste_2021-04-11_14-32-51.jpg'
	res = ocr.ocr(screen)
	print("Predicted Chars:", res)
	#for i in ocr.ocr(screen):
	#	print(i)
def getAward(award_num, award_type):
	act_dict = {
		"获取" : (1050,150),
		"见习" : (),
		"日常" : (),
		"周常" : (),
		"主线" : ()
	}
	def click(act, sleep=0.5):
		command = 'adb -s %s shell input tap %d %d' % (device_name, int(act[0]), int(act[1]))
			#print(command)
		os.system(command)
		time.sleep(sleep)
	for k in range(award_num):
		for k in range(2):
			click(act_dict['获取'],1)
	
	print("%d个%s任务奖励已领取" % (award_num, award_type))
if __name__ == '__main__':
	award_num = int(input("请输入任务奖励的数量"))
	award_type = input("请输入任务奖励的类型（见习/日常/周常/主线）")
	getAward(award_num, award_type)