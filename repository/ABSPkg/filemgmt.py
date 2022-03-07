import os.path

from ABSPkg import GPGUtils, env
from ABSPkg.PackageStubGenerator import desc_handler, get_pkginfo

gpg_client = GPGUtils.GPG()


class FileMgmt:
    def __init__(self):
        self.web_path = env.web_dir

    def upload_handler(self, form) -> tuple[bool, str, dict[str, str]]:
        filename = None
        for part in form:
            new_filename = os.path.join(self.web_path, part.secure_filename)
            if filename is not None and new_filename != filename:
                print(new_filename, filename)
                os.remove(filename)
                return False,"", {}
            filename = new_filename
            with open(filename, "wb+") as f:
                part.stream.pipe(f)
        if filename is None:
            return False, "", {}
        gpg_client.sign(filename)
        signature = gpg_client.get_signature(filename)
        pkg_info = get_pkginfo(filename, signature)
        return True, filename, pkg_info

    def remove_handler(self, desc_file_str: str):
        filename = desc_handler(desc_file_str)["filename"]
        os.remove(os.path.join(self.web_path, filename))
        os.remove(os.path.join(self.web_path, "{}.sig".format(filename)))
