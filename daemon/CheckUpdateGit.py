from asyncio.log import logger
from sqlite3 import SQLITE_DROP_TEMP_TABLE
import git 
import time
import os
from ConnectMQ import push_path_to_MQ,modifyDatabase
from env import pkgs_path
from loggerWrite import myLogger
import traceback

'''
TODO
定时检查的时间问题

'''

gitupdatelogger = myLogger('gitupdate').getmyLogger()

class CheckUpdateGit(object):
    def __init__(self,sleep_time):
        self.sleep_time = sleep_time  #定义检查周期时间间隔



    def connect_to_MQ(self):  #用于定时调用check_warehouse_update检查更新，并把结果给到消息队列程序

        while True:

            try:               
                path_list = self.check_warehouse_update()
            except Exception:
                gitupdatelogger.error("%s" %traceback.format_exc())
            
            else:                
                for itempath in path_list:

                    #state = 2 #默认成功
                    try:
                        push_path_to_MQ(itempath)
                    except Exception:
                        gitupdatelogger.error("%s" %traceback.format_exc())


                        #state = 6
                    # don't modify the database for updating, I just do it for my self
                    '''
                    try:
                        modifyDatabase(os.path.basename(itempath),state)
                    except Exception:
                        gitupdatelogger.error("%s" %traceback.format_exc())
                    '''
            
                 
            time.sleep(self.sleep_time)

    
            

    def check_warehouse_update(self): #检查本地软件更新情况，返回有更新的软件目录
        HousePathes = self.find_dirs() #得到所有软件包地址
        paths = []                               #本地更新的文件目录地址

        for housepath in HousePathes:  #轮询所有的仓库地址，检查更新

            #网络错误
            try:
                newrepo = git.Repo(path=housepath)  #这样就可以和当前这个分支建立联系
                gitt = newrepo.git

                str = gitt.pull() #得到pull之后的信息，为一个字符串

                lines = str.split('\n') #将字符串按行分割，放入line的list中

                if len(lines)==1: #无更新
                    continue
                else: #有更新，即这个软件包更新。直接记录下这个路径
                    paths.append(housepath) #只考虑一个包对应一个本地仓库的情况
            except Exception:
                raise Exception
                
        paths = list(set(paths)) #去重，因为一个文件夹下多个文件更新的情况

        return paths

    #返回path下的所有的子文件目录名
    def find_dirs(self):

        dirs = []
        for dir in os.scandir(pkgs_path):
            if dir.is_dir():
                dirs.append(dir.path)


        return dirs



        



          

if __name__ == "__main__":
    #packages_path = 'E:\\大三下\\软件工程\\大作业\\SEcode\\packages' #所有软件包的上级目录

    testMode = CheckUpdateGit(20)
    testMode.connect_to_MQ()


