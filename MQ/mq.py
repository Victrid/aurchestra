import os.path
import subprocess
from subprocess import run
from typing import Optional

import pika as pika

from MQSender.file_backend import FileEngine


class MakepkgError(Exception):
    pass


class MakepkgTimeoutError(MakepkgError):
    pass


class MakepkgRuntimeError(MakepkgError):
    def __init__(self, retval: int, stdout: str, stderr: str):
        self.return_code = retval
        self.stdout = stdout
        self.stderr = stderr

    pass


class MakepkgConnectionError(MakepkgRuntimeError):
    def __init__(self, retval: int, stdout: str, stderr: str):
        super().__init__(retval, stdout, stderr)

    pass


def retrieve_source_tar_path(file_path: str) -> str:
    # TODO: a better way to get the source file name
    source_file_name = run(["/usr/bin/makepkg", "--packagelist"], cwd=file_path, capture_output=True, text=True
                           ).stdout.split("\n")
    source_file_name = list(filter(lambda x: x.strip() != "", source_file_name))
    if len(source_file_name) < 1:
        raise MakepkgRuntimeError(-9, "", "makepkg --packagelist returned nothing.")
    source_file_name = "-".join(source_file_name[0].split("-")[:-1]) + ".src.tar.gz"
    return source_file_name


class MQSender:
    def __init__(self, connection: str):
        self.conn_str = connection
        self.file_engine = FileEngine()

    def clean_cache(self) -> None:
        # Optional: cleanup cache for old files
        pass

    def send(self, file_path: str, timeout: Optional[int] = None) -> None:
        # First prepare the file to be sent
        try:
            makepkg_proc = run(["/usr/bin/makepkg", "-So", "--allsource"], cwd=file_path, capture_output=True,
                               text=True, timeout=timeout
                               )
        except subprocess.TimeoutExpired:
            # Timed-out process will be killed by Python
            raise MakepkgTimeoutError
        if makepkg_proc.returncode != 0:
            # TODO: specify ConnectionError
            raise MakepkgRuntimeError(makepkg_proc.returncode, makepkg_proc.stdout, makepkg_proc.stderr)

        source_file_name = retrieve_source_tar_path(file_path)
        source_base_name = os.path.basename(source_file_name)

        # Send the file to file backend
        with self.file_engine.file_engine.open(os.path.join("/", source_base_name), "wb") as f:
            with open(source_file_name, "rb") as source_file:
                f.write(source_file.read())

        # Now dispatch the file to the queue
        with pika.BlockingConnection(pika.ConnectionParameters(self.conn_str)) as connection:
            channel = connection.channel()
            # This can be called multiple times, but it will only create one queue
            channel.queue_declare(queue='work_dispatch')
            channel.basic_publish(exchange='',
                                  routing_key="work_dispatch",
                                  body=source_base_name.encode()
                                  )

        self.clean_cache()
        return
