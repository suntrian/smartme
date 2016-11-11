# encoding: utf-8

import metal
import sys

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