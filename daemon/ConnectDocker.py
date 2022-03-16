from re import S
import pika
import pymysql
'''
功能：
    1、监听消息队列，获取编译好的软件更新信息
    2、修改数据库中的状态信息。
TODO
和消息队列交互获得的状态信息格式

'''

class ConnectDocker(object):

   
    def __init__(self,MQ_parameters, sql_parameters):

        #提供连接RabbitMQ服务器的用户名，密码，IP，port 和 要使用的队列名
        self.MQ_username = MQ_parameters[0]
        self.MQ_userpassword = MQ_parameters[1]
        self.MQ_ip = MQ_parameters[2]
        self.MQ_port = MQ_parameters[3]
        self.co_queue = MQ_parameters[4]

        #提供连接数据库的参数：服务器IP，用户名，密码，要连接的数据库，端口号，以及要更新的表名，软件字段名和状态名
        self.sql_host = sql_parameters[0]
        self.sql_user = sql_parameters[1] 
        self.sql_password = sql_parameters[2]
        self.sql_db = sql_parameters[3]
        self.sql_port = sql_parameters[4]
        self.sql_table = sql_parameters[5]
        self.sql_table_sfname = sql_parameters[6]
        self.sql_table_stname = sql_parameters[7]


    def getInfo(self):
        #1. 连接RabbitMQ
        credentials = pika.PlainCredentials(self.MQ_username,self.MQ_userpassword)
        connect = pika.BlockingConnection(pika.ConnectionParameters(self.MQ_ip,self.MQ_port,'/',credentials)) #提供IP和port地址
        channel = connect.channel() #构建一个通道的对象

        #2. 创建队列
        channel.queue_declare(queue=self.co_queue) #队列的名字和生产者一样


        #回调函数，用于执行接收到消息后执行的语句
        #接收的消息为软件包的名字和编译状态信息，一个list，里面为字符串

        
        #TODO body的类型和结构
        def callback(ch, method, properties, body):  
            self.modify_data(body[0],body[1])

        #接收设置
        channel.basic_consume(  callback,
                                queue=self.co_queue,  #指定要接受的队列的名字
                                auto_ack=True) #是否要队列自动回复，如果是，就是直接从消息队列中拿出消息后rabbitMQ就会删除这个消息，
                                                #如果不是，就需要手动指定，一般是在回调函数的结尾手动回复，这样避免中间出问题导致消息丢失  


        channel.start_consuming() #这里开始监听队列



    #更新数据库
    def modify_data(self,name, state):
        db = pymysql.connect(host = self.sql_host,user = self.sql_user ,password=self.sql_password,database=self.sql_db)
        #创建一个cursor对象
        cursor = db.cursor()

        try:
            modif = "UPDATE %s SET %s = '%s'  WHERE %s= '%s'" %(self.sql_table, self.sql_table_stname, state, self.sql_table_sfname, name)
            cursor.execute(modif) #执行
            db.commit()    #对数据库的操作和修改要提交到数据库
        except:
            db.rollback() #出错回滚

        db.close()



