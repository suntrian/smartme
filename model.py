# encoding: utf-8

import os
import time
import threading


class Model:
    """
        the base model
    """
    SAVE_BY_COUNT = 0
    SAVE_BY_TIME = 1
    auto_save_flag = True
    flush_threshold_count = 10              # counts
    flush_threshold_time = 300              # seconds
    update_frequency = 30

    def __init__(self, file=None):
        self.name = ''
        self.tag = ''
        self.rec_count = 0                  # 缓存中的记录数
        self.file_handler = None            # 文件句柄
        self.save_mode = self.SAVE_BY_TIME  # 定时保存
        self.pre_update_time = 0
        self.file_name = file
        self.is_updated = False
        if self.file_name is not None:
            self.open(self.file_name)

    def __del__(self):
        if self.file_handler is not None:
            self.file_handler.close()

    def update(self):
        """
        update data , parse and  write the data to file cache which will be written to file frequently
        :return: None
        """
        self.rec_count += 1
        self.is_updated = True

    def autosave(self):
        while self.auto_save_flag:
            if not self.is_updated:
                time.sleep(self.update_frequency)
                continue
            if self.save_mode == self.SAVE_BY_COUNT:
                time.sleep(self.update_frequency)
                if self.rec_count >= self.flush_threshold_count:
                    self.save()
                    self.rec_count = 0
            elif self.save_mode == self.SAVE_BY_TIME:
                time.sleep(self.flush_threshold_time)
                self.save()
        self.auto_save_flag = True

    def open(self, fn):
        if not os.path.exists(os.path.dirname(fn)):
            raise FileNotFoundError
        self.file_handler = open(fn, 'a+')
        save_thread = threading.Thread(target=self.autosave)
        save_thread.setDaemon(True)
        save_thread.start()
        return self.file_handler

    def close(self):
        self.auto_save_flag = False
        self.file_handler.close()

    def save(self):
        self.file_handler.flush()

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