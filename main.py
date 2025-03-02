import telebot
    
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("token")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Пр я эко бот!")

@bot.message_handler(commands=['eco'])
def send_welcome(message):
    bot.reply_to(message, "Ну короче если мы не будем беречь землю она заболеет и мы все умрем.")

@bot.message_handler(commands=['fact'])
def send_welcome(message):
    bot.reply_to(message, "В тихом океане есть огромное мусорное пятно.")





bot.polling()
