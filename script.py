import telebot

bot = telebot.TeleBot("1830651233:AAH64rmPGjcgMGDblRYkc4AMadENLaA1o0w")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hi soosai, how are you ?")


bot.polling()
