from subprocess import run


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


def get_pkglist(working_dir, non_root=True):
    """
    Get the list of packages to be built
    :param non_root:
    :param working_dir:
    :return: File with absolute paths of packages
    """
    try:
        makepkg_proc = run(["/usr/bin/makepkg", "--packagelist"], cwd=working_dir, capture_output=True, text=True,
                           timeout=60, user=None if non_root else "nobody"
                           )
    except TimeoutError:
        # TODO timeout error
        return
    if makepkg_proc.returncode != 0:
        # TODO report error
        return
    output = makepkg_proc.stdout.split("\n")
    output = [x.strip() for x in output]
    output = list(filter(lambda x: x != "", output))
    return output


def retrieve_source_tar_path(file_path: str) -> str:
    # TODO: a better way to get the source file name
    source_file_name = run(["/usr/bin/makepkg", "--packagelist"], cwd=file_path, capture_output=True, text=True,
                           timeout=60,
                           ).stdout.split("\n")
    source_file_name = list(filter(lambda x: x.strip() != "", source_file_name))
    if len(source_file_name) < 1:
        raise MakepkgRuntimeError(-9, "", "makepkg --packagelist returned nothing.")
    source_file_name = "-".join(source_file_name[0].split("-")[:-1]) + ".src.tar.gz"
    return source_file_name
