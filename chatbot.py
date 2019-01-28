# -*- coding: utf-8 -*-

"""
import telegram

chii_token = '691023739:AAGrtfuJ8Rbev9yw3YlM09FpcXse6Zgd1J4'
chii = telegram.Bot(token = chii_token)
updates = chii.getUpdates()

for u in updates:
    print(u.message)
"""

import chatbotmodel
import get_price
import get_champ
import telegram
from telegram.ext import Updater, MessageHandler, Filters  # import modules

def proc_price(bot, update):
    get_price.PLheader()
    get_price.PLdata()
    price = get_price.runrunrun()
    for u in price:
        EY.sendMessage(u)
    EY.sendMessage('실행중')
    

   
def get_message(bot, update) :
    print("receiving..")
    item=get_champ.callitem(update.message.text)
    a=1
    for i in item:
        if a==10:
            continue
        EY.sendMessage(str(a)+"위:"+i.string)
        a=a+1



def proc_stop(bot, update):
    EY.sendMessage('봇종료')
    EY.stop()


EY = chatbotmodel.Bot_EY()
EY.add_handler('price', proc_price)
EY.add_handler('stop', proc_stop)
#EY.add_handler('item', proc_item)

message_handler = MessageHandler(Filters.text, get_message)
EY.updater.dispatcher.add_handler(message_handler)

EY.start()

EY.start_polling(timeout=3, clean=True)
EY.idle()
