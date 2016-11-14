from apscheduler.schedulers.background import BackgroundScheduler
import time

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

scheduler = BackgroundScheduler()
scheduler.add_job(abc, 'cron', hour='16', minute='52', day_of_week='0')
scheduler.add_job(stop, 'cron', hour='16', minute='55',second='5')
scheduler.start()



input()
stop()