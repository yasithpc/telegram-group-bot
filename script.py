import telebot

bot = telebot.TeleBot("1607176195:AAE6t21ata7f-EMssrzD_ulRF-yikcvfa-I")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hi soosai, how are you ?")


bot.polling()
