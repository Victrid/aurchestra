import os
from threading import Lock

pkgs_pathtemp = os.path.abspath(os.path.join(os.path.abspath(__file__),os.pardir,'softwareHub'))

folder = os.path.exists(pkgs_pathtemp)
if not folder:
    os.makedirs(pkgs_pathtemp)


logconfpath = os.path.abspath(os.path.join(os.path.abspath(__file__),os.pardir,'logging','logging.conf'))

#本地软件仓库包
pkgs_path = os.getenv('PACKAGE_PATH',pkgs_pathtemp)


#数据库连接需要的参数
#前端数据库表名
tableName = os.getenv('TABLE_NAME','softwareinfo') 
#连接数据库需要的参数， 数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字
connMySQLPara = os.getenv('CONNECT_MYSQL_PARAMETER','mysql+pymysql://tp:tpljqj@localhost:3306/software')

#本地映射数据库表名
localTableName = os.getenv('LOCAL_TABLE_NAME','softmappkgs')
connMyLocalSQLPara = os.getenv('CONNECT_LOCAL_MYSQL_PARAMETER','mysql+pymysql://tp:tpljqj@localhost:3306/software')
 

#连接日志信息数据库
logtableName = os.getenv('Log_table_name','loginfo')
connLogPara = os.getenv('CONNECT_LOG_PARAMETER','mysql+pymysql://tp:tpljqj@localhost:3306/software')

#http server需要的参数
IPWeb = '0.0.0.0'
portWeb = 8880

IPDocker = '0.0.0.0'
portDocker = 8881


#MQ连接参数
ConnMQPara = os.getenv('Address_for_MQ','amqp://user:passwd@somehost/somevh')


#logger配置文件
logConfigPath = os.getenv('LogConfigPath',logconfpath)

# 检查更新时间间隔
updateInterval = os.getenv('UPDATA_Interval', '30')

softwareHubLock = Lock()

