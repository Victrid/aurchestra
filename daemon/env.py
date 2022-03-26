import os

#本地软件仓库包
pkgs_path = os.getenv('PACKAGE_PATH','E:\\大三下\\软件工程\\大作业\\SEcode\\packages\\aa.txt')


#数据库连接需要的参数
#表名
tableName = os.getenv('TABLE_NAME','softwareInfo') 
#连接数据库需要的参数， 数据库类型、数据库驱动（就是用的什么库）、用户名、密码、ip、端口、数据库名字
connMySQLPara = os.getenv('CONNECT_MYSQL_PARAMETER','mysql+pymysql://tp:tpljqj@localhost:3306/dbname') 


#http server需要的参数
IPWeb = os.getenv('IP_for_web','localhost')
portWeb = 8888

IPDocker = os.getenv('TP_for_docker','localhost')
portDocker = 8889

