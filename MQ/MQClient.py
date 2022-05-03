import logging
import os
import tempfile
from subprocess import run
from urllib.parse import urljoin

import requests

from .MQBase import MQBase
from .env import default_timeout, repo_server, daemon_server
from .makepkg_common import MakepkgRuntimeError, MakepkgTimeoutError, get_pkglist

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# message format: {'name':'git', 'state':'3', 'info': '...'}
def send_report(name: str, state: int, info: str):
    url = urljoin(daemon_server, '')
    data = {
        'name':   name,
        'state':  state,    # 3 for success, 6 for fail
        'info':  info,
        }
    requests.post(url, data=data)


class MQReceiver(MQBase):
    def __init__(self, connection: str):
        super().__init__(connection)

    def message_callback(self, ch, method, properties, body):
        filename = body.decode('utf-8')
        logger.debug("Received message: {}".format(filename))
        if not self.file_engine.file_engine.exists(filename):
            # TODO: handle file not found
            logger.error("{} not found.".format(filename))
            ch.basic_ack(delivery_tag=method.delivery_tag)
            return
        logger.debug("{} downloaded.".format(filename))
        with tempfile.TemporaryDirectory() as tmpdir:
            # Allow nobody to R/W
            os.chmod(tmpdir, 0o777)
            with self.file_engine.file_engine.open(filename) as f:
                with open(os.path.join(tmpdir, "src.tar.gz"), "wb") as f_out:
                    f_out.write(f.read())
            ch.basic_ack(delivery_tag=method.delivery_tag)
            # Extract and compile
            logger.debug("Removed from queue: {}".format(filename))
            try:
                pkglist = self.compilation(tmpdir)
                send_report(filename, 3, pkglist)
            except MakepkgRuntimeError as e:
                send_report(filename, 6,
                                  "Return code {}:\nstdout:\n{}\nstderr:\n{}\n".format(e.return_code, e.stdout,
                                                                                       e.stderr
                                                                                       )
                                  )

    def compilation(self, working_dir):
        logger.debug("Starting extraction")
        run(["/usr/bin/tar", "xf", "src.tar.gz", "--strip-components=1"], cwd=working_dir,
            capture_output=True,
            text=True
            )
        logger.debug("Extraction done")
        self.compile_package(working_dir)
        return self.upload_package(working_dir)

    def compile_package(self, working_dir) -> None:
        """
        Compile the package
        :param working_dir:
        :return:
        """
        try:
            logger.debug("Starting compilation")
            makepkg_proc = run(["/usr/bin/extra-x86_64-build"], cwd=working_dir, capture_output=True, text=True,
                               timeout=default_timeout
                               )
        except TimeoutError:
            logger.error("Compilation timeout")
            raise MakepkgTimeoutError("Time out error occurs.\n", "")
        if makepkg_proc.returncode != 0:
            logger.error("Compilation failed")
            raise MakepkgRuntimeError(makepkg_proc.returncode, makepkg_proc.stdout, makepkg_proc.stderr)
        logger.debug("Compilation done")
        return

    def upload_package(self, working_dir):
        pkg_list = get_pkglist(working_dir, non_root=False)
        for pkg in pkg_list:
            logger.debug("Uploading {}".format(pkg))
            response = requests.post(urljoin(repo_server, "api/package"),
                                     files={os.path.basename(pkg): open(pkg, "rb")}
                                     )
            if response.status_code != 200:
                logger.error("Upload failed")
                raise MakepkgRuntimeError(response.status_code, response.text, "")
        return pkg_list

    def run(self):
        self.channel.basic_consume(queue='work_dispatch', on_message_callback=self.message_callback)
        self.channel.start_consuming()
