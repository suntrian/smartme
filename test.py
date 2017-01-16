from apscheduler.schedulers.background import BackgroundScheduler
import time
import os
import importlib
import model

import os.path as Path

import modules
import modules.metal
import modules.weather
print(dir(modules.metal))
print(dir(modules.weather))
print(dir(modules))
print(type(modules))
print(type(modules.weather), type(modules.weather.Yaya), type(modules.weather.city_parser), type(modules.weather.Weather), type(modules.weather.Logger))


current_path = os.path.dirname(os.path.abspath(__file__))


class Child:
    def __init__(self):
        self.name = self.__class__.__name__
        print('Child', self.name)

class Father(Child):
    def __init__(self):
        Child.__init__(self)
        self.name = self.__class__.__name__
        print('Pather', self.name)

def da():
    pass

c = Child()
f = Father()

print(type(Child), type(c),type(da), issubclass(Father, Child))

exit(0)

run = True


def abc():
    global run
    while run:
        print(time.asctime())
        time.sleep(5)


def stop():
    print('stoped')
    global run
    run = False


def start():
    print(time.asctime())


scheduler = BackgroundScheduler()
scheduler.add_job(abc, 'cron', hour='11', minute='23', day_of_week='3')
scheduler.add_job(stop, 'cron', hour='11', minute='24', second='5')
# scheduler.start()

input()
stop()
