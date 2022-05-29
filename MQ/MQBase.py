import pika

from .file_backend import FileEngine


class MQBase:
    def __init__(self, connection: str):
        self.conn = None
        self.connection = connection
        self.file_engine = FileEngine()
        connection_par = pika.URLParameters(self.connection)
        connection_par.heartbeat = 0
        self.conn = pika.BlockingConnection(connection_par)
        self.channel = self.conn.channel()
        self.channel.queue_declare(queue='work_dispatch')

    def retry_connection(self):
        if self.conn is not None:
            try:
                self.conn.close()
            except:
                pass
        connection_par = pika.URLParameters(self.connection)
        connection_par.heartbeat = 0
        self.conn = pika.BlockingConnection(connection_par)

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
