import time

import schedule
import telebot

import Parser

API_KEY = "Bot's API_KEY"
URL = "URL of site u need"

chat_ids = []
empty = []
bot = telebot.TeleBot(API_KEY)
Version = None


def job():
    """
    Parses the page we need and determines whether there was an update in the version
    :return: None
    """
    global Version, URL, chat_ids, empty
    vs = Parser.parser(URL)
    if Version != vs and chat_ids != empty:
        Version = vs
        for chat_id in chat_ids:
            bot.send_message(text="New version is " + Version, chat_id=chat_id)


def worker(ch):
    """
    Starts parsing every second
    :param ch: list
    :return: None
    """
    global chat_ids
    chat_ids = ch
    schedule.every().second.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
