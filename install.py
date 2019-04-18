#!/usr/bin/env python
import os
print('Start installation')
DATA_DIR = 'storage'
name = input('Укажите имя бота: ')
bot_path = '%s/%s' % (DATA_DIR, name)
if not os.path.exists(bot_path):
    os.makedirs(bot_path)
    if not os.path.exists(bot_path+'/index'):
        os.makedirs(bot_path+'/index')
    print("Creating folder %s" % bot_path)
else:
    print("Directory %s exists!!!" % bot_path)

key = input('Укажите ключ: ')
f = open('%s/key' % bot_path, 'w+')
f.write(key)
f.close()
print("Теперь запустите команду ./run.py")

