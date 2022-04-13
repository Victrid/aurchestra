

import logging
from logging import config
from env import logConfigPath
from logging import handlers

class myLogger(object):
    def __init__(self,loggerName='root') -> None:
        
        config.fileConfig(logConfigPath)
        self.logger = logging.getLogger(loggerName)

    def getmyLogger(self):
        return self.logger


if __name__ == '__main__':

    import time
    while True:
        weblogger = myLogger('web').getmyLogger()
        gitloger = myLogger('gitupdate').getmyLogger()
        dokerlogger = myLogger('docker').getmyLogger()
        weblogger.error('fffff')
        gitloger.error('fffff')
        dokerlogger.error('fffff')
        time.sleep(10)


