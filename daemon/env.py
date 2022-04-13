import os

#本地软件仓库包
pkgs_path = os.getenv('PACKAGE_PATH','/home/tpljqj/testDaemon/daemon/softwareHub')


#数据库连接需要的参数
#前端数据库表名
tableName = os.getenv('TABLE_NAME','softwareInfo') 
#连接数据库需要的参数， 数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字
connMySQLPara = os.getenv('CONNECT_MYSQL_PARAMETER','mariadb+pymysql://root:tpljqj@localhost:3306/software') 

#本地映射数据库表名
localTableName = os.getenv('LOCAL_TABLE_NAME','softMapPkgs')
connMyLocalSQLPara = os.getenv('CONNECT_LOCAL_MYSQL_PARAMETER','mariadb+pymysql://root:tpljqj@localhost:3306/software')
 

#http server需要的参数
IPWeb = os.getenv('IP_for_web','localhost')
portWeb = 8888

IPDocker = os.getenv('TP_for_docker','localhost')
portDocker = 8889


#logger配置文件
logConfigPath = os.getenv('LogConfigPath','/home/tpljqj/testDaemon/daemon/logging/logging.conf')

