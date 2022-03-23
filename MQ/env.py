import os

ftp_host = os.getenv('FTP_HOST')
ftp_port = os.getenv('FTP_PORT', 21)
ftp_user = os.getenv('FTP_USER')
ftp_pass = os.getenv('FTP_PASS')
