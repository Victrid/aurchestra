
import traceback
import git
import os
import shutil
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from env import IPWeb, portWeb,pkgs_path

from ConnectMQ import push_path_to_MQ, deleteFromDatabase, queryLocalDatabase, deleteLocalDatabase,modifyDatabase
from loggerWrite import myLogger

'''
功能：
1、监听前端信息
2、通过信息下载新的软件包并送入编译，同时修改数据库状态
3、通过信息删除软件

TODO
1.服务器地址 和 端口 问题
2.错误处理问题, networkerror
3.删除包问题
'''


#设置文件夹路径为全局变量

weblogger = myLogger('web').getmyLogger()


class myHandler(BaseHTTPRequestHandler):

  
    def do_GET(self):
        pass


    def do_POST(self):

        #print(self.headers)
        #print(self.command)

        req_datas = self.rfile.read(int(self.headers['content-length']))
        self.send_header('Content-type','text/html')
        #self.send_header("Access-Control-Allow-Origin", "http://"+IPWeb+":"+str(portWeb))
        self.send_header("*", "http://"+IPWeb+":"+str(portWeb))
        self.send_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
       

        res1 = req_datas.decode('utf-8') #解码
        res = json.loads(res1) #变成字典
        
        if list(res.keys()) != ['name','address','state']:
            self.send_response(503,"format error")
        else:
            
            if res['state'] == 'wait': #需要下载的软件
                self.send_response(201)
                state = 2
                try: #下载错误
                    new_path = self.Add_software(res['name'],res['address'])
                except Exception:
                    state = 6
                    weblogger.error("%s" %traceback.format_exc())
                else: #下载成功
                    try:
                        
                        push_path_to_MQ(new_path) #放入消息队列
                    except Exception:
                        weblogger.error("%s" %traceback.format_exc())
                        state = 6
                        #对刚才下载成功的目录进行删除
                        shutil.rmtree(new_path)
                    
                try: #放入数据库，这里进行人为处理
                    modifyDatabase(res['name'],state)
                except Exception:
                    weblogger.error("%s" %traceback.format_exc())

                

            elif res['state'] == 'delete': #需要删除的软件
                self.send_response(201)

                #删除本地目录
                try:
                    localpath = os.path.join(pkgs_path,res['name'])
                    shutil.rmtree(localpath)
                except Exception:
                    weblogger.error("%s" %traceback.format_exc())
                
                else:
                    #删除远程仓库
                    try:
                        self.Delete_compiled_Packge(res['name'])
                    except Exception:
                        weblogger.error("%s" %traceback.format_exc())
                    else: 
                        #删除本地数据库
                        try:
                            deleteLocalDatabase(res['name'])
                        except Exception:
                            weblogger.error("%s" %traceback.format_exc())     

                        #删除前端数据库条目
                        try:
                            deleteFromDatabase(res['name'])
                        except Exception:
                            weblogger.error("%s" %traceback.format_exc())

               
                
            else:
                 self.send_response(503,"state error")  
        self.end_headers()



    def do_OPTIONS(self):
        self.send_response(201,"ok")
        self.send_header('Content-type','application/json')
        self.send_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        #self.send_header('Access-Control-Allow-Origin', "http://"+IPWeb+":"+str(portWeb))
        self.send_header('*', "http://"+IPWeb+":"+str(portWeb))
        self.end_headers()


    def Add_software(self,name,address): #处理增加一个软件的情况，传入参数为包名，一个git地址和对应的存放包的上级文件夹路径

        #下载失败
        try:
            newrepo = git.Repo.clone_from(url=address,to_path=os.path.join(pkgs_path,name)) #下载
        except Exception:
            raise Exception

        new_path = os.path.join(pkgs_path,name) #这里是存放包的位置加上包名就是包的路径


        return new_path #交给上一级程序将这个文件地址给消息队列程序


        #y用于删除本地的软件对应的仓库和软件库
        #删除参数为对应的包的名字
    def Delete_compiled_Packge(self,name):
        
        #从本地数据库中查找出所有的需要的删除的包名

        try:
            pkgslist = queryLocalDatabase(name)
        except Exception:
            raise Exception
        else:
            #删除远程仓库
            #TODO 
            pass
        

 





       
    
    



def listener():
        
    #开启https服务器监听获取得到name,address
    host = (IPWeb,portWeb)
    server = HTTPServer(host,myHandler)
    print("starting listening...... at %s:%s"%host)
    server.serve_forever()
    









if __name__ == "__main__":
    listener()
    
