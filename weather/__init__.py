#!/usr/python3.5
# encoding:utf-8

'''
    心知天气api
    doc_url:http://www.thinkpage.cn/doc#sign

    新浪天气api
    api：http://php.weather.sina.com.cn/iframe/index/w_cl.php?code=js&day=0&city=&dfc=1&charset=utf-8

'''

import model
import requests
import util


class Weather(model.Model):
    """

    """

    def __init__(self, file=None):
        model.Model.__init__(self, file=file)
        self.api = Yaya()

    def update(self):
        data = self.api.update('abc')
        if isinstance(data, str):
            if self.file_name is not None:
                self.file_handler.write(data + '\n')
        else:
            return
        model.Model.update(self)


class Yaya:
    """
        key: 8omfd0ib98mdlqgp
        天气实况: http://api.yytianqi.com/observe?city=CH010100&key=8omfd0ib98mdlqgp
        # 24小时预报: http://api.yytianqi.com/weatherhours?city=CH010100&key=8omfd0ib98mdlqgp
    """

    def __init__(self):
        self.session = requests.session()
        self.session.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        self.key = '8omfd0ib98mdlqgp'
        self.api = 'http://api.yytianqi.com/observe'
        # self.api = 'http://api.yytianqi.com/weatherhours' # vip only
        # self.api = 'http://api.yytianqi.com/forecast7d'
        self.pre = {}

    def update(self, city):
        param = dict()
        param['city'] = 'CH010100'  # 北京
        # param['city'] = 'CH210901'  # 金华
        param['key'] = self.key
        result = self.session.get(self.api, params=param)
        if not result.ok:
            return False
        res_json = result.json()
        if res_json['msg'].lower() != 'sucess':
            return False
        data = res_json.get('data', {})
        cityname = data.get('cityName', '')
        uptime = data.get('lastUpdate', '')
        if self.pre.get('lastUpdate') == uptime:
            print('not updated')
            return True
        self.pre = data
        curweacher = data.get('tq', '')
        temperature = data.get('qw', '')
        wind = data.get('fl', '')
        wind_direct = data.get('fx', '')
        humanity = data.get('sd', '')
        return ','.join([cityname, uptime, temperature, humanity, curweacher, wind_direct, wind])


class ThinkPage:
    def __init__(self):
        self.api = 'https://api.thinkpage.cn/v3/weather/now.json?'
        self.location = 'beijing'
        self.uid = 'U20E304E3C'
        self.key = 'os08tnjdsqvbpzir'
        self.language = 'en'
        self.unit = 'c'
        self.pre_uptime = ''
        self.api_url = self.get_nomal_url()

    def get_nomal_url(self):
        return '%skey=%s&location=%s&language=%s&unit=%s' % (
        self.api, self.key, self.location, self.language, self.unit)

    def update(self, city):
        data = requests.get(self.api_url).json()
        result = data.get('results', False)
        if not isinstance(result, list):
            return False
        else:
            result = result[0]
        cityname = result['location']['name']
        uptime = result['last_update'].split('+')[0]
        uptime = util.timestr_to_timestr(uptime, '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S')
        if uptime == self.pre_uptime:
            return True
        temperature = result['now']['temperature']
        curweathre = result['now']['text']
        return ','.join([cityname, uptime, temperature, '', curweathre])


if __name__ == "__main__":
    weather = Weather('/home/yuanxm/weather.csv')
    weather.update()
    weather.save()

