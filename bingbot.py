#!/usr/bin/python3.5
# ! encoding: utf-8
# __author__ = suntrian

from queue import Queue

from wxBot.wxbot import *


class BingBot(WXBot):
    '''
    把从联系人发的消息转发给小冰，然后把小冰的回复转发回去
    '''

    def __init__(self):
        WXBot.__init__(self)
        self.userqueue = Queue()
        self.bing_id = '@69edc26aeeb6bbd78d8b82f3f75cdf7b'  # 小冰id
        self.bing_name = '小冰'

    def handle_msg_all(self, msg):
        if msg['user']['name'] == self.bing_name:
            if not self.userqueue.empty():
                user_to = self.userqueue.get()
                if msg['content']['type'] == 0:  # text msg
                    self.send_msg_by_uid(msg['content']['data'], user_to)
                elif msg['content']['type'] == BingBot.CONTENT_TYPE_IMAGE:
                    self.send_msg_by_uid('呵呵', user_to)
                elif msg['content']['type'] == BingBot.CONTENT_TYPE_VOICE:
                    self.send_msg_by_uid('哈哈', user_to)
                else:
                    self.send_msg_by_uid('嗯呢', user_to)
        else:
            if msg['SubMsgType'] == 0 and msg['MsgType'] == WXBot.CONTENT_TYPE_TEXT:  # from contract and text msg
                self.send_msg(self.bing_name, msg['content']['data'])
                self.userqueue.put(msg['user']['id'])


def main():
    bot = BingBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
