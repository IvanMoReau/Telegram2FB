# -*- coding: utf-8 -*-

__author__ = 'XTickXIvanX'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import logging
logger = logging.getLogger(__name__)

from pytgbot import Bot, InputFile
import facebook

API_KEY="..."
graph = facebook.GraphAPI(access_token='...')
TEST_CHAT = 12345

bot = Bot(API_KEY)

my_info=bot.get_me()
print("Informacion del Bot: {info}".format(info=my_info))
last_update_id = 0

while True:
	# loop forever.
	for update in bot.get_updates(limit=100, offset=last_update_id+1)["result"]:
		last_update_id = update["update_id"]
		print(update)
		if "message" in update and "text" in update["message"]:

			if "chat" in update["message"]:
				sender = update["message"]["chat"]["id"]
			else:
				sender = update["message"]["from"]["id"]
				

			if "/publicar" in update["message"]["text"]:
				mnsj = update["message"]["text"]
				pong = mnsj.replace("/publicar ", "")
				if 140 >= len(pong):
					pong1 = pong
					graph.put_wall_post(message=pong1)
					bot.send_msg(sender, 'Hace poquito se publico lo siguiente en Facebook y Twitter: "'+pong1+'"')
				else:
					pong1 = "Intenta con menos caracteres"
					bot.send_msg(sender, 'Error: "'+pong1+'"')