import os.path
import subprocess

from ABSPkg.env import bsdtar_path, md5sum_path, sha256sum_path
from ABSPkg.options import desc_key, desc_key_order, desc_list, package_info_key, package_info_key_renamed, \
    package_info_list, \
    package_info_list_renamed


def get_pkginfo(filename, pgp_signature: str) -> dict[str, str]:
    """
    Reads the package info from the given file.
    """
    md5sum = subprocess.check_output([md5sum_path, filename]).decode("utf-8").split(" ")[0]
    sha256sum = subprocess.check_output([sha256sum_path, filename]).decode("utf-8").split(" ")[0]
    content = subprocess.check_output([bsdtar_path, "-xOqf", filename, ".PKGINFO"]).decode("utf-8").strip()
    lines = content.splitlines()
    pkginfo = {
        "filename":  os.path.basename(filename),
        "csize":     "{}".format(os.path.getsize(filename)),
        "md5sum":    md5sum,
        "sha256sum": sha256sum,
        "pgpsig":    pgp_signature,
        }
    for line in lines:
        if line.startswith("#"):
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if key in package_info_key:
            pkginfo[key] = value
        elif key in package_info_list:
            if key not in pkginfo:
                pkginfo[key] = []
            pkginfo[key].append(value)
        elif key in package_info_key_renamed:
            pkginfo[package_info_key_renamed[key]] = value
        elif key in package_info_list_renamed:
            if package_info_list_renamed[key] not in pkginfo:
                pkginfo[package_info_list_renamed[key]] = []
            pkginfo[package_info_list_renamed[key]].append(value)
        else:
            print("WARNING: Unknown key '{}' in PKGINFO".format(key))

    if "name" not in pkginfo:
        raise RuntimeError("No pkgname in PKGINFO")
    if "version" not in pkginfo:
        raise RuntimeError("No pkgver in PKGINFO")

    return pkginfo


def desc_handler(desc_file: str) -> dict:
    '''
    Reads the desc file and returns a dictionary with the content.

    Args:
        desc_file: Absolute path to the desc file.
    '''
    gen_list: list[str] = list(filter(lambda x: x != "", map(lambda x: x.strip(), desc_file.splitlines())))
    currentitem = None
    pkginfo = {}
    for item in gen_list:
        if item.startswith("%"):
            currentitem = item[1:-1].lower()
            continue
        if currentitem is None:
            raise RuntimeError("Desc file is not valid")
        if currentitem in desc_key:
            pkginfo[currentitem] = item
        elif currentitem in desc_list:
            if currentitem not in pkginfo:
                pkginfo[currentitem] = []
            pkginfo[currentitem].append(item)
        else:
            print("WARNING: Unknown key '{}' in DESC".format(currentitem))
    return pkginfo


def entry_formatter(key: str, content: dict[str, str]) -> str:
    """
    Formats the given entry.
    """
    if key not in content:
        return ""
    if type(content[key]) is list:
        content_string = "\n".join([i.strip() for i in content[key]])
    else:
        content_string = content[key].strip()
    return "%{}%\n{}\n".format(key.upper(), content_string)


def generate_files(filename: str) -> str:
    '''
    Generates the files section of the package.

    Args:
        filename: Absolute path ot the generated files.
    '''
    content = subprocess.check_output([bsdtar_path, "--exclude=^.*", "-tf", filename]
                                      ).decode("utf-8").splitlines(keepends=False)
    return "%FILES%\n" + "\n".join(content) + "\n"


def generate_desc(pkginfo: dict[str, str]) -> str:
    '''
    Generates the desc section of the package.

    Args:
        pkginfo: dictionary [str, str] created by get_pkginfo()
    '''
    retval = "\n".join(filter(lambda x: x != "", [entry_formatter(key, pkginfo) for key in desc_key_order]))
    return retval
