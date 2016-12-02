# encoding: utf-8

import os
import shutil
import time
import logging
from threading import Thread

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


# @singleton
class Logger:
    """
        logging wrapper
    """

    log_dirname = 'log'
    log_filename = 'smartme.log'
    current_path = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.abspath(os.path.join(current_path, log_dirname))
    log_file = os.path.join(log_path, log_filename)

    MAX_LOGFILE_SIZE = 512*1024  # byte
    LOG_LEVEL = logging.DEBUG

    def __init__(self, name=None, loglevel=LOG_LEVEL, filename=''):
        self.log_level = loglevel
        self.log_file = filename if filename else self.log_file
        self.name = name if name else "SMARTME"
        self.log_filemode = 'a'
        self.file_handler = logging.FileHandler(self.log_file, mode=self.log_filemode)
        self.log_format = '%(asctime)s [%(levelname)-7s] %(name)s: %(message)s'
        self.log_time_fmt = '%Y-%m-%d %H:%M:%S'
        self.log_formatter = logging.Formatter(self.log_format, self.log_time_fmt)
        self.file_handler.setFormatter(self.log_formatter)
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(self.log_level)
        self.logger.addHandler(self.file_handler)
        deamon = LoggerDeamon(self)
        deamon.setDaemon(True)
        deamon.start()


    def get_logger(self, name):
        self.set_logger(name)
        return Logger(name, self.log_level, self.log_file)

    def set_logger(self, name):
        self.logger.name = name

    def roll_log(self):
        for i in range(1000):
            file_name = os.path.join(self.log_path, 'smartme.%d.log'%i)
            if os.path.isfile(file_name):
                continue
            shutil.move(self.log_file, file_name)
            self.logger.removeHandler(self.file_handler)
            self.file_handler = logging.FileHandler(self.log_file, mode=self.log_filemode)
            self.logger.addHandler(self.file_handler)
            return

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        self.logger.exception(msg, *args, **kwargs)

class LoggerDeamon(Thread):
    def __init__(self, logger):
        Thread.__init__(self)
        self.logger = logger
        self.check_interval = 60 # second

    def run(self):
        while True:
            filesize = os.path.getsize(self.logger.log_file)
            if filesize >= self.logger.MAX_LOGFILE_SIZE:
                self.logger.roll_log()
            time.sleep(self.check_interval)



if __name__ == '__main__':
    logger = Logger()
    # logger.get_logger('MMMMMMMMM')
    logger.info('1this is info')
    logger.debug('1this is debug')
    logger.warning('1this is warning')
    logger.error('1this is error')


    logger2 = Logger().get_logger('PPPPPPPPPPPPPP')
    logger2.info('222222222222222')
    logger2.get_logger('QQQQQQQQQQQQQQQQQQQQQQ')
    logger2.info('2this is info')
    logger2.debug('2this is debug')
    logger2.warning('2this is warning')
    logger2.error('2this is error')

    logger3 = Logger('TTTTTTTTTTTTTT')
    # logger3.set_logger('RRRRRRRRRRRRRRRRRRR')
    logger3.info('3this is info')
    logger3.debug('3this is debug')
    logger3.warning('3this is warning')
    logger3.error('3this is error')

    logger2 = Logger().get_logger('SSSSSSSSSSSSS')
    logger2.info('44444444444444444444')
    logger2.debug('$444444444444444444444444')
    logger2.warning('44444444444444444444444')

    logger.info('this log this log'*10)
