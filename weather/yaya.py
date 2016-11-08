#encoding: utf-8

"""
ref: http://www.yytianqi.com/api.html
api: http://api.yytianqi.com/接口名称?city=城市ID&key=用户key
"""

import requests
import json
import time

class Yaya:

    """
        key: 8omfd0ib98mdlqgp
        天气实况: http://api.yytianqi.com/observe?city=CH010100&key=8omfd0ib98mdlqgp
        # 24小时预报: http://api.yytianqi.com/weatherhours?city=CH010100&key=8omfd0ib98mdlqgp
    """
    def __init__(self):
        self.session = requests.session()
        self.session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        self.key = '8omfd0ib98mdlqgp'
        self.api = 'http://api.yytianqi.com/observe'
        # self.api = 'http://api.yytianqi.com/weatherhours' # vip only
        # self.api = 'http://api.yytianqi.com/forecast7d'
        self.pre = {}

    def update(self, fn=None):
        param = dict()
        param['city'] = 'CH010100'  # 北京
        # param['city'] = 'CH210901'  # 金华
        param['key'] = self.key
        result = self.session.get(self.api,params=param)
        if not result.ok:
            return
        res_json = result.json()
        if res_json['msg'].lower() != 'sucess':
            return
        data = res_json.get('data',{})

        city = data.get('cityName','')
        updtime = data.get('lastUpdate','')
        if self.pre.get('lastUpdate') == updtime:
            print('not updated')
            return
        self.pre = data
        curweacher = data.get('tq','')
        temprature = data.get('qw','')
        wind = data.get('fl','')
        wind_direct = data.get('fx','')
        humanity = data.get('sd','')

        if fn is None:
            import os
            fn = os.path.join(os.getcwd(),'weather_'+city+'.csv')
        weatherfile = open(fn, 'a')
        weatherfile.write('%s;%s;%s;%s;%s;%s;%s\n' % (city, updtime, temprature, humanity, curweacher, wind_direct, wind))
        weatherfile.close()

        print(data)

if __name__ == "__main__":
    yaya = Yaya()
    yaya.update()
    time.sleep(20)
    yaya.update()

