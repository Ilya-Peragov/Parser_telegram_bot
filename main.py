import telebot
from telebot import TeleBot

import Version_teller

chat_ids: list = []
API_KEY = "Bot's API_KEY"

bot: TeleBot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def hello(message):
    """
    Add chat_id to the list and send a message about the start of the bot
    :param message: string
    :return: None
    """
    chat_ids.append(message.chat.id)
    bot.send_message(message.chat.id, 'Bot has been started')
    Version_teller.worker(chat_ids)


bot.infinity_polling()
