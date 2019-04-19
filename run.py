#!/usr/bin/env python
import sys
import os
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Bot
from bs4 import BeautifulSoup

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

def navigate(command, chat_id):
    path = '%s/%s' % (bot_path,command)
    img_path = '%s/image.png' % path
    print(img_path)
    if os.path.isfile(img_path):
        bot.send_photo(chat_id=chat_id, photo=open(img_path, 'rb'))
    message_path = path+'/message.txt'
    if os.path.isfile(message_path):
        
        with open(message_path) as f:
            but_txt = f.read()
        soup = BeautifulSoup(but_txt, 'html.parser')
        msg = soup.find('message')
        btns = soup.findAll('button')
        btn_lst = []
        for bt in btns:
            btn_lst.append(InlineKeyboardButton(bt.text,callback_data=bt['value']))
        button_list = InlineKeyboardMarkup(build_menu(btn_lst,n_cols=1))
        print(button_list)
        bot.send_message(chat_id, msg.text, reply_markup=button_list)


def build_menu(buttons,n_cols):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    return menu

def press_button(update: Updater, context: CallbackContext):
    print("Pressing button %s" % update.callback_query.data)
    navigate(update.callback_query.data,update.callback_query.message.chat_id)

def start(update: Updater, context: CallbackContext):
    print("Start command!")
    username = update.message.from_user['username']
    room_id = update.message.chat_id 
    #first_message(room_id)
    navigate('index',update.message.chat_id)

    '''
    print("Username is %s room_id=%s" % (username,room_id))
    bot.send_message(room_id,'Hello. How are you?')
    bot.send_photo(chat_id=room_id, photo=open('%s/%s/index/1.jpeg' % (DATA_DIR, botname), 'rb'))
    button_list = []
    button_list.append(InlineKeyboardButton('Test 1',callback_data='one'))
    button_list.append(InlineKeyboardButton('Test 2',callback_data='two'))
    print(button_list)
    button_list = InlineKeyboardMarkup(build_menu(button_list,n_cols=1))
    print(button_list)
    bot.send_message(room_id, 'Buttons', reply_markup=button_list)
    '''
    

start_handler = CommandHandler('start', start)


updater = Updater(token=key, use_context=True)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(press_button))
updater.start_polling()