
import git
import pymysql
import time
import os
import shutil

'''
功能：
1、监听前端信息
2、通过信息下载新的软件包并送入编译，同时修改数据库状态
3、通过信息删除软件

TODO
和前端交互部分，如何获取信息
如何删除软件库信息
如何将软件信息送入消息队列

'''


    
    
class ConnectMysql(object):
    def __init__(self,pkgs_path, sql_parameters):
        self.pkgs_path = pkgs_path


        #提供连接数据库的参数：服务器IP，用户名，密码，要连接的数据库，端口号，以及要更新的表名，软件字段名和状态名
        self.sql_host = sql_parameters[0]
        self.sql_user = sql_parameters[1] 
        self.sql_password = sql_parameters[2]
        self.sql_db = sql_parameters[3]
        self.sql_port = sql_parameters[4]
        self.sql_table = sql_parameters[5]
        self.sql_table_sfname = sql_parameters[6]
        self.sql_table_stname = sql_parameters[7]



    #监听状态得到来自前端的消息进行处理
    def listener(self):

        #TODO
        #监听获取得到name,address
        
        name = "packge"
        address = "git.com"

        flag = True #true表示添加，false表示删除
        if flag:
            new_path = self.Add_software(name,address,self.pkgs_path)
            
            #将得到的地址放入另一个接口，
            #TODO
            
            #并改下数据库状态为正在编译
            state = "正在编译"
            self.Modify_database(name,state)


        else:
            self.Delete_software(name,self.pkgs_path)


    def Add_software(self,name,address,pkg_path): #处理增加一个软件的情况，传入参数为包名，一个git地址和对应的存放包的上级文件夹路径
        newrepo = git.Repo.clone_from(url=address,to_path=pkg_path) #下载
        
        new_path = os.path.join(pkg_path,name) #这里是存放包的位置加上包名就是包的路径


        return new_path #交给上一级程序将这个文件地址给消息队列程序


    #y用于删除本地的软件对应的仓库和软件库
    #删除参数为对应的包的名字
    def Delete_software(self,name,pkg_path):
        
        
        #由于包名和packages_path之和就是这个包的路径
        path = os.path.join(pkg_path,name)

        #删除对应的本地软件目录
        shutil.rmtree(path) 


        #删除远程仓库
        #TODO 


        return True #告诉上一级程序已经删除完毕  

    #用于修改数据库中的状态
    def Modify_database(self,name,state):
        db = pymysql.connect(host = self.sql_host,user = self.sql_user ,password=self.sql_password,database=self.sql_db)
        #创建一个cursor对象
        cursor = db.cursor()

        try:
            modif = "UPDATE %s SET %s = '%s'  WHERE %s= '%s'" %(self.sql_table, self.sql_table_stname, state, self.sql_table_sfname, name)
            cursor.execute(modif) #执行
            db.commit()    #对数据库的操作和修改要提交到数据库
        except:
            db.rollback() #出错回滚

        db.close()





if __name__ == "__main__":
    packages_path = 'E:\\大三下\\软件工程\\大作业\\SEcode\\packages' #所有软件包的上级目录
    
