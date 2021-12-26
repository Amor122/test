#coding:utf8
import servicemanager
import win32serviceutil
import win32service
import win32event
import winerror
# import servicemanage
import os,time,sys
from subprocess import Popen, PIPE
import json
import signal
"""
#1.安装服务
python WinPollManager.py install
#2.让服务自动启动
python WinPollManager.py --startup auto install
#3.启动服务
python WinPollManager.py start
 #4.重启服务
python WinPollManager.py restart
#5.停止服务
python WinPollManager.py stop
#6.删除/卸载服务
python WinPollManager.py remove
"""

class Anaservice(win32serviceutil.ServiceFramework):
    _svc_name_ = "ANAservice"  #服务名
    _svc_display_name_ = "ANAservice"   #在windows中显示的名

    _svc_description_ = "Ana service is writen by python"  #描述

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.isAlive=True


    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.isAlive=False


    def SvcDoRun(self):
        while self.isAlive:
            pass
            #do something here

if __name__=='__main__':
    if len(sys.argv) == 1:
        # try:
            evtsrc_dll = os.path.abspath(servicemanager.__file__)
            servicemanager.PrepareToHostSingle(Anaservice)
            servicemanager.Initialize('Anaservice', evtsrc_dll)
            servicemanager.StartServiceCtrlDispatcher()
        # except win32service.error, details:
        #     if details[0] == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
        #         win32serviceutil.usage()
    else:
        win32serviceutil.HandleCommandLine(Anaservice)
# ————————————————
# 版权声明：本文为CSDN博主「虫酋」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/wo446100076/article/details/80973551