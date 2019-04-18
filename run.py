#!/usr/bin/env python
import sys
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackContext
from telegram import Bot
DATA_DIR = 'storage'
try:
    botname = sys.argv[1]
except:
    print("Введите в качестве аргумента имя бота например ./run.py my_bot")
    sys.exit()
print("Запускаю бота %s" % botname)
bot_path = '%s/%s' % (DATA_DIR,botname)
print("Читаю настройки из %s" % bot_path)
f = open(bot_path+'/key','r')
key = f.read()
f.close()
print("Ключ: %s" % key)

bot = Bot(token=key)

def start(update: Updater, context: CallbackContext):
    print("Start command!")
    username = update.message.from_user['username']
    room_id = update.message.chat_id
    print("Username is %s room_id=%s" % (username,room_id))
    bot.send_message(room_id,'Hello!!!!!')
    bot.send_photo(chat_id=room_id, photo=open('%s/%s/index/1.jpeg' % (DATA_DIR, botname), 'rb'))
    

start_handler = CommandHandler('start', start)


updater = Updater(token=key, use_context=True)
updater.dispatcher.add_handler(start_handler)
updater.start_polling()