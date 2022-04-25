import os
import shutil
import subprocess
import tempfile
from subprocess import run
from typing import Optional

from .env import default_timeout
from .MQBase import MQBase
from .makepkg_common import MakepkgRuntimeError, MakepkgTimeoutError, get_pkglist, retrieve_source_tar_path


class MQSender(MQBase):
    def __init__(self, connection: str):
        super().__init__(connection)

    def clean_cache(self) -> None:
        # Optional: cleanup cache for old files
        pass

    def send(self, file_path: str, timeout: Optional[int] = None) -> list[str]:
        # TODO: return the package list
        # First prepare the file to be sent
        with tempfile.TemporaryDirectory() as tmpdir:
            # copy the file to the temporary directory
            shutil.copytree(file_path, tmpdir, dirs_exist_ok=True)
            file_path = tmpdir
            if timeout is None:
                timeout = default_timeout
            try:
                makepkg_proc = run(["/usr/bin/makepkg", "-So", "--allsource"], cwd=file_path, capture_output=True,
                                   text=True, timeout=timeout
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
            self.channel.basic_publish(exchange='',
                                       routing_key="work_dispatch",
                                       body=source_base_name.encode()
                                       )

            self.clean_cache()
            return get_pkglist(file_path)
