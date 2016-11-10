import os
import sys
import time
# http://1212.ip138.com/ic.asp 获取公网ip

def get_cur_path():
    return os.path.split(os.path.realpath(sys.argv[0]))[0]
script_path = get_cur_path()


def timestamp_to_timestr(timestamp):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))


def timestr_to_timestamp(timestr, fmt):
    return time.mktime(time.strptime(timestr, fmt))


def timestr_to_timestr(timestr, fmt_from, fmt_to):
    return time.strftime(fmt_to, time.strptime(timestr,fmt_from))


if __name__ == '__main__':
    print(timestr_to_timestamp('2016-11-09 15:41:23','%Y-%m-%d %H:%M:%S'))

