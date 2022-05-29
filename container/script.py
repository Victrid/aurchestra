import MQ
from MQ.MQClient import MQReceiver
import os

address_for_mq = os.getenv("ADDRESS_FOR_MQ", "amqp://user:password@host:port/virtualhost")

client = MQReceiver(address_for_mq)
print("Connection to MQ is established successfully. ")
client.run()
