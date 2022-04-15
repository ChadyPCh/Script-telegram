# -*- coding: utf-8 -*-
pip install python-telegram-bot
from telegram.ext import Updater , CommandHandler
import telegram

def start(Update , context) : 

	Update.message.reply_text("Hola")
	
	
	

if __name__ == '__main__':
	
	bot = telegram.Bot(token= "5351774574:AAGIhcHaxztx7Q779WUgVMLRuyDcSG1Xczo")
	updater = Updater(token= "5351774574:AAGIhcHaxztx7Q779WUgVMLRuyDcSG1Xczo" ,  use_context=True)
	
	update = Updater
	dp = updater.dispatcher
	
	dp.add_handler(CommandHandler('start', start))
		
	updater.start_polling()
	print("el bot Esta Corriendo")
	updater.idle()
	
