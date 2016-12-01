# -*- coding: utf-8 -*-
import os
from threading import Thread

class Deamon(Thread):

    def __init__(self):
        self.filelist = []

    def _check_filesize(self, file):
        if os.path.exists(file):
            filesize = os.path.getsize(file)
            if filesize >= self.file_threshold:
                filename = os.path.basename(file)
                pathname = os.path.dirname(file)
                suffix = filename[filename.rfind('.')+1:]
                try:
                    serial = int(suffix)
                    return os.path.join(pathname, filename[:filename.rfind('.')+1]+str(serial+1))
                except ValueError as e:
                    return os.path.join(pathname, filename+'.2')
        return file