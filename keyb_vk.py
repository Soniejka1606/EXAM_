import datetime
import os

import vk_api
from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
settings1 = dict(one_time=False, inline=False)
settings2 = dict(one_time=False, inline=True)
towns = ['Брестская область','Витебская область','Гомельская область','Гродненская область','Могилевская область','Минская область','Минск']


def towns_keyb():
    #выбор города
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button(towns[0], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город",'town':towns[0]})
    keyboard.add_callback_button(towns[1], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город", 'town': towns[1]})
    keyboard.add_line()
    keyboard.add_callback_button(towns[2], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город", 'town': towns[2]})
    keyboard.add_callback_button(towns[3], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город", 'town': towns[3]})
    keyboard.add_line()
    keyboard.add_callback_button(towns[4], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город", 'town': towns[4]})
    keyboard.add_callback_button(towns[5], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город", 'town': towns[5]})
    keyboard.add_line()
    keyboard.add_callback_button(towns[6], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город", 'town': towns[6]})
    return keyboard
def do_order():
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button('Меню', color=VkKeyboardColor.NEGATIVE, payload={'type': "меню"})
    keyboard.add_callback_button('Оформить заказ', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "Оформить заказ"})
    keyboard.add_line()
    keyboard.add_callback_button('Отменить заказ', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "Отменить заказ"})
    return keyboard


def buy_order():
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button('Подтвердить заказ', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "Подтвердить заказ"})
    keyboard.add_callback_button('Отменить заказ', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "Отменить заказ"})
    return keyboard

# Основное меню
keyboard_1 = VkKeyboard(**settings1)
keyboard_1.add_button(label='HELP', color=VkKeyboardColor.NEGATIVE, payload={"type": "text"})
keyboard_1.add_line()
keyboard_1.add_button(label='Зарегистрироваться!', color=VkKeyboardColor.PRIMARY, payload={"type": "text"})

keyboard_2 = VkKeyboard(**settings1)
keyboard_2.add_button(label='HELP', color=VkKeyboardColor.NEGATIVE, payload={"type": "text"})
keyboard_2.add_line()
keyboard_2.add_button(label='Начать', color=VkKeyboardColor.PRIMARY, payload={"type": "text"})

#клавиатура на описание
desc_1 = VkKeyboard(**settings1)
desc_1.add_button(label='HELP', color=VkKeyboardColor.NEGATIVE, payload={"type": "text"})
desc_1.add_line()
desc_1.add_button(label='/описание', color=VkKeyboardColor.PRIMARY, payload={"type": "/описание"})

def keyb_infa(cat_name, name_dish):
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button('Заказать', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "Заказать", "name_dish": name_dish})
    keyboard.add_line()
    keyboard.add_callback_button('Меню', color=VkKeyboardColor.NEGATIVE, payload={'type': "меню"})
    keyboard.add_callback_button('Назад в категорию', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "Назад в категорию", "data": cat_name})

    return keyboard

def women_men():
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button('Женский', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "указать пол", "women": "1" })
    keyboard.add_line()
    keyboard.add_callback_button('Мужской', color=VkKeyboardColor.NEGATIVE, payload={'type': "указать пол", "women": "0"})


    return keyboard

def create_profil():
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button('Создать профиль', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "Создать профиль"})
    return keyboard

def start_search_or_show_my_profil():
    desc_1 = VkKeyboard(**settings1)
    desc_1.add_button(label='Посмотреть мой профиль', color=VkKeyboardColor.NEGATIVE, payload={"type": "Посмотреть мой профиль"})
    desc_1.add_line()
    desc_1.add_button(label='Начать поиск', color=VkKeyboardColor.PRIMARY, payload={"type": "Начать поиск"})
    return desc_1

def chose_women():
    #клавиатура для выбара какой пол человек хочет
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button('Женский', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "выбрать пол", "women": "1"})
    keyboard.add_line()
    keyboard.add_callback_button('Мужской', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "выбрать пол", "women": "0"})
    keyboard.add_line()
    keyboard.add_callback_button('Не важно', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "выбрать пол", "women": "None"})

    return keyboard

def chose_diapazon():
    #клавиатура для выбара какой пол человек хочет
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button('18-25', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "выбрать диапазон", "range_age": "18-25"})
    keyboard.add_line()
    keyboard.add_callback_button('25-40', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "выбрать диапазон", "range_age": "25-40"})
    keyboard.add_line()
    keyboard.add_callback_button('40+', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "выбрать диапазон", "range_age": "40-55"})
    keyboard.add_line()
    keyboard.add_callback_button('Не важно', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "выбрать диапазон", "range_age": "None"})

    return keyboard

def choice_towns_keyb():
    #выбор города
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button(towns[0], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город выбор",'town':towns[0]})
    keyboard.add_callback_button(towns[1], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город выбор", 'town': towns[1]})
    keyboard.add_line()
    keyboard.add_callback_button(towns[2], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город выбор", 'town': towns[2]})
    keyboard.add_callback_button(towns[3], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город выбор", 'town': towns[3]})
    keyboard.add_line()
    keyboard.add_callback_button(towns[4], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город выбор", 'town': towns[4]})
    keyboard.add_callback_button(towns[5], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город выбор", 'town': towns[5]})
    keyboard.add_line()
    keyboard.add_callback_button(towns[6], color=VkKeyboardColor.NEGATIVE, payload={'type': "Город выбор", 'town': towns[6]})
    keyboard.add_callback_button("Не важно", color=VkKeyboardColor.NEGATIVE, payload={'type': "Город выбор", 'town': "None"})
    return keyboard

def start():
    #выбор города
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button("Поиск собеседника", color=VkKeyboardColor.NEGATIVE, payload={'type': "Поиск собеседника"})

    return keyboard

def scroll(number):
    #клавиатура для выбара какой пол человек хочет
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button('Like', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "like", "like_who": number})
    keyboard.add_line()
    keyboard.add_callback_button('Следующий', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "Следующий"})
    return keyboard

def add_next():
    #клавиатура для выбара какой пол человек хочет
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button('Следующий', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "Следующий"})
    return keyboard

def write_to_sob(number):
    '''
    :param number: айди понравившегося человека дает возможность
    :return: дает возможность либо написать либо посмотреть профиль
    '''
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button('Написать', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "Написать соб", "him_id": number})
    keyboard.add_line()
    keyboard.add_callback_button('Посмотреть профиль собеседника', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "Профиль собеседника","him_id": number})
    return keyboard

def answer(number):
    '''
    :param number: айди понравившегося человека дает возможность
    :return: дает возможность либо написать либо посмотреть профиль
    '''
    keyboard = VkKeyboard(**settings2)
    keyboard.add_callback_button('Ответить', color=VkKeyboardColor.NEGATIVE,
                                 payload={'type': "Написать соб", "him_id": number})

    return keyboard