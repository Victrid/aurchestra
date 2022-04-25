import pika

from .file_backend import FileEngine


class MQBase:
    def __init__(self, connection: str):
        self.connection = connection
        self.file_engine = FileEngine()
        self.conn = pika.BlockingConnection(pika.URLParameters(self.connection))
        self.channel = self.conn.channel()
        self.channel.queue_declare(queue='work_dispatch')

    def __del__(self):
        self.conn.close()
