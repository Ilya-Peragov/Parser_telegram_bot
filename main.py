import telebot
from telebot import TeleBot

import version_teller

chat_ids: list = []
try:
    with open('db_of_chat_ids.txt', 'r') as db_of_chat_ids:
        for ids in db_of_chat_ids:
            x = ids[:-1]
            chat_ids.append(int(x))
except:
    with open('db_of_chat_ids.txt', 'w') as db_of_chat_ids:
        db_of_chat_ids.write('')

version_teller.chat_ids_updater(chat_ids)
version_teller.job()

with open('db_of_chat_ids.txt', 'a') as db_of_chat_ids:
    API_KEY = "Your Api_key"
    bot: TeleBot = telebot.TeleBot(API_KEY)


    @bot.message_handler(commands=['start'])
    def hello(message):
        """
        Add chat_id to the list and send a message about the start of the bot
        :param message: string
        :return: None
        """

        if message.chat.id not in chat_ids:
            db_of_chat_ids.write("%s\n" % str(message.chat.id))
            chat_ids.append(message.chat.id)
            print(chat_ids)
        bot.send_message(message.chat.id, 'Bot has been started')
        version_teller.worker(chat_ids)


    bot.infinity_polling()
