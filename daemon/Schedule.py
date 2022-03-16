from pymysql import Connect
from CheckUpdateGit import CheckUpdateGit
from ConnectDocker import ConnectDocker
from ConnectMysql import ConnectMysql
import threading
import time

   

'''
功能：
用不同线程启动各个模块
'''

def schedule():
    packages_path = 'E:\\大三下\\软件工程\\大作业\\守护服务\\packages' #所有软件包的上级目录，即本地仓库目录

    
    #提供连接RabbitMQ服务器的用户名，密码，IP，port 和 要使用的队列名
    #提供连接数据库的参数：服务器IP，用户名，密码，要连接的数据库，端口号，以及要更新的表名，软件字段名和状态名
    MQ_parameters = [] #5个参数的字符串
    SQL_parameters = [] #8个参数的字符串

    ###############前端交互模块
    #参数：1、本地仓库目录 2、连接数据库参数
    
    ConnectMysql_model = ConnectMysql(packages_path)
    ConnectMysql_Thread = threading.Thread(target=ConnectMysql_model.listener)


    ############与docker程序交互模块
    #参数：1、连接消息队列的参数，2、连接数据库的参数
    
    ConnectDocker_model = ConnectDocker(MQ_parameters=MQ_parameters, sql_parameters=SQL_parameters)
    ConnectDocker_Thread = threading.Thread(target=ConnectDocker_model.getInfo)


    ###########与远端交互模块
    #参数：仓库目录，轮询时间
    
    sleep_time = 10 #轮询检查间隔时间
    CheckUpdateGit_model = CheckUpdateGit(packages_path,sleep_time)
    CheckUpdateGit_Thread = threading.Thread(target=CheckUpdateGit_model.connect_to_MQ) #这里有问题，对于定时扫描的问题




    ConnectMysql_Thread.start()
    ConnectDocker_Thread.start()
    CheckUpdateGit_Thread.start()

    print("守护中..........")
    ConnectMysql_Thread.join()
    ConnectDocker_Thread.join()
    CheckUpdateGit_Thread.join()



    print("守护结束!")




if __name__ == "__main__":
    schedule()
    