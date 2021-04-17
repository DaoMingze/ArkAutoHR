# ArkAuto

基于明日方舟自动公开招募脚本思路，使用adb控制安卓模拟器，实现通过输入控制代替操作的python脚本。使用python3编写。

forked from [shuangluoxss/ArkAutoHR](https://github.com/shuangluoxss/ArkAutoHR)

为其增添一些便利性而非实质功能性的更新

## 更新说明

### 2021-04-17

1. 增加`自动代理点击`脚本和`自动任务奖励领取`脚本。

### 2021-02-23

1. 根据[ngc7331](https://github.com/ngc7331/ArkAutoHR)的向[shuangluoxss/ArkAutoHR](https://github.com/shuangluoxss/ArkAutoHR)的pull request，换用其修改的`auto_hr.py`，修改`README.md`，增加`requirements.txt`（脚本依赖库及其版本限定）

### 2021-02-21

1. 增加`platform-tools`压缩包，提供Android SDK Platform Tools 30.0.5。
2. 增加`write_in_path.py`，自动将`adb.exe`所在文件夹加入环境变量。
3. 在`auto_hr.py`中增添输入设备编号、公招次数代码。
4. 增加一个批处理文件`set_port_to_MuMu.bat`，为MuMu模拟器（1.1.1.4_nochannel_zh-Hans）64位添加7775端口。

## 安装说明

1. 安装python

python[官方下载地址](https://www.python.org/downloads/)

建议使用[python3.6.X](https://www.python.org/downloads/release/python-3613/)

2. 使用pip安装依赖库

命令行输入`pip install -r requirements.txt`安装python库

建议使用清华源`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt`。

如果安装完成后运行时出现`RuntimeError: Cannot find the MXNet library.`报错，并且使用的版本为python3.8则请尝试使用python3.6。[参考](https://github.com/apache/incubator-mxnet/issues/17719)

3. 运行`platform-tools`文件夹中的`write_in_path.py`，将adb加入环境变量。此时需注销或重启，以完成注册表写入。可换用手动方式添加。adb的手动安装请参考[百度经验](https://jingyan.baidu.com/article/22fe7cedf67e353002617f25.html)

## 展示

实现思路与运行效果参考此视频：https://www.bilibili.com/video/BV1jh411k7r9/

## 使用说明

1. 打开模拟器，运行明日方舟，并进入公开招募界面（如下图）

![公招界面](./fig/公招界面.png)
    
2. 命令行运行`adb devices`，找到模拟器对应的设备编号

![devices](./fig/devices.png)

3. 运行脚本

命令行输入`python auto_hr.py`运行脚本，可选参数：

```
  -h, --help            show this help message and exit
  -d Device_Name, --device Device_Name
                        设置ADB设备名称. eg. 127.0.0.1:7555（网易MuMu模拟器）
  -n Num                设置本次需要公招的次数.
  -a, --all             公招直至龙门币、招聘许可或加急许可耗尽. 该选项将会覆盖[-n Num].
  -r, --reset           清除历史记录.
  -f, --force           无视检查，强制运行至指定次数或出错. (此选项可能有助于解决识别出错导致提前终止的问题)
```
4. 如果需要设置默认ADB设备名称或公招次数，请修改auto_hr.py第38行`devicename = '***'`或第50行`default_num = '***'`，如只需临时设置这两个参数可使用-d/--device及-n

注意：`干员信息.json`为截止到2021年2月20日为止的可公招干员信息，若后续新干员加入公招，此文件也需要更新。

## 其他说明

我是在Windows 10系统中使用[miniconda](https://docs.conda.io/en/latest/miniconda.html)，一个anaconda的小型引导版，仅含conda、Python、它们依赖的包，以及少量其他有用的包，如pip、zlib等。配合conda构建的虚拟环境，使用[visual studio code](https://code.visualstudio.com/)来检查、学习、修改、运行。

在cmd中创建python3.6虚拟环境、激活被命名为py3.6的环境、在该环境中安装依赖库

```
conda create -n py3.6 python=3.6
activate py36
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

在vs code中

1. 文件-首选项-设置，搜索终端，打开settings.json，写入

```
    "python.pythonPath": "D:\\conda\\envs\\py3.6\\python.exe",
    "terminal.integrated.env.windows": {
        "python_env": "py3.6",
    },
```

"D:\\conda\\envs\\py3.6\\python.exe"应为你创建的“py3.6”虚拟环境位置。

2. 安装官方python插件。
3. 用vs code打开`auto_hr.py`，右键，选择“在终端中运行python文件”。

