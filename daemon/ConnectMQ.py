import logging
import sys

import os
from tabnanny import verbose

from keyring import delete_password
#sys.paht.append("..") not working
sys.path.append(os.path.abspath(os.path.join(os.path.join(os.path.abspath(__file__), os.pardir),os.pardir))
)
#for env 
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),os.pardir)))
from MQ import mq

from sqlalchemy import Column,String, create_engine,Integer,VARCHAR, CHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from env import tableName, connMySQLPara, localTableName, connMyLocalSQLPara



#用于与MQ通信和修改数据库
#数据库实现改用 ORM
'''
TODO
sender 地址问题
'''




#将地址推入队列
def push_path_to_MQ(path):

    #TODO 
    sender = mq.MQSender(connection="amqp://user:passwd@somehost/somevh")


    maxerrornumber = 10
    success = False
    while maxerrornumber and not success:
        maxerrornumber -=1
        try:
            sender.send(path) 

        except (mq.MakepkgConnectionError,
                #mq.UploadError,
                #pika.AMQPError, #no this attribute error
                #pika.AMQPConnectionError
                ):
            if maxerrornumber==0:
                raise mq.MakepkgConnectionError               
            continue 

        except mq.UploadError:
            if maxerrornumber==0:
                raise mq.UploadError
            continue

        except Exception:
            raise Exception
        
            
            
        #state = 2  
        success = True

    #modifyDatabase(name,state)       
    


# 修改数据库状态函数

#定义表的对象
#创建基类

Base = declarative_base()

#定义表的对象
class SFtable(Base):

    #表的名字
    __tablename__ = tableName

    #表的结构: id, 软件名，地址，状态
    #id = Column(Integer,primary_key = True)
    name = Column(VARCHAR(255),primary_key = True)
    address = Column(VARCHAR(255))
    state = Column(Integer)
    email = Column(VARCHAR(255))

#定义本地的表
class LocalSFMapPKG(Base):

    __tablename__ = localTableName
    #表的结构 id, 软件名，拥有的包，版本

    name = Column(VARCHAR(255),primary_key = True)
    pkgslist = Column(VARCHAR(1000))
    version = Column(Integer)


def modifyDatabase(name, state):


    count = 0
    while True:
        try:            
            #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
            engine = create_engine(connMySQLPara)
            # 创建DBSession类型:
            DBSession = sessionmaker(bind=engine)

            session = DBSession()

            #这里只是进行修改
            sf = session.query(SFtable).filter_by(name=name).first()
            sf.state = state
            session.commit()
            session.close()
            break
        except Exception:
            if count>10:
                raise Exception
            count+=1



def deleteFromDatabase(name):
    count = 0
    while True:
        try:            
            #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
            engine = create_engine(connMySQLPara)
            # 创建DBSession类型:
            DBSession = sessionmaker(bind=engine)

            session = DBSession()

            #这里只是进行修改
            session.query(SFtable).filter_by(name=name).delete()            
            session.commit()
            session.close()
            break
        except Exception:
            if count>10:
                raise Exception
            count+=1

   

def queryLocalDatabase(name):
    pakgelist = None #记录所有的包名

    count = 0
    while True:
        try:            
            #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
            engine = create_engine(connMyLocalSQLPara)
            # 创建DBSession类型:
            DBSession = sessionmaker(bind=engine)

            session = DBSession()

            #这里只是进行修改
            sf = session.query(LocalSFMapPKG).filter_by(name=name).first()           
            pakgelist = sf.pkgslist.split('&') #分割字符串得到所有的包

            session.close()
            break
        except Exception:
            if count>10:
                raise Exception
            count+=1
        
    
    return pakgelist


def deleteLocalDatabase(name):
    count = 0
    while True:
        try:            
            #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
            engine = create_engine(connMyLocalSQLPara)
            # 创建DBSession类型:
            DBSession = sessionmaker(bind=engine)

            session = DBSession()

            #这里只是进行修改
            session.query(LocalSFMapPKG).filter_by(name=name).delete()
            session.commit()
            session.close()
            break
        except Exception:
            if count>10:
                raise Exception
            count+=1
        

#只在第一次编译软件时使用
def insertLocalDatabase(name,pkglist):

    #转化为字符串
    pkgliststr = ""
    for item in pkglist:
        pkgliststr += item
        pkgliststr += '&'
    pkgliststr = pkgliststr[:-1]
    count = 0
    while True:
        try:            
            #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
            engine = create_engine(connMyLocalSQLPara)
            # 创建DBSession类型:
            DBSession = sessionmaker(bind=engine)

            session = DBSession()

            #这里只是进行修改
            newItem = LocalSFMapPKG(name=name,pkgslist=pkgliststr,version=1)
            session.add(newItem)
            session.commit()
            session.close()
            break
        except Exception:
            if count>10:
                raise Exception
            count+=1



#返回0则表明没有
def IsNewSoft(name):  
    version = 0    
    count = 0
    while True:
        try:            
            #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
            engine = create_engine(connMyLocalSQLPara)
            # 创建DBSession类型:
            DBSession = sessionmaker(bind=engine)

            session = DBSession()

            #这里只是进行修改
            exist = session.query(LocalSFMapPKG).get(name)
            if exist != None:
                version = exist.version          
            session.close()
            break
        except Exception:
            if count>10:
                raise Exception
            count+=1
        
    
    return version


def updateLocalDatabase(name,pkgslist,version):

    #转化为字符串
    pkgliststr = ""
    for item in pkgslist:
        pkgliststr += item
        pkgliststr += '&'
    pkgliststr = pkgliststr[:-1]

    count = 0
    while True:
        try:            
            #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
            engine = create_engine(connMyLocalSQLPara)
            # 创建DBSession类型:
            DBSession = sessionmaker(bind=engine)

            session = DBSession()

            #这里只是进行修改
            sf = session.query(LocalSFMapPKG).filter_by(name=name).first()
            sf.pkgslist = pkgliststr
            sf.version = version
            session.commit()
            session.close()
            break
        except Exception:
            if count>10:
                raise Exception
            count+=1



if __name__ == '__main__':
    #modifydatabase
    #modifyDatabase('test', 4)

    # deleteFromdatabase
    #deleteFromDatabase('test')

    #version = IsNewSoft('test')
    #print(version)

    #insertLocalDatabase('test3',['dddd','fff','rrrr'])

    #listt = queryLocalDatabase('test')
    #print(listt)

    #updateLocalDatabase('test',['555','3333','dfdgi'],2)

    #deleteLocalDatabase('test3')
    try:
        push_path_to_MQ("ffffffffffff")
    except Exception:
        print('error')
