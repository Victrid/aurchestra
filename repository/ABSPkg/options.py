# This file serves as a template applying ABS structure.

package_info_key = ["url", "builddate", "packager", "arch"]

package_info_key_renamed = {
    "pkgname": "name",
    "pkgbase": "base",
    "pkgver":  "version",
    "pkgdesc": "desc",
    "size":    "isize"
    }

package_info_list = ["license", "replaces", "provides"]

package_info_list_renamed = {
    "conflict":    "conflicts",
    "depend":      "depends",
    "group":       "groups",
    "optdepend":   "optdepends",
    "makedepend":  "makedepends",
    "checkdepend": "checkdepends"
    }

desc_key_order = [
    "filename", "name", "base", "version", "desc", "groups", "csize", "isize", "md5sum", "sha256sum", "pgpsig",
    "url", "license", "arch", "builddate", "packager", "replaces", "conflicts", "provides", "depends", "optdepends",
    "makedepends", "checkdepends"]

desc_key = [
    "url", "builddate", "packager", "arch", "name", "base", "version", "desc", "isize", "filename", "csize", "md5sum",
    "sha256sum", "pgpsig"
    ]

desc_list = [
    "license", "replaces", "provides", "conflicts", "depends", "optdepends", "makedepends", "checkdepends", "groups"]
