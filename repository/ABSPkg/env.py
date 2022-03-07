import os

# Executable path
GPG_path = os.getenv('AURCHESTRA_GPGPATH', "/usr/bin/gpg")
md5sum_path = os.getenv('AURCHESTRA_MD5SUM_PATH', "/usr/bin/md5sum")
sha256sum_path = os.getenv('AURCHESTRA_SHA256SUM_PATH', "/usr/bin/sha256sum")
bsdtar_path = os.getenv('AURCHESTRA_BSDTAR_PATH', "/usr/bin/bsdtar")
mv_path = os.getenv('AURCHESTRA_MV_PATH', "/usr/bin/mv")

# Running directory
run_dir = os.getenv('AURCHESTRA_RUN_DIR', "/var/run/aurchestra/")
tmp_dir = os.getenv('AURCHESTRA_TMP_DIR', "/tmp/aurchestra/")
etc_dir = os.getenv('AURCHESTRA_ETC_DIR', "/etc/aurchestra/")
web_dir = os.getenv('AURCHESTRA_WEB_DIR', "/var/www/aurchestra/")

GPG_home = os.getenv('AURCHESTRA_GPGHOME', os.path.join(run_dir, ".gnupg"))
GPG_private_key_file = os.getenv('AURCHESTRA_PRIVATE_KEY_FILE', os.path.join(etc_dir, "private.key"))

repo_name = os.getenv('AURCHESTRA_REPO_NAME', "aurchestra")