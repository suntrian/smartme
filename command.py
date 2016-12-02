# encoding: utf-8

from threading import Thread


class Command(Thread):
    """
        接受命令，返回结果
        命令类型有1)查询2)更改
    """
    prompt = 'cmd:'

    def __init__(self, manager):
        Thread.__init__(self)
        self.manager = manager

    def run(self):
        self.go()

    def go(self):
        while True:
            try:
                cmd = input(self.prompt)
                cmd = cmd.upper()
                if cmd == '':
                    print(cmd)
                elif cmd == '':
                    print(cmd)
                elif cmd == 'QUIT':
                    break
                else:
                    print(cmd)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    command = Command()
    try:
        command.start()
    except KeyboardInterrupt:
        print('quit')
