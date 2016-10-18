# encodeing: utf-8

import os


class DataClass():
    """

    """

    def __init__(self):
        self.name = ''
        self.buyin = 0.0
        self.sellout = 0.0
        self.price = 0.0  # middle price between in and out
        self.unit = '¥/g'  # 元/克or "$/oz" 美元/盎司
        self.uptime = 0
        self.comment = ''

    def update(self):
        '''
        update date from web data
        :return: self
        '''
        pass

    def persistence(self, fn):
        if not os.path.exists(fn):
            return False
        with open(fn, 'a+') as f:
            f.write(
                '%s;%s;%s;%s;%s;%s;\n' % (self.name, self.buyin, self.sellout, self.unit, self.uptime, self.comment))
