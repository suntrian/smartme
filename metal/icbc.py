#!/usr/bin/python3.5
# encoding:utf-8

import sys, os
import chardet
import re
import datetime
import requests
from bs4 import BeautifulSoup
from smartme.metal.DataClass import DataClass


class ICBCDataClass(DataClass):
    SOUPPARSER = 'html.parser'
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
        url = self.url if (not url and url != self.url) else url
        self.__headers['Referer'] = url
        data = requests.get(url, headers=self.__headers, timeout=30)
        if not data.ok:
            return
        html_str = data.text.encode('utf-8')
        ret = self.parsedata(html_str)
        hist = self.getdaydata(html_str)
        print(ret)
        print(hist)

    def parsedata(self, html_str):
        soup = BeautifulSoup(html_str,self.SOUPPARSER)
        items = soup.table.table.table.findAll('td')
        self.uptime = items[0].span.text.strip()
        self.price = items[2].span.text.strip()
        self.name = items[9].text.strip()

        return {'name':self.name,'price':self.price,'uptime':self.uptime}

    def getdaydata(self,html_str):
        re_str = r'dataCell.cell0 = "([\d\-: ]*?)";dataCell.cell1 = "([\d\.]*?)"'
        res = re.findall(re_str, html_str.decode('utf-8'), flags=re.MULTILINE)
        hist = []
        for rr in res:
            uptime = rr[0]
            price = rr[1]
            timestamp = int(datetime.datetime.strptime(uptime,'%Y-%m-%d %H:%M:%S').timestamp())
            hist.append((price,timestamp))
        return hist


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
        self.paper_gold = ICBCDataClass()  # 人民币账户黄金
        self.paper_silver = ICBCDataClass('http://www.icbc.com.cn/ICBCDynamicSite/Charts/TimeLine.aspx?pWidth=1010&pHeight=600&dataType=0&dataId=903&picType=3')  # 人民币账户白银
        self.paper_silver.unit = DataClass.CNY
        self.paper_Platinum = ICBCDataClass()  # 人民币账户铂金
        self.paper_Palladium = ICBCDataClass()  # 人民币账户钯金

    def query(self):
        try:
            self.paper_silver.update()
            self.paper_silver.save(os.path.join(os.getcwd(), 'silver.txt'))
        except Exception as e:
            print(e)

if __name__ == "__main__":
    icbc = ICBCDATA()
    icbc.query()