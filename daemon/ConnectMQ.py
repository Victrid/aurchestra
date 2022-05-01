
from datetime import datetime
import sys
import stat
import os
from tabnanny import verbose
from time import time
from pymysql import Date
import traceback
from requests import session

# from keyring import delete_password
# sys.paht.append("..") not working
sys.path.append(os.path.abspath(os.path.join(os.path.join(os.path.abspath(__file__), os.pardir),os.pardir))
)
# for env
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),os.pardir)))


from MQ import MQSender, makepkg_common

from sqlalchemy import Column,String, create_engine,Integer,VARCHAR, CHAR,Date,TEXT 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from env import tableName, connMySQLPara, localTableName, connMyLocalSQLPara, logtableName,connLogPara



#用于与MQ通信和修改数据库
#数据库实现改用 ORM
'''
TODO
sender 地址问题
'''




# 将地址推入队列

def push_path_to_MQ(path):

    # TODO 
    sender = MQSender.MQSender(connection="amqp://user:passwd@somehost/somevh")


    maxerrornumber = 10
    while maxerrornumber:
        maxerrornumber -= 1
        try:
            pkglist = sender.send(path)  #获取到结果直接返回
            return pkglist
        except (makepkg_common.MakepkgTimeoutError
                ):
            if maxerrornumber == 0:
                raise makepkg_common.MakepkgTimeoutError
            continue 

        except makepkg_common.MakepkgRuntimeError:
            if maxerrornumber==0:
                raise makepkg_common.MakepkgRuntimeError
            continue
        


'''
# 用于测试和前端的交互
def push_path_to_MQ(path):
    print(path)

    # 通过修改a来抛出错误
    a = 1
    try:
        b = 1/a
    except Exception:
        raise Exception
    
    return ['aa','bb','cc']
'''




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
    lastupdateTime = Column(Date)

#定义本地的表
class LocalSFMapPKG(Base):

    __tablename__ = localTableName
    #表的结构 id, 软件名，拥有的包，版本

    name = Column(VARCHAR(255),primary_key = True)
    pkgslist = Column(VARCHAR(1000))
    version = Column(Integer)
    compilinglist = Column(VARCHAR(1000)) # 记录刚更新的版本

#定义日志信息表
class LogTable(Base):

    __tablename__ = logtableName

    id = Column(Integer,autoincrement=True ,primary_key=True)
    logtype = Column(VARCHAR(255)) #信息关键词
    loginfo = Column(TEXT) #具体信息字段


#每次修改前端数据库，都加入时间，因为只有成功的才会被显示，所以失败的添加了时间也无所谓
def modifyDatabase(name, state):

    #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
    engine = create_engine(connMySQLPara)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    #这里只是进行修改
    sf = session.query(SFtable).filter_by(name=name).first()
    sf.state = state
    sf.lastupdateTime = datetime.now()
    session.commit()
    session.close()




def deleteFromDatabase(name):

    #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
    engine = create_engine(connMySQLPara)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    #这里只是进行修改
    session.query(SFtable).filter_by(name=name).delete()
    session.commit()
    session.close()


   

def queryLocalDatabase(name):
    pakgelist = None #记录所有的包名


    #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
    engine = create_engine(connMyLocalSQLPara)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    #这里只是进行修改
    sf = session.query(LocalSFMapPKG).filter_by(name=name).first()
    pakgelist = sf.pkgslist.split('&') #分割字符串得到所有的包

    session.close()

    
    return pakgelist


def deleteLocalDatabase(name):

    #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
    engine = create_engine(connMyLocalSQLPara)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    #这里只是进行修改
    session.query(LocalSFMapPKG).filter_by(name=name).delete()
    session.commit()
    session.close()

        

# 只在第一次编译软件时使用，用在connectWeb中，插入获取的list,这个时候两个位置都插入一样。
def insertLocalDatabase(name,pkglist):

    #转化为字符串
    pkgliststr = ""
    for item in pkglist:
        pkgliststr += item
        pkgliststr += '&'
    pkgliststr = pkgliststr[:-1]

    #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
    engine = create_engine(connMyLocalSQLPara)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    # 这里只是进行修改
    newItem = LocalSFMapPKG(name=name,pkgslist=pkgliststr,version=0, compilinglist=pkgliststr)
    session.add(newItem)
    session.commit()
    session.close()



#返回0则表明第一次编译，不可能没有，如果没有则是报错
def CheckSoftwareVersion(name):
    version = -1

    #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
    engine = create_engine(connMyLocalSQLPara)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    #这里只是进行修改
    exist = session.query(LocalSFMapPKG).get(name)

    version = exist.version
    session.close()

        
    
    return version

# 在update模块中只是更新原理的compilinglist字段，表明这个包正在编译
def updatePkgListLocalDatabase(name,pkgslist):

    #转化为字符串
    pkgliststr = ""
    for item in pkgslist:
        pkgliststr += item
        pkgliststr += '&'
    pkgliststr = pkgliststr[:-1]


    #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
    engine = create_engine(connMyLocalSQLPara)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    #这里只是进行修改
    sf = session.query(LocalSFMapPKG).filter_by(name=name).first()
    sf.compilinglist = pkgliststr
    session.commit()
    session.close()



# 在编译结束后对版本进行更新，如果成功，则用complinglist覆盖pkgslist，并修改version为+1 如果失败，则用pkgslist覆盖compilinglist
def updateVersionLocalDatabase(name, state): #state = True 成功，state=false 失败


    #连接，提供“数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字”
    engine = create_engine(connMyLocalSQLPara)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    #这里只是进行修改
    sf = session.query(LocalSFMapPKG).filter_by(name=name).first()
    if state:
        sf.pkgslist = sf.compilinglist
        sf.version = sf.version+1

    else:
        sf.compilinglist = sf.pkgslist

    session.commit()
    session.close()


# 写日志到数据库
def Logger(logkey, loginfo):
    engine = create_engine(connLogPara)
    DBSession = sessionmaker(bind=engine)
    session=DBSession()

    newItem = LogTable(logtype=logkey,loginfo=loginfo)
    session.add(newItem)
    session.commit()
    session.close()





def file_remove_readonly(func, path, execinfo):
    os.chmod(path, stat.S_IWUSR)  # 修改文件权限
    func(path)

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
   


    """ try:
        print(10/0)
    except Exception:
        Logger("testinfo", str(traceback.format_exc())) """

    modifyDatabase('python-web3',6)
