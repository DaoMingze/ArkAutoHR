@echo off
title 为MuMu模拟器设定端口
echo 为MuMu模拟器设定端口
echo.
echo 按Enter键开始
pause >nul
C:
cd Program Files\MuMu\emulator\nemu\vmonitor\bin
adb connect 127.0.0.1:7555
echo 完成,请按任意键退出
pause >nul
exit
:end
pause >nul