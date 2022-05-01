from pymysql import Connect
from CheckUpdateGit import CheckUpdateGit
from ConnectDocker import getInfo
from ConnectWeb import listener
import threading
import time

   

'''
功能：
用不同线程启动各个模块

'''

def schedule(sleeptime):
   
    


    ###############前端交互模块
    ConnectWeb_Thread = threading.Thread(target=listener)

    ############与docker程序交互模块
    ConnectDocker_Thread = threading.Thread(target=getInfo)


    ###########与远端交互模块
    #参数：轮询时间
    
    sleep_time = sleeptime #轮询检查间隔时间
    CheckUpdateGit_model = CheckUpdateGit(sleep_time)
    CheckUpdateGit_Thread = threading.Thread(target=CheckUpdateGit_model.connect_to_MQ) #这里有问题，对于定时扫描的问题

    print("守护中..........")
    ConnectWeb_Thread.start()
    ConnectDocker_Thread.start()
    CheckUpdateGit_Thread.start()


    ConnectWeb_Thread.join()
    ConnectDocker_Thread.join()
    CheckUpdateGit_Thread.join()



    print("守护结束!")




if __name__ == "__main__":

    sltime = 20
    schedule(sltime)
    