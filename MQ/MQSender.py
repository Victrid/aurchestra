import os
import shutil
import subprocess
import tempfile
import json
from subprocess import run
from typing import Optional

from pika.exceptions import AMQPConnectionError

from .env import default_timeout, current_user_is_root
from .MQBase import MQBase
from .makepkg_common import MakepkgRuntimeError, MakepkgTimeoutError, get_pkglist, retrieve_source_tar_path


class MQSender(MQBase):
    def __init__(self, connection: str):
        super().__init__(connection)

    def clean_cache(self) -> None:
        # Optional: cleanup cache for old files
        pass

    def send(self, name: str, file_path: str, timeout: Optional[int] = None) -> list[str]:
        # TODO: return the package list
        # First prepare the file to be sent
        with tempfile.TemporaryDirectory() as tmpdir:
            # copy the file to the temporary directory
            shutil.copytree(file_path, tmpdir, dirs_exist_ok=True)
            file_path = tmpdir
            os.chmod(file_path, 0o777)
            os.system('chown -R nobody {}'.format(file_path))
            print(os.stat(file_path))
            if timeout is None:
                timeout = default_timeout
            try:
                makepkg_proc = run(["/usr/bin/makepkg", "-So", "--allsource"], cwd=file_path, capture_output=True,
                                   text=True, timeout=timeout, user='nobody' if current_user_is_root else None
                                   )
            except subprocess.TimeoutExpired:
                # Timed-out process will be killed by Python
                raise MakepkgTimeoutError
            if makepkg_proc.returncode != 0:
                raise MakepkgRuntimeError(makepkg_proc.returncode, makepkg_proc.stdout, makepkg_proc.stderr)

            source_file_name = retrieve_source_tar_path(file_path)
            source_base_name = os.path.basename(source_file_name)

            # Send the file to file backend
            with self.file_engine.file_engine.open(os.path.join("/", source_base_name), "wb") as f:
                with open(source_file_name, "rb") as source_file:
                    f.write(source_file.read())

            # Now dispatch the file to the queue
            # TODO: update the retry strategy
            retry = 5
            while retry:
                try:
                    self.channel.basic_publish(exchange='',
                                               routing_key="work_dispatch",
                                               body=json.dumps({"name": name, "source": source_base_name}).encode()
                                               )
                    retry = 0
                except AMQPConnectionError:
                    retry -= 1
                    self.retry_connection()
                except Exception as e:
                    raise e


            self.clean_cache()
            return get_pkglist(file_path)
