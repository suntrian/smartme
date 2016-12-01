# /usr/bin/python3

from wxBot.wxbot import WXBot
from command import Command
import metal
import weather
from stock.Stock import MyStock


class Context:
    """

    """
    def __init__(self):
        self.msg_handle = WXBot(self)
        self.cmd_handle = Command(self)
        self.module = []