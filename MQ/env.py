import os

ftp_host = os.getenv('FTP_HOST', "127.0.0.1")
ftp_port = os.getenv('FTP_PORT', 21)
ftp_user = os.getenv('FTP_USER', "admin")
ftp_pass = os.getenv('FTP_PASS', "test")
repo_server = os.getenv('REPO_SERVER', "http://127.0.0.1:8080")
default_timeout = os.getenv('DEFAULT_TIMEOUT', 3600)
