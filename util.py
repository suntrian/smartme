import os
import sys
import time
import logging
# http://1212.ip138.com/ic.asp 获取公网ip

def get_cur_path():
    return os.path.split(os.path.realpath(sys.argv[0]))[0]
script_path = get_cur_path()

std_time_fmt = "%Y-%m-%d %H:%M:%S"

def timestamp_to_timestr(timestamp):
    return time.strftime(std_time_fmt, time.localtime(timestamp))


def timestr_to_timestamp(timestr, fmt):
    return time.mktime(time.strptime(timestr, fmt))


def timestr_to_timestr(timestr, fmt_from, fmt_to):
    return time.strftime(fmt_to, time.strptime(timestr,fmt_from))


if __name__ == '__main__':
    print(timestr_to_timestamp('2016-11-09 15:41:23','%Y-%m-%d %H:%M:%S'))
    logging.basicConfig(filename='smartme.log', level=logging.DEBUG)
    logging.debug('this my debug')
    logging.info('this is info')
    logging.warning('this is warning')
    logging.error('this is error')
    logging.critical('this is critical')