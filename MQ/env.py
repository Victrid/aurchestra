import os
import os
import pwd

ftp_host = os.getenv('FTP_HOST', "127.0.0.1")
ftp_port = int(os.getenv('FTP_PORT', "21"))
ftp_user = os.getenv('FTP_USER', "admin")
ftp_pass = os.getenv('FTP_PASS', "test")
repo_server = os.getenv('REPO_SERVER', "http://127.0.0.1:8080")
default_timeout = int(os.getenv('DEFAULT_TIMEOUT', 3600))

daemon_server = os.getenv('DAEMON_SERVER', "http://127.0.0.1:8081")

current_user_is_root = os.getuid() == 0
