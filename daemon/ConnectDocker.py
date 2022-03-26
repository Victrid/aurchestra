from ConnectMQ import modifyDatabase
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from env import IPDocker, portDocker

'''
功能：
    1、监听消息队列，获取编译好的软件更新信息
    2、修改数据库中的状态信息。

'''


class myHandler(BaseHTTPRequestHandler):

  
    def do_GET(self):
        pass


    def do_POST(self):

        print(self.headers)
        print(self.command)

        req_datas = self.rfile.read(int(self.headers['content-length']))

        #print("----------接收数据---------")
        #这里接收的数据 name&state

        res1 = req_datas.decode('utf-8') #解码
        res = json.loads(res1) #变成字典
        

        modifyDatabase(res['name'],res['state'])
            





def getInfo():
    #开启https服务器监听获取得到name,address
    host = (IPDocker,portDocker) #和前端用不同的端口
    server = HTTPServer(host,myHandler)
    print("starting listening...... at %s:%s"%host)
    server.serve_forever()
        







