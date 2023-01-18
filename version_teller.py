import time

import schedule
import telebot

import parser_html

API_KEY = "Your Api_key"
URL = "URL"
chat_ids = []
empty = []
bot = telebot.TeleBot(API_KEY)
version = None
try:
    with open('versions.txt', 'r') as versions:
        x = versions.readline()
        version = x[:-1]
except:
    with open('versions.txt', 'w') as versions:
        versions.write('')


def job():
    """
    Parses the page we need and determines whether there was an update in the version
    :return: None
    """
    global version, URL, chat_ids, empty, versions
    vs = parser_html.parser(URL)
    if version != vs and chat_ids != empty:
        version = vs
        with open('versions.txt', 'w') as versions:
            versions.write("%s\n" % str(version))
        for chat_id in chat_ids:
            bot.send_message(text="New version is " + version, chat_id=chat_id)


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


def chat_ids_updater(ch):
    global chat_ids
    chat_ids = ch
