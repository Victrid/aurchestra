import traceback
from ConnectMQ import modifyDatabase, updateVersionLocalDatabase, CheckSoftwareVersion, deleteLocalDatabase, file_remove_readonly, Logger
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from env import IPDocker, portDocker,pkgs_path,softwareHubLock
from loggerWrite import myLogger
import os
import shutil
import git

'''
功能：
    1、监听消息队列，获取编译好的软件更新信息
    2、修改数据库中的状态信息。

'''
#dockerlogger = myLogger('docker1').getmyLogger()

# 用于处理只读文件无法删除的问题




class myHandler(BaseHTTPRequestHandler):

  
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()


    def do_POST(self):

        req_datas = self.rfile.read(int(self.headers['content-length']))
        self.send_response(200, "OK")
        self.send_header('Content-Type','text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        self.wfile.write(b"OK")
        self.wfile.close()
        

        res1 = req_datas.decode('utf-8') #解码
        print("get the information from docker compiled ", res1)
        res = json.loads(res1) #变成字典

        if list(res.keys()) != ['name','state','info']:
            print("format error")
        else:                      
            if res['state'] == 3 or res['state'] == 6: # 编译完状态
                
                #写入日志
                loginfo = {3:" compiling success", 6:" compiling fail"}
                Logger(res['name'], res['info'])
                

                # 先查本地仓库拿到version
                softversion = CheckSoftwareVersion(res['name'])

                if softversion==0: # 软件首次加入
                    # 失败，则删除本地文件，同时删除对应的条目
                    if res['state'] == 6: 
                        localpath = os.path.join(pkgs_path,res['name'])
                        with softwareHubLock:
                            shutil.rmtree(localpath,onerror=file_remove_readonly)
                        try:
                            deleteLocalDatabase(res['name'])
                        except Exception:
                            #dockerlogger.error("%s" %traceback.format_exc())
                            Logger(res['name'], str(traceback.format_exc()))


                    # 成功，则需要更新本地数据库中的版本为1
                    if res['state'] == 3: 
                        try:
                            updateVersionLocalDatabase(res['name'], True)
                        except Exception:
                            #dockerlogger.error("%s" %traceback.format_exc())
                            Logger(res['name'], str(traceback.format_exc()))

                    try:
                        modifyDatabase(res['name'],res['state'])
                        print("modify the state of ", res['name'], " to ", res['state'])
                    except Exception:
                        Logger(res['name'], str(traceback.format_exc()))


                else: #是对旧版本的更新

                    # 失败则用旧版本覆盖新版本的数据库，并将本地的仓库回退，以便下次能检查更新
                    if res['state'] == 6:
                        try:
                            updateVersionLocalDatabase(res['name'],False) #失败
                        except Exception:
                            Logger(res['name'], str(traceback.format_exc()))

                        #回退本地仓库到上一个版本
                        localpath = os.path.join(pkgs_path, res['name'])
                        with softwareHubLock:
                            newrepo = git.Repo(path=localpath)  # 这样就可以和当前这个分支建立联系
                            gitt = newrepo.git
                            gitt.reset('--hard', 'HEAD@{1}')


                    if res['state'] == 3:
                        try:
                            updateVersionLocalDatabase(res['name'], True)
                        except Exception:
                            Logger(res['name'], str(traceback.format_exc()))

                        #考虑到更新时间，所以对旧版本更新成功也需要写一下更新时间
                        try:
                            modifyDatabase(res['name'],res['state'])
                        except Exception:
                            Logger(res['name'], str(traceback.format_exc()))

                
            else:
                print("state error")  
        
        



    def do_OPTIONS(self):
        self.send_response(201,"ok")
        self.send_header('Content-type','application/json')
        self.send_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        self.send_header('Access-Control-Allow-Origin', "*")
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
    #import stat



    #shutil.rmtree("softwareHub/python-web3", onerror=file_remove_readonly)




