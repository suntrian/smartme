# -*- coding:utf-8 -*-
"""
单支股票和股市情况
Created on 2016/11.10
@author: Suntrian
@contact: suntrian@126.com
"""

import tushare as ts
import util
import os
import model


def get_cur_data(sharecode):
    dt = ts.get_realtime_quotes(sharecode)
    dt.to_csv(os.path.join(util.get_cur_path(), 'data', 'today.txt'), index=False)


def get_hist_data(sharecode):
    dt = ts.get_hist_data(sharecode)


def get_today_data():
    dt = ts.get_today_all()


class Stock(model.Model):
    """

    """
    def __init__(self, code, file=None):
        model.Model.__init__(self, file)
        self.sharecode = code
        self.filename = file

    def update(self):
        data = ts.get_realtime_quotes(self.sharecode)
        dt = data.get('date')[0]
        tm = data.get('time')[0]
        update_time = util.timestr_to_timestamp('%s %s'%(dt, tm), '%Y-%m-%d %H:%M:S')
        if update_time <= self.pre_update_time:
            return
        data_str = data.to_csv(header=False, index=False)
        self.write(data_str + '\n')
        model.Model.update(self)

class StockMarket:
    """
        获取沪深上市公司基本情况
        Return
        --------
        DataFrame
               code,代码
               name,名称
               industry,细分行业
               area,地区
               pe,市盈率
               outstanding,流通股本
               totals,总股本(万)
               totalAssets,总资产(万)
               liquidAssets,流动资产
               fixedAssets,固定资产
               reserved,公积金
               reservedPerShare,每股公积金
               eps,每股收益
               bvps,每股净资
               pb,市净率
               timeToMarket,上市日期
    """

    def get_stocks(self):
        return ts.get_stock_basics()

