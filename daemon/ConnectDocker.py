import traceback
from ConnectMQ import modifyDatabase, updateLocalDatabase, IsNewSoft, insertLocalDatabase
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from env import IPDocker, portDocker,pkgs_path
from loggerWrite import myLogger
import os
import shutil
'''
功能：
    1、监听消息队列，获取编译好的软件更新信息
    2、修改数据库中的状态信息。

'''
dockerlogger = myLogger('docker').getmyLogger()

class myHandler(BaseHTTPRequestHandler):

  
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()


    def do_POST(self):

        #print(self.headers)
        #print(self.command)

        req_datas = self.rfile.read(int(self.headers['content-length']))
        self.send_header('Content-type','text/html')
        self.send_header("Access-Control-Allow-Origin", "http://localhost:8998")
        #self.send_header("*", "http://"+IPDocker+":"+str(portDocker))
        self.send_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")

        self.send_response(201) 
        #print("----------接收数据---------")
        #这里接收的数据 name state
        self.end_headers()


        res1 = req_datas.decode('utf-8') #解码
        res = json.loads(res1) #变成字典

        if list(res.keys()) != ['name','pkgslist','state']:
            print("format error")
        else:                      
            if res['state'] == 3 or res['state'] == 6: #编译完状态
                

                #先查本地仓库拿到version
                softversion = IsNewSoft(res['name'])

                if softversion==0: #软件首次加入
                    #失败，则删除本地文件，本地数据库中没有对于的条目
                    if res['state'] == 6: 
                        localpath = os.path.join(pkgs_path,res['name'])
                        shutil.rmtree(localpath)

                    #成功，则需要在本地数据库中加入该条目
                    if res['state'] == 3: 
                        try:
                            insertLocalDatabase(res['name'],res['pkgslist'])
                        except Exception:
                            dockerlogger.error("%s" %traceback.format_exc())

                    try:
                        modifyDatabase(res['name'],res['state'])
                    except Exception:
                        dockerlogger.error("%s" %traceback.format_exc())

                else: #是对旧版本的更新

                    #失败则什么都不做
                    #成功则需要更新数据库
                    if res['state'] == 3:
                        try:
                            updateLocalDatabase(res['name'],res['pkgslist'], softversion+1)
                        except Exception:
                            dockerlogger.error("%s" %traceback.format_exc())              
                
            else:
                print("state error")  
        
        



    def do_OPTIONS(self):
        self.send_response(201,"ok")
        self.send_header('Content-type','application/json')
        self.send_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        self.send_header('Access-Control-Allow-Origin', "http://localhost:8998")
        #self.send_header('*', "http://"+IPDocker+":"+str(portDocker))
        self.end_headers()
            





def getInfo():
    #开启https服务器监听获取得到name,address
    host = (IPDocker,portDocker) #和前端用不同的端口
    server = HTTPServer(host,myHandler)
    print("starting listening...... at %s:%s"%host)
    server.serve_forever()
        


if __name__ == "__main__":
    getInfo()




