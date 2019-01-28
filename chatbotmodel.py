# -*- coding: utf-8 -*-

import telegram
from telegram.ext import Updater, CommandHandler


class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 166243777
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()
        
class Bot_EY(TelegramBot):
    def __init__(self):
        self.token = '691023739:AAGrtfuJ8Rbev9yw3YlM09FpcXse6Zgd1J4'
        TelegramBot.__init__(self, 'EY_TAS', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('EY_TAS 봇 인식 완료.')
        self.updater.start_polling()
        self.updater.idle()
        
