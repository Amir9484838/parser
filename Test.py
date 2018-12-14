# -*- coding: utf-8 -*-
import config
import pytz
from datetime import datetime
import telebot
from telebot import types
import random
bot = telebot.TeleBot(config.token)


	
@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id,  'Hello. \n\n Write /help fro help.')
	bot.send_message(config.owner,'Привет, хозяин! ' + str(message.from_user.first_name) + ' использовал команду /start')

@bot.message_handler(commands=["help"])
def start(message):
	bot.send_message(message.chat.id, 'Help message😈')
	bot.send_message(config.owner,'Привет, хозяин! ' + str(message.from_user.first_name) + ' использовал команду /help')
	

@bot.message_handler(content_types=["text"])
def messages(message):
	if int(message.chat.id) == int(config.owner):
		try:
			chatId=message.text.split(': ')[0]
			text=message.text.split(': ')[1]
			bot.send_message(chatId, text)
		except:
			pass
	else:
		
		
		bot.send_message(config.owner, 'User: ' + str(message.from_user.first_name)  + 'Текст сообщения: ' + message.text)
		
		bot.send_message(config.owner, str(message.chat.id), str(message.message_id))
rand = 60*random.randint(1, 10)		
bot.send_message(config.owner, 'Я был запущен', 'rand')	

if __name__ == '__main__':
        bot.polling(none_stop = True)
print('random.uniform(0, 20)')
print('cedcbdjcbdhbchdb')