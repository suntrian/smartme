import os
import sys
import time
import logging
# http://1212.ip138.com/ic.asp 获取公网ip


def public_ip():
    import socket
    with socket.create_connection(('ns1.dnspod.net',6666)) as sock:
        return sock.recv(16).decode()

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


def _check_filesize(self, file):
    if os.path.exists(file):
        filesize = os.path.getsize(file)
        if filesize >= self.file_threshold:
            filename = os.path.basename(file)
            pathname = os.path.dirname(file)
            suffix = filename[filename.rfind('.') + 1:]
            try:
                serial = int(suffix)
                return os.path.join(pathname, filename[:filename.rfind('.') + 1] + str(serial + 1))
            except ValueError as e:
                return os.path.join(pathname, filename + '.2')
    return file

if __name__ == '__main__':
    print(timestr_to_timestamp('2016-11-09 15:41:23','%Y-%m-%d %H:%M:%S'))
    logging.basicConfig(filename='smartme.log', level=logging.DEBUG)
    logging.debug('this my debug')
    logging.info('this is info')
    logging.warning('this is warning')
    logging.error('this is error')
    logging.critical('this is critical')

    print(public_ip())