# ArkAutoHR

明日方舟自动公开招募，使用adb控制安卓模拟器，实现公开招募的全自动脚本，使用python3编写

forked from [shuangluoxss/ArkAutoHR](https://github.com/shuangluoxss/ArkAutoHR)

为其增添一些便利性而非实质功能性的更新

## 更新说明

1. 增加`platform-tools`压缩包，提供Android SDK Platform Tools 30.0.5。
2. 增加`write_in_path.py`，自动将`adb.exe`所在文件夹加入环境变量。
3. 在`auto_hr.py`中增添输入设备编号、公招次数代码。
4. 增加一个批处理文件`set_port_to_MuMu.bat`，为MuMu模拟器（1.1.1.4_nochannel_zh-Hans）64位添加7775端口。

## 需求

脚本依赖[cnocr](https://github.com/breezedeus/cnocr)与cv2等python库。

使用pip安装依赖库

建议使用清华源，建议使用python3.6环境

cnocr：`pip install cnocr`

cv2：`pip install opencv-python`

## 展示

实现思路与运行效果参考此视频：https://www.bilibili.com/video/BV1jh411k7r9/

## 使用说明

1. 安装python环境，加载依赖模块
2. 运行`platform-tools`文件夹中的`write_in_path.py`，将adb加入环境变量。此时需注销或重启，以完成注册表写入。可换用手动方式添加。
3. 打开模拟器，运行明日方舟，并进入公开招募界面（如下图）

![公招界面](./fig/公招界面.png)
    
4. 命令行运行`adb devices`，找到模拟器对应的设备编号

![devices](./fig/devices.png)

5. `python auto_hr.py`运行脚本
6. 输入模拟器端口
7. 输入招募次数 

注意：`干员信息.json`为截止到2021年2月20日为止的可公招干员信息，若后续新干员加入公招，此文件也需要更新