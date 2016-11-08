# encoding: utf-8

from threading import Thread
import finance.tusharewrap
import wxBot.bingbot
import weather


class Command(Thread):
    """
        接受命令，返回结果
        命令类型有1)查询2)更改
    """
    prompt = 'cmd:'

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        self.go()

    def go(self):
        while True:
            try:
                cmd = input(self.prompt)
                if cmd == '':
                    print(cmd)
                elif cmd == '':
                    print(cmd)
                else:
                    print(cmd)
            except KeyboardInterrupt:
                print('quit')
            except Exception as e:
                print(e)

if __name__ == '__main__':
    command = Command()
    command.start()
