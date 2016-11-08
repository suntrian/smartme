#!/usr/bin/python3.5
# ! encoding: utf-8
# __author__ = suntrian

from queue import Queue

from wxBot.wxbot import WXBot
from wxBot import emotion
import random
import re

class BingBot(WXBot):
    '''
    把从联系人发的消息转发给小冰，然后把小冰的回复转发回去
    唂咿呀咿哈哈哈哈哈哈
    '''

    def __init__(self):
        WXBot.__init__(self)
        self.userqueue = Queue()
        self.bing_id = '@69edc26aeeb6bbd78d8b82f3f75cdf7b'  # 小冰id
        self.bing_name = '小冰'

    def handle_msg_all(self, msg):
        msgtype = msg[WXBot.DICT_MSG_KEY_MSG_CONTENT][WXBot.DICT_MSGCONTENT_KEY_TYPE]
        if msg[WXBot.DICT_MSG_KEY_USERFROM]['name'] == self.bing_name:
            if not self.userqueue.empty():
                user_to = self.userqueue.get()
                if msgtype == WXBot.CONTENT_TYPE_TEXT:  # text msg
                    self.send_msg_by_uid(emotion.gen_random_emotion() + msg[WXBot.DICT_MSG_KEY_MSG_CONTENT][WXBot.DICT_MSGCONTENT_KEY_DATA], user_to)
                elif msgtype == WXBot.CONTENT_TYPE_IMAGE:
                    self.send_msg_by_uid('呵呵' + emotion.gen_random_emotion(), user_to)
                elif msgtype == WXBot.CONTENT_TYPE_VOICE:
                    self.send_msg_by_uid('哈哈' + emotion.gen_random_emotion(), user_to)
                elif msgtype == WXBot.CONTENT_TYPE_EMOTICON:
                    self.send_msg_by_uid('嘻嘻' + emotion.gen_random_emotion(), user_to)
                else:
                    self.send_msg_by_uid('嗯呢' + emotion.gen_random_emotion(), user_to)
        else:
            if msgtype == WXBot.CONTENT_TYPE_TEXT and msg[WXBot.DICT_MSG_KEY_FROM_TYPE] == WXBot.MSG_FROM_CONTACT:  # from contract and text msg
                self.send_msg(self.bing_name, msg[WXBot.DICT_MSG_KEY_MSG_CONTENT][WXBot.DICT_MSGCONTENT_KEY_DATA])
                self.userqueue.put(msg[WXBot.DICT_MSG_KEY_USERFROM]['id'])


def main():
    bot = BingBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
