#! python3
# _*_ coding:utf-8 _*_
import os
import winreg
import sys
import ctypes

def is_admin():
	'''获取管理员权限'''
	try:return ctypes.windll.shell32.IsUserAnAdmin()
	except:return False

def append_Path(value, type=winreg.REG_SZ, keyname='Path'):
	'''默认为键Path追加值(路径)'''
	if is_admin():	
		# 以管理员身份运行以下代码
		# 连接注册表根键HKEY_LOCAL_MACHINE
		regRoot = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
		subDir = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
		# 只读方式打开注册表
		key_read = winreg.OpenKey(regRoot, subDir)
		count = winreg.QueryInfoKey(key_read)[1]  # 获取该目录下所有键的个数(0-下属键个数;1-当前键值个数)
		for i in range(count):
			name,values,type_ = winreg.EnumValue(key_read, i)
			if name.lower() == keyname.lower():
				if values[-1] == ';':
					values += value
				else:
					values += f';{value}'
				# 以只写方式打开注册表
				key_write = winreg.OpenKey(regRoot, subDir, 0, winreg.KEY_WRITE)
				# 追加值
				winreg.SetValueEx(key_write, name, 0, type, values)
				winreg.CloseKey(key_write)
		winreg.CloseKey(key_read)
	else :
		if sys.version_info[0] == 3:
			ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
def RefreshEnv():
    HWND_BROADCAST = 0xFFFF
    WM_SETTINGCHANGE = 0x1A

    SMTO_ABORTIFHUNG = 0x0002

    result = ctypes.c_long()
    SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
    SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, u'Environment',
                        SMTO_ABORTIFHUNG, 5000, ctypes.byref(result))

if __name__ == '__main__':
	ENV =  sys.path[0]
	print(ENV)
	append_Path(ENV)
	RefreshEnv()