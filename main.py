import telebot
from config.py import bot_token

bot = telebot.TeleBot(bot_token)
#test
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"test")