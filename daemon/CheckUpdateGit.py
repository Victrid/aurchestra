from cgi import test
from sqlite3 import SQLITE_DROP_TEMP_TABLE
from time import sleep, time
from unittest.mock import patch
from xml.dom.pulldom import default_bufsize
import git 
import time
import os

'''
TODO

待完成部分：
和消息队列程序交互部分

'''


class CheckUpdateGit(object):
    def __init__(self,pkgs_path,sleep_time):
        self.pkgs_path = pkgs_path #所有包的文件目录
        self.sleep_time = sleep_time  #定义检查周期时间间隔

    def connect_to_MQ(self):  #用于定时调用check_warehouse_update检查更新，并把结果给到消息队列程序

        while True:
            path_list = self.check_warehouse_update()

            #TODO
            #如何传递path_list

            time.sleep(self.sleep_time)

    
            

    def check_warehouse_update(self): #检查本地软件更新情况，返回有更新的软件目录
        HousePathes = self.find_dirs(self.pkgs_path) #得到所有软件包地址
        paths = []                               #本地更新的文件目录地址

        for housepath in HousePathes:  #轮询所有的仓库地址，检查更新
            newrepo = git.Repo(path=housepath)  #这样就可以和当前这个分支建立联系
            gitt = newrepo.git

            str = gitt.pull() #得到pull之后的信息，为一个字符串

            lines = str.split('\n') #将字符串按行分割，放入line的list中

            if len(lines)==1: #无更新
                continue
            else: #有更新，即这个软件包更新。直接记录下这个路径
                paths.append(housepath) #只考虑一个包对应一个本地仓库的情况
                
        paths = list(set(paths)) #去重，因为一个文件夹下多个文件更新的情况

        return paths

    #返回path下的所有的子文件目录名
    def find_dirs(self):

        dirs = []
        for dir in os.scandir(self.pkgs_path):
            if dir.is_dir():
                dirs.append(dir.path)


        return dirs
        



          

if __name__ == "__main__":
    packages_path = 'E:\\大三下\\软件工程\\大作业\\SEcode\\packages' #所有软件包的上级目录

    testMode = CheckUpdateGit(packages_path,10)
    testMode.connect_to_MQ()


