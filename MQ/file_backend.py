import fsspec

from .env import ftp_host, ftp_pass, ftp_port, ftp_user


class FileEngine:
    def __init__(self):
        # TODO: Add config file
        print("Connecting ftp://{}:{}@{}:{}".format(ftp_user, ftp_pass, ftp_host, ftp_port))
        self.file_engine = fsspec.filesystem("ftp", host=ftp_host, port=ftp_port, username=ftp_user, password=ftp_pass)

    pass
