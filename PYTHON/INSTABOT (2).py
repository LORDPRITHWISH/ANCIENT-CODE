from instabot import *
import os 
import glob
import time
import random

cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])

lines=['I AM NOT A HUMAN I AM A LABRAT','LAL ROBO BOY','IT IS A GOOD PROGRAM I LOVE IT','I AM HERE FROM A SON OF GOD A PYTHON LOVER']
user=['amitghosh3245','darknight999z']
bot = Bot()
bot.login( username='darkson22557x', password='Sampa2004#')

while True :
    # bot.send_message('I AM HERE FROM A SON OF GOD A PYTHON LOVER','darknight999z')
    for i in user :
        bot.send_message(random.choice(lines),i)
        time.sleep(100)
        
    time.sleep(3600)

bot.logout()