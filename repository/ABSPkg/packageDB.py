import os
import random
import shutil
import subprocess

from ABSPkg import env
from ABSPkg.env import bsdtar_path, mv_path, repo_name, web_dir


class PackageDB:
    """
    Class to handle the creation of package database.
    """

    def __init__(self):
        self.packages = []

    def add_package(self, pkg_title: str, pkg_files: str, pkg_desc: str):
        self.packages.append(
                (pkg_title, pkg_files, pkg_desc)
                )

    def update_db(self):
        package_name = os.path.join(env.tmp_dir, "repo-{}".format(random.Random().randint(0, 10000)))
        while os.path.exists(package_name):
            package_name = os.path.join(env.tmp_dir, "repo-{}".format(random.Random().randint(0, 10000)))

        os.makedirs(package_name)

        files_dir = os.path.join(package_name, "files")
        db_dir = os.path.join(package_name, "db")

        os.makedirs(files_dir)
        os.makedirs(db_dir)
        for name, files_file, desc_file in self.packages:
            os.mkdir(os.path.join(files_dir, name))
            os.mkdir(os.path.join(db_dir, name))
            with open(os.path.join(files_dir, name, "files"), "w+") as f:
                f.write(files_file)
            with open(os.path.join(db_dir, name, "desc"), "w+") as f:
                f.write(desc_file)
            with open(os.path.join(files_dir, name, "files"), "w+") as f:
                f.write(desc_file)

        subprocess.run(
                [bsdtar_path, "czf", os.path.join(package_name, "{}.db.tar.gz".format(repo_name)), *os.listdir(db_dir)],
                cwd=db_dir
                )
        subprocess.run([bsdtar_path, "czf", os.path.join(package_name, "{}.files.tar.gz".format(repo_name)),
                        *os.listdir(files_dir)],
                       cwd=files_dir
                       )
        subprocess.run(
                [mv_path, os.path.join(package_name, "{}.db.tar.gz".format(repo_name)),
                 os.path.join(package_name, "{}.files.tar.gz".format(repo_name)), web_dir]
                )
        if not os.path.exists(os.path.join(web_dir, "{}.db".format(repo_name))):
            subprocess.run(["ln", "-s", "{}.db.tar.gz".format(repo_name),
                            os.path.join(web_dir, "{}.db".format(repo_name))
                            ]
                           )
        if not os.path.exists(os.path.join(web_dir, "{}.files".format(repo_name))):
            subprocess.run(["ln", "-s", "{}.files.tar.gz".format(repo_name),
                            os.path.join(web_dir, "{}.files".format(repo_name))
                            ]
                           )
        shutil.rmtree(package_name)
