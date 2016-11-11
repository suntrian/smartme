# encoding: utf-8

from model import Model
from bs4 import BeautifulSoup as bs
import requests
import re
import util


class ICBC(Model):
    """

    """
    _HTML_PARSER = 'html.parser'
    __headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Referer': 'http://www.icbc.com.cn/ICBCDynamicSite/Charts/TimeLine.aspx?pWidth=1010&pHeight=600&dataType=0&dataId=901&picType=3',
        'Host': 'www.icbc.com.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }
    code = {
        'gold': 901,  # 人民币黄金
        'silver': 903,  # 人民币白银
        'platinum': 905,  # 人民币铂金
        'palladium': 907  # 人民币钯金
    }
    _api = "http://www.icbc.com.cn/ICBCDynamicSite/Charts/TimeLine.aspx?pWidth=1010&pHeight=600&dataType=0&picType=3"

    def __init__(self, varieties, file=None):
        Model.__init__(self, varieties, file)
        self.name = varieties
        self.file_name = file
        self.update_frequency = 30
        self.flush_cache_time = 120

    def update(self):
        html = self.get_data(self.name)
        cur_price = self.parse_cur_data(html)
        rest = self.deal_sequence(cur_price)
        print(rest)
        Model.update(self)

    def get_data(self, varieties):
        if type(varieties) is int and varieties in self.code.values():
            dataid = str(varieties)
        elif isinstance(varieties, str) and varieties in self.code.keys():
            dataid = self.code[varieties]
        else:
            dataid = '903'
        url = self._api + '&dataId=%s' % dataid
        self.__headers['Referer'] = url
        data = requests.get(url, headers=self.__headers, timeout=30)
        if not data.ok:
            return False
        html_str = data.text.encode('utf-8')
        return html_str

    def parse_cur_data(self, html_str):
        soup = bs(html_str, self._HTML_PARSER)
        items = soup.table.table.table.findAll('td')
        uptime = items[0].span.text.strip()
        price = items[2].span.text.strip()
        name = items[9].text.strip()
        return {'name': name, 'price': price, 'uptime': uptime}

    def deal_sequence(self, cur_data):
        uptime = cur_data.get('uptime','1970-01-01 00:00:00')
        s = ','.join([cur_data['name'], cur_data['price'], cur_data['uptime']])
        curtime = util.timestr_to_timestamp(uptime, util.std_time_fmt)
        pretime = util.timestr_to_timestamp(self.pre_update_time, util.std_time_fmt)
        if pretime < curtime:
            self.pre_update_time = uptime
            self.writecache(s)
            return s
        elif pretime == curtime:
            print('==%s' % uptime)
            return False
        else:
            if len(self.cache) == 0:
                self.writecache(s)
                return s
            self.pre_update_time = self.cache[-1:][0].split(',')[-1:][0]
            for i in range(len(self.cache), 0, -1):
                temptime = self.cache[i-1].split(',')[-1:][0]
                tempt = util.timestr_to_timestamp(temptime, util.std_time_fmt)
                if tempt > curtime:
                    continue
                elif tempt == curtime:
                    print('<=%s' % uptime)
                    return False
                else:
                    self.lock.acquire()
                    self.cache.insert(i-1, s)
                    self.lock.release()
                    return s

    def parse_day_data(self, html_str):
        re_str = r'dataCell.cell0 = "([\d\-: ]*?)";dataCell.cell1 = "([\d\.]*?)"'
        res = re.findall(re_str, html_str.decode('utf-8'), flags=re.MULTILINE)
        hist = []
        pretimestamp = 0
        for rr in res:
            uptime = rr[0]
            price = rr[1]
            timestamp = util.timestr_to_timestamp(uptime, '%Y-%m-%d %H:%M:%S')
            if timestamp != pretimestamp:
                hist.append((price, timestamp))
                pretimestamp = timestamp
        return hist


class MetalMarket:
    """

    """

    def __init__(self):
        self.goods = []
