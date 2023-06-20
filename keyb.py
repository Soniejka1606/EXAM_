import telebot
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from DATABASE import *
towns = ['Брестская область','Витебская область','Гомельская область','Гродненская область','Могилевская область','Минская область','Минск']
#клавиатру для регистрации
def reg_keyb():
    reg_keyb = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Регистрация", callback_data="registration")
    reg_keyb.add(b1)
    return reg_keyb

#клавиатру для выбора города
def chose_town():
    town = types.InlineKeyboardMarkup()
    for i in towns:
        b1 = types.InlineKeyboardButton(text=i, callback_data=f"town;{i}")
        town.add(b1)
    return town

#клавиатру для выбора действия после регистрации
def do_after_regostr():
    town = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text='Создать профиль', callback_data="Start_profil")
    town.add(b1)
    b2 = types.InlineKeyboardButton(text='Отменить регистрация', callback_data = "regist_delete")
    town.add(b2)
    return town
#добавить ли еще фотографию или нет
def add_pic_profil():
    town = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text='Добавить фотографию', callback_data="add_pic1")
    town.add(b1)
    b2 = types.InlineKeyboardButton(text='Хватит фотографий', callback_data="stop_pic")
    town.add(b2)
    return town
def add_pic_profil1():
    town = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text='Добавить фотографию', callback_data="add_pic2")
    town.add(b1)
    b2 = types.InlineKeyboardButton(text='Хватит фотографий', callback_data="stop_pic")
    town.add(b2)
    return town

# клавиатура для выбора диапазона возрастов для своей записи
def zakresy_lat():
    zakresy = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text='18-25', callback_data="18-25")
    zakresy.add(b1)
    b2 = types.InlineKeyboardButton(text='25-40', callback_data="25-40")
    zakresy.add(b2)
    b3 = types.InlineKeyboardButton(text='40+', callback_data="40-55")
    zakresy.add(b3)
    return zakresy

def age18_25a(a1,a2):
    '''
    :param a1: нижнее число диапазона возрастов
    :param a2: верхнее число диапазона возрастов
    :return: клавиатуру с возрастами
    '''
    zakresy = types.InlineKeyboardMarkup()
    for i in range(a1,a2):
        b1 = types.InlineKeyboardButton(text=str(i), callback_data=f"age_count {str(i)}")
        zakresy.add(b1)
    return zakresy
def start_search():
    zakresy = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Начать поиск", callback_data=f"start_seerch")
    zakresy.add(b1)
    b1 = types.InlineKeyboardButton(text="Показать мою карточку", callback_data=f"show_my_profil")
    zakresy.add(b1)
    return zakresy

def male_female():
    zakresy = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Женский", callback_data=f"girl")
    zakresy.add(b1)
    b1 = types.InlineKeyboardButton(text="Мужской", callback_data=f"boy")
    zakresy.add(b1)
    return zakresy

def male_female_param():
    zakresy = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Женский", callback_data=f"plec 1")
    zakresy.add(b1)
    b1 = types.InlineKeyboardButton(text="Мужской", callback_data=f"plec 0")
    zakresy.add(b1)
    b1 = types.InlineKeyboardButton(text="не важно", callback_data=f"plec None")
    zakresy.add(b1)
    return zakresy

def zakresy_lat_param():
    zakresy = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text='18-25', callback_data="laty 18-25")
    zakresy.add(b1)
    b2 = types.InlineKeyboardButton(text='25-40', callback_data="laty 25-40")
    zakresy.add(b2)
    b3 = types.InlineKeyboardButton(text='40+', callback_data="laty 40-55")
    zakresy.add(b3)
    b3 = types.InlineKeyboardButton(text='Не важно', callback_data="laty None")
    zakresy.add(b3)
    return zakresy

def chose_town_param():
    town = types.InlineKeyboardMarkup()
    for i in towns:
        b1 = types.InlineKeyboardButton(text=i, callback_data=f"TOWN;{i}")
        town.add(b1)
    b1 = types.InlineKeyboardButton(text="Не важно", callback_data=f"TOWN;None")
    town.add(b1)
    return town

def poisk():
    town = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Начинаем поиск", callback_data=f"GET_KART")
    town.add(b1)
    return town


def what_do(id):
    '''
    :return: клавиатура с кнопками что сделать когда увидит карточку
    '''
    town = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Like❤️️", callback_data=f"Like {id}")
    b2 = types.InlineKeyboardButton(text="Следующий▶️", callback_data=f"GET_KART1")
    town.add(b1, b2)
    return town

def dialog(id):
    '''
    :return: клавиатура с кнопками начать диалог или дальше
    '''
    town = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Начать диалог", callback_data=f"Dialog {id}")
    #b2 = types.InlineKeyboardButton(text="Следующий", callback_data=f"GET_KART2")
    b3 = types.InlineKeyboardButton(text="Посмотреть профиль собеседника", callback_data=f"ProfilSob {id}")
    town.add(b1)
    town.add(b3)
    return town

def answer(id):
    '''
    :return: клавиатура  с кнопкой ответить
    '''
    town = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Oтветить", callback_data=f"Answer {id}")
    b2 = types.InlineKeyboardButton(text="Посмотреть профиль собеседника", callback_data=f"ProfilSob {id}")
    town.add(b1,b2)
    return town

def add_keyb1():
    '''
    :return: клавиатура  для рекламы
    '''
    town = types.InlineKeyboardMarkup()
    b2 = types.InlineKeyboardButton(text="К поиску собеседника", callback_data=f"GET_KART1")
    town.add(b2)
    return town

def add_keyb(id_tg_komu_otvet):
    '''
    :return: клавиатура  для рекламы
    '''
    town = types.InlineKeyboardMarkup()
    b2 = types.InlineKeyboardButton(text="Ответить пользователю", callback_data=f"Admin_answer {str(id_tg_komu_otvet)}")
    town.add(b2)
    return town