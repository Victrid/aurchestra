import MQ
from MQ.MQClient import MQReceiver
# TODO
client = MQReceiver("amqp://user:password@host:port/virtualhost")
client.run()
