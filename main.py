# encoding: utf-8

from apscheduler.schedulers.background import BackgroundScheduler
import metal
from finance.stock import Stock
import sys

stock = Stock('600252','/home/yuanxm/stock_600252.csv')

scheduler = BackgroundScheduler()
scheduler.add_job(stock.start, 'cron', minute='30', hour='9', day_of_week='0-4')
scheduler.add_job(stock.stop, 'cron', minute='30', hour='11', day_of_week='0-4')
scheduler.add_job(stock.start, 'cron', minute='0', hour='13', day_of_week='0-4')
scheduler.add_job(stock.stop, 'cron', minute='0', hour='15', day_of_week='0-4')
scheduler.start()


icbc_silver = metal.ICBC('silver', '/home/yuanxm/silver_icbc.csv')
icbc_silver.start()

while True:
    cmd = input('$$:')
    cmd = cmd.lower()
    if cmd == 'stop':
        icbc_silver.stop()
    elif cmd == 'quit':
        break
    else:
        print(cmd)