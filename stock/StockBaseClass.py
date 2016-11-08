#encoding: utf-8

import os

class BaseStock:
    """
    base class
    """
    SEP = ';'
    def __init__(self):
        self.name = ''
        self.code = ''
        self.price = ''
        self.uptime = ''

    def update(self):
        pass

    def save(self,fn):
        if not os.path.exists(os.path.dirname(fn)):
            return False
        with open(fn, 'a+') as f:
            f.write(self.SEP.join([self.name, self.code, self.price, self.uptime, self.high, self.low, self.low, self.open, self.close]))
        return True

    def read(self,fn):
        if not os.path.exists(fn):
            return False
        with open(fn, 'r') as f:
            res = f.read()
            return res