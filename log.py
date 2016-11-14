# encoding: utf-8

import logging


class Logger:
    """
        logging wrapper
    """

    def __init__(self,filename=''):
        self.log_level = logging.DEBUG
        self.log_filename = filename
        self.log_filemode = 'w+'                # read and write with open with empty file
        self.log_format = '[%(levelname)-7s] %(asctime)s %(threadName)s: %(message)s'
        self.log_time_fmt = '%Y-%m-%d %H:%M:%S'
        if isinstance(self.log_filename, str) and len(self.log_filename) > 0:
            self.basic_config(filename=self.log_filename, level=self.log_level, format=self.log_format)
        else:
            self.basic_config(level=self.log_level, format=self.log_format)

    def logfile(self, filename):
        self.log_filename = filename
        self.basic_config(filename=self.log_filename, level=self.log_level, format=self.log_format)

    @staticmethod
    def basic_config(**kwargs):
        logging.basicConfig(**kwargs)

    @staticmethod
    def debug(msg, *args, **kwargs):
        logging.debug(msg, *args, **kwargs)

    @staticmethod
    def info(msg, *args, **kwargs):
        logging.info(msg, *args, **kwargs)

    @staticmethod
    def warning(msg, *args, **kwargs):
        logging.warning(msg, *args, **kwargs)

    @staticmethod
    def error(msg, *args, **kwargs):
        logging.error(msg, *args, **kwargs)

    @staticmethod
    def critical(msg, *args, **kwargs):
        logging.critical(msg, *args, **kwargs)

    @staticmethod
    def exception(msg, *args, **kwargs):
        logging.exception(msg, *args, **kwargs)

if __name__ == '__main__':
    logger = Logger()
    logger.info('this is info')
    logger.debug('this is debug')
    logger.warning('this is warning')
    logger.error('this is error')
