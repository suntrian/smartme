# encoding: utf-8

import os


class DataClass:
    """
        it's a base class
    """
    CNY = '¥/g'
    USD = "$/oz"
    SEP = ';'

    def __init__(self):
        self.name = ''
        self.buyin = 0.0
        self.sellout = 0.0
        self.price = 0.0  # middle price between in and out
        self.unit = '¥/g'  # 元/克or "$/oz" 美元/盎司
        self.uptime = 0
        self.comment = ''

    def update(self):
        """
        update date from web data
        :return: self
        """
        pass

    def save(self, fn):
        if not os.path.exists(os.path.dirname(fn)):
            return False
        with open(fn, 'a+',encoding='utf-8') as f:
            f.write(self.SEP.join([self.name,self.price,self.unit,self.uptime, self.comment]))

    def read(self,fn):
        if not os.path.exists(fn):
            return False
        with open(fn, 'r') as f:
            lines = f.read()
            seclines = []
            for line in lines.splitlines():
                secs = line.split(';')
                seclines.append(secs)
        return seclines
