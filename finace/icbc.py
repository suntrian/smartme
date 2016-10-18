#!/usr/bin/python3.5
# encoding:utf-8

import requests
from bs4 import BeautifulSoup

from finace.DataClass import DataClass


class ICBCDataClass(DataClass):
    __headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'http://www.icbc.com.cn/ICBCDynamicSite/Charts/TimeLine.aspx?pWidth=1010&pHeight=600&dataType=0&dataId=901&picType=3',
        'Host': 'www.icbc.com.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def __init__(self, url=''):
        DataClass.__init__(self)
        self.url = url
        self.requests = requests

    def set_url(self, url):
        self.url = url

    def update(self, url=''):
        if not self.url and not url:
            return False
        url = url if not url and url != self.url else self.url
        data = requests.get(url, headers=self.__headers, timeout=30)
        html = data.text

        if data.ok:
            return

    def parsedata(self, data):
        soup = BeautifulSoup(data)
        items = soup.table.table.table.findAll('td')
        uptime = items[0].span.text.strip()
        price = items[2].span.text.strip()
        comment = items[9].text.strip()


class ICBCDATA:
    '''
    # url:http://www.icbc.com.cn/ICBCDynamicSite/Charts/GoldTendencyPicture.aspx
    url : http://www.icbc.com.cn/ICBCDynamicSite/Charts/TimeLine.aspx?pWidth=1010&pHeight=600&dataType=0&dataId=903&picType=3   # silver
    data:
        paper_gold:{buyin:float, sellout:float, lowest:float, highest: float, uptime: int}
        paper_silver:{buyin:float, sellout:float, lowest:float, highest: float, uptime: int}
    '''

    def __init__(self):
        self.query_url = 'http://www.icbc.com.cn/ICBCDynamicSite/Charts/GoldTendencyPicture.aspx'
        self.paper_gold = DataClass()  # 人民币账户黄金
        self.paper_silver = DataClass()  # 人民币账户白银
        self.paper_Platinum = DataClass()  # 人民币账户铂金
        self.paper_Palladium = DataClass()  # 人民币账户钯金

    def query(self):
        try:
            requests.get(self.query_url)

        except Exception as e:
            print(e)
