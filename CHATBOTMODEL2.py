import sys
import ChatBotModel

def proc_rolling(bot, update):
    chii.sendMessage('데구르르..')
    sound = firecracker()
    chii.sendMessage(sound)
    chii.sendMessage('르르..')

def proc_stop(bot, update):
    chii.sendMessage('치이 봇이 잠듭니다.')
    chii.stop()

def firecracker():
    return '팡팡!'

chii = ChatBotModel.BotChii()
chii.add_handler('rolling', proc_rolling)
chii.add_handler('stop', proc_stop)
chii.start()