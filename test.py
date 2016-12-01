from apscheduler.schedulers.background import BackgroundScheduler
import time
import os
import importlib
import model

import os.path as Path


current_path = os.path.dirname(os.path.abspath(__file__))

module = 'weather'
fromlist = ['weather']
mod = __import__(module)
mod2 = importlib.import_module('weather')
mod2.Weather('beijing').test()
obj = getattr(mod2, 'Weather')
print(obj)
ms = dir(mod2)
for m in ms:
    try:
        print(m,type(getattr(mod2, m)), issubclass(getattr(mod2, m), model.Model))
    except TypeError as e:
        print(e)

class Child:
    def __init__(self):
        self.name = self.__class__.__name__
        print('Child', self.name)

class Father(Child):
    def __init__(self):
        Child.__init__(self)
        self.name = self.__class__.__name__
        print('Pather', self.name)


Child()
Father()

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
