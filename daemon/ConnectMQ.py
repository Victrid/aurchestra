
from sre_constants import SUCCESS
import sys
import pika
sys.path.append("..")
from MQ import mq
import os
import pymysql
from sqlalchemy import Column,String, create_engine,Integer,VARCHAR, CHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from env import tableName, connMySQLPara

#用于与MQ通信和修改数据库

#数据库实现改用 ORM
'''
TODO
sender 地址问题
'''

def push_path_to_MQ(path):

    #TODO 
    sender = mq.MQSender(connection="amqp://user:passwd@somehost/somevh")

    #从path中解析出软件的名字
    name = os.path.basename(path)
    
    state = "fail"
    #两种错误对于的数量
    maxerrornumber = 10
    success = False
    while maxerrornumber and not success:
        maxerrornumber -=1
        try:
            sender.send(path) 

        except (mq.MakepkgConnectionError,
                mq.UploadError,
                pika.AMQPError,
                pika.AMQPConnectionError
                ):
            
            continue  
        except:
            break
        state = "compiling"  
        success = True

    modifyDatabase(name,state)       
      


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
    name = Column(VARCHAR(20))
    address = Column(VARCHAR(30))
    state = Column(VARCHAR(20))



def modifyDatabase(name, state):


    #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
    engine = create_engine(connMySQLPara)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    #这里只是进行修改
    sf = session.query(SFtable).filter_by(name=name).first()
    sf.state = state
    count = 0
    while True:
        try:
            session.commit()
            break
        except Exception:
            if count>10:
                break
            count+=1

    session.close()

   

