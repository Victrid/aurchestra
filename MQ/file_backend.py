import fsspec

import MQSender.env as env


class FileEngine:
    def __init__(self):
        # TODO: Add config file
        self.file_engine = fsspec.filesystem("ftp", host=env.ftp_host, port=env.ftp_port, username=env.ftp_user,
                                             password=env.ftp_pass
                                             )

    pass
