
import git
import os
import shutil
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from env import IPWeb, portWeb,pkgs_path


from ConnectMQ import push_path_to_MQ


'''
功能：
1、监听前端信息
2、通过信息下载新的软件包并送入编译，同时修改数据库状态
3、通过信息删除软件

TODO
1.服务器地址 和 端口 问题
2.错误处理问题
3.删除包问题
'''


#设置文件夹路径为全局变量




class myHandler(BaseHTTPRequestHandler):

  
    def do_GET(self):
        pass


    def do_POST(self):

        print(self.headers)
        print(self.command)

        req_datas = self.rfile.read(int(self.headers['content-length']))

        #print("----------接收数据---------")

        res1 = req_datas.decode('utf-8') #解码
        res = json.loads(res1) #变成字典
        
        #infolist = (list(res.values())[0]).split('&') #分割

        if res['state'] == 'wait': #需要下载的软件
            new_path = self.Add_software(res['name'],res['address'])
            push_path_to_MQ(new_path)

        elif res['state'] == 'delete': #需要删除的软件
            self.Delete_software(res['name'])




    def Add_software(self,name,address): #处理增加一个软件的情况，传入参数为包名，一个git地址和对应的存放包的上级文件夹路径
        newrepo = git.Repo.clone_from(url=address,to_path=pkgs_path) #下载
        
        new_path = os.path.join(pkgs_path,name) #这里是存放包的位置加上包名就是包的路径


        return new_path #交给上一级程序将这个文件地址给消息队列程序


        #y用于删除本地的软件对应的仓库和软件库
        #删除参数为对应的包的名字
    def Delete_software(self,name):
        
        
        #由于包名和packages_path之和就是这个包的路径
        path = os.path.join(pkgs_path,name)

        #删除对应的本地软件目录
        shutil.rmtree(path) 


        #删除远程仓库
        #TODO 


       
    
    



def listener():
        
    #开启https服务器监听获取得到name,address
    host = (IPWeb,portWeb)
    server = HTTPServer(host,myHandler)
    print("starting listening...... at %s:%s"%host)
    server.serve_forever()
    









if __name__ == "__main__":
    packages_path = 'E:\\大三下\\软件工程\\大作业\\SEcode\\packages' #所有软件包的上级目录
    
