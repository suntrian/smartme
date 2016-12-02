# /usr/bin/python3

from command import Command
from wxBot.wxbot import WXBot


class Context:
    """

    """
    def __init__(self):
        self.msg_handle = WXBot(self)
        self.cmd_handle = Command(self)
        self.module = []