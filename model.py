# encoding: utf-8

import os
import io
import sys
from log import Logger
import time
import threading


class Model:
    """
        the base model
    """
    SAVE_BY_COUNT = 0
    SAVE_BY_TIME = 1

    flush_cache_count = 10  # counts
    flush_cache_time = 300  # seconds
    update_frequency = 30
    lock = threading.RLock()

    def __init__(self, name='', file=None):
        self.logger = Logger()
        self.name = name
        self.tag = ''
        self.rec_count = 0  # 缓存中的记录数
        self.file_handler = None  # 文件句柄
        self.save_mode = self.SAVE_BY_TIME  # 定时保存
        self.pre_update_time = "1970-01-01 00:00:00"
        self.file_name = file
        self.is_autosave = True
        self.is_updated = False
        self.is_stop = False
        if self.file_name is not None:
            self.open(self.file_name)
        self.cache = []
        self.logger.info('%s START' % self.name)

    def __del__(self):
        if self.file_handler is not None:
            self.file_handler.close()
            self.logger.info('%s END' % self.name)

    def update(self):
        """
        update data , parse and  write the data to file cache which will be written to file frequently
        :return: None
        """
        self.rec_count += 1
        self.is_updated = True
        self.logger.info('%s UPDATE' % self.name)
        raise NotImplementedError

    def run(self):
        """
        run the update in the main thread
        :return:
        """
        while not self.is_stop:
            try:
                self.update()
            except KeyboardInterrupt:
                self.close()
            except Exception as e:
                print(e)
            finally:
                try:
                    time.sleep(self.update_frequency)
                except Exception:
                    pass

    def start(self):
        update_thread = threading.Thread(target=self.run)
        update_thread.setDaemon(True)
        update_thread.start()

    def stop(self):
        self.is_stop = True

    def autosave(self):
        while self.is_autosave:
            if not self.is_updated:
                time.sleep(self.update_frequency)
                continue
            if self.save_mode == self.SAVE_BY_COUNT:
                time.sleep(self.update_frequency)
                if self.rec_count >= self.flush_cache_count:
                    self.write_and_save(self.cache)
                    self.lock.acquire()
                    self.cache.clear()
                    self.lock.release()
                    self.rec_count = 0
            elif self.save_mode == self.SAVE_BY_TIME:
                time.sleep(self.flush_cache_time)
                self.write_and_save(self.cache)
                self.lock.acquire()
                self.cache.clear()
                self.lock.release()
        # self.is_autosave = True

    def open(self, fn):
        if not os.path.exists(os.path.dirname(fn)):
            raise FileNotFoundError
        self.file_handler = open(fn, 'a+')
        save_thread = threading.Thread(target=self.autosave)
        save_thread.setDaemon(True)
        save_thread.start()
        return self.file_handler

    def close(self):
        self.is_autosave = False
        self.file_handler.close()

    def writecache(self, text):
        self.lock.acquire()
        self.cache.append(text)
        self.lock.release()

    def write(self, text):
        if self.file_handler is None:
            return False
        if not isinstance(self.file_handler, io.TextIOBase):
            return False
        if isinstance(text, str):
            self.file_handler.write(text)
        elif isinstance(text, list):
            self.file_handler.writelines(['%s\n' % l for l in text])
        else:
            self.file_handler.write(str(text) + '\n')
        if not self.is_autosave:
            self.file_handler.flush()
        return True

    def save(self):
        self.file_handler.flush()

    def write_and_save(self, text):
        self.write(text)
        self.save()

    def read(self):
        content = self.file_handler.read()
        return content


if __name__ == "__main__":
    model = Model()
    f = model.open('/home/yuanxm/b.txt')
    i = 0
    while True:
        f.write(str(i) + ":" + time.asctime() + '\n')
        i += 1
        model.update()
        time.sleep(10)
