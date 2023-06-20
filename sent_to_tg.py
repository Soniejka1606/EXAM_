import json
import os
import datetime
import time
import telebot
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from DATABASE import *
from  keyb import *
from send_to_vk import send_messege
import cenzura

bot = telebot.TeleBot('5907180411:AAGG_L1KNqmIj-3SeuqGBNPYFUe0hL82Dk8')
id_admin = -930672631

def sending_message(message,who,whom):
    '''
    :param message: сообщение
    :param who: кто отправляет
    :param whom: кому отправляет
    :return: пересылка сообщения
    '''
    print('ghbikj------------------')
    name = find_login(who)
    proverka = find_tg_or_vk(whom)
    pr = str(message.text)
    a = cenzura.cenzura1(pr)
    if a == False:
        bot.send_message(message.chat.id, "Это сообщение не отправлено, так как не прошло проверку на цензуру 🤬🤬🤬🤬")

    else:

        if proverka[1] == "tg":
            print('tg')
            #---
            name = find_login(who)
            komu = find_tg_id(whom)
            bot.send_message(int(komu), name + "\n" + message.text, reply_markup=answer(who))
            # try:
            #     bot.delete_message(message.chat.id, message.message_id - 1)
            # except:
            #     pass
            # try:
            #     bot.delete_message(message.chat.id, message.message_id - 2)
            # except:
            #     pass
        elif proverka[1] == "vk":
            name = find_login(who)
            text = message.text
            send_messege(proverka[0], name + "\n" + text, who)

def sending_message_vk(text,who,whom):
    '''
    :param message: сообщение
    :param who: кто отправляет
    :param whom: кому отправляет
    :return: пересылка сообщения
    '''
    print("дощло до функции")
    name = find_login(who)
    #proverka = find_tg_or_vk(whom)
    text = f'{name}\n{text}'
    bot.send_message(whom,  text, reply_markup=answer(who))

