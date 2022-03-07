# To sign the package with global private key
import base64
import os
import shutil
import subprocess

from ABSPkg import env


class GPG:
    def __init__(self):
        self.gpg_path = env.GPG_path
        self.gpg_home = env.GPG_home
        self.private_key_file = env.GPG_private_key_file

        self.init_gpg_home()

    def init_gpg_home(self):
        if not os.path.isfile(self.gpg_path):
            raise FileNotFoundError('GPG not found')
        if not os.path.isfile(self.private_key_file):
            raise FileNotFoundError('Private key not found')

        # create an empty gpg_home
        if os.path.isdir(self.gpg_home):
            shutil.rmtree(self.gpg_home)
        os.makedirs(self.gpg_home, mode=0o700)

        # initiate gpg homedir
        subprocess.run([self.gpg_path, "--homedir", self.gpg_home, "--list-keys"], check=True)
        # import private key
        subprocess.run([self.gpg_path, "--homedir", self.gpg_home, "--import", self.private_key_file], check=True)

    def sign(self, package_path):
        subprocess.run([self.gpg_path, "--batch", "--yes", "--homedir", self.gpg_home, "--detach-sign", package_path],
                       check=True, capture_output=True
                       )

    def get_signature(self, package_path) -> str:
        if not os.path.isfile("{}.sig".format(package_path)):
            print("{}.sig".format(package_path))
            self.sign(package_path)
        with open("{}.sig".format(package_path), 'rb') as f:
            content = f.read()
        return base64.b64encode(content).decode("ascii")

    def __del__(self):
        if os.path.isdir(self.gpg_home):
            shutil.rmtree(self.gpg_home)
