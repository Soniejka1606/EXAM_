import json
import os
import datetime
import time
import telebot
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import keyb
#598388419  - my_id
from DATABASE import *
from  keyb import *
from checking_security import *
from sent_to_tg import sending_message

bot = telebot.TeleBot('5907180411:AAGG_L1KNqmIj-3SeuqGBNPYFUe0hL82Dk8')
param_dict = {}
dict_for_add = {}
last_add = {}
id_admin = -930672631
name_aad_stp = {}
@bot.message_handler(content_types=['text'])
def start(message):
    id_tg = search_id_tg()
    if message.text == '/start':
        bot.send_message(message.chat.id, '''Здравствуйте, ВЫ находитель на платформе знакомсв TINDER2.0\n
❤️ /help - если у Вас возникли проблемы можете написать администратору
❤️ /start - чтобы начать
''')

    if str(message.chat.id) in id_tg and message.text != "/help":
        bot.send_message(message.chat.id, '''Вы зарегистрированы''', reply_markup=start_search())
    elif str(message.chat.id) not in id_tg and message.text != "/help":
        print(message.chat.id, id_tg)
        bot.send_message(message.chat.id,
                         '''Для того, чтобы начать пользоваться нашей платформой Вам необходимо зарегистрироваться''',
                         reply_markup=reg_keyb())
    if message.text == "/help":
        text = 'Опишите проблему Ваш запрос будет отправлен администратору, после рассмотрения вопроса вы получите ответ'
        a = bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(a, to_admin,message.chat.id)

def to_admin(message,otkogo):
    # переходит в админ группу запрос от пользователя
    bot.send_message(id_admin,message.text,reply_markup=add_keyb(otkogo))
def answer_from_admin(message,komu):
    text = message.text + '\n' + 'P.S. Admin'
    bot.send_message(komu, text)




def add_login(message):
    if len(message.text)<6:
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        text = 'Ваш логин слишком короткий (минимальное количество символов 6)'
        a = bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(a, add_login)
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id-1)
        add_login_and_id({'id_tg':str(message.chat.id)},message.text)
        a = bot.send_message(message.chat.id, 'Введите пароль (минимальное количество символов 6)')
        bot.register_next_step_handler(a, add_password)

def add_password(message):
    if len(message.text)<6:
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        text = 'Ваш пароль слишком короткий (минимальное количество символов 6)'
        a = bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(a, add_password)
    else:
        add_password1({'id_tg': f'{message.chat.id}'}, message.text)
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id-1)
        bot.send_message(message.chat.id, 'Выберите город/регион',reply_markup=chose_town())
def add_pic(message):
    if message.content_type == "photo":
        file_photo = bot.get_file(message.photo[-1].file_id)
        file_extension = os.path.splitext(file_photo.file_path)
        downl_file_photo = bot.download_file(file_photo.file_path)
        scr = 'downloads_photo_user/' + str(message.chat.id)+ file_extension[1]
        id_use = show_id({'id_tg': message.chat.id})
        save_foto_tg(id_use, scr)
        with open(scr,'wb') as new_file:
            new_file.write(downl_file_photo)
        check = analyze_image(scr)
        print(check)
        if check == 'запрещенка':
            bot.delete_message(message.chat.id, message.message_id - 1)
            bot.delete_message(message.chat.id, message.message_id)
            os.remove(scr)
            a = bot.send_message(message.chat.id, 'это плохие вещи попробуй заново')
            bot.register_next_step_handler(a, add_pic)
        else:
            bot.delete_message(message.chat.id, message.message_id - 1)
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id,'Хотите еще добавить фотографию в профиль?',reply_markup=add_pic_profil())

    else:
        a = bot.send_message(message.chat.id, 'Нужна фотография')
        bot.register_next_step_handler(a, add_pic)

def add_descr_profil(message):
    if message.content_type == "text":
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id-1)
        descr_text = message.text
        id_use = show_id({'id_tg' : message.chat.id})
        add_descriptiom(id_use, descr_text) #добавление описания в базу данных
        bot.send_message(message.chat.id, 'Введите диапазон вашего возраста',reply_markup=zakresy_lat())
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        a = bot.send_message(message.chat.id, 'Введите описание')
        bot.register_next_step_handler(a, add_descr_profil)

def add_plusy_profil(message):
    if message.content_type == "text":
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id-1)
        plusy = message.text
        id_use = show_id({'id_tg' : message.chat.id})
        add_plusy(id_use,plusy)  #вставляет плюсы в базу данных
        a = bot.send_message(message.chat.id, 'Введите Ваши отрицательные черты')
        bot.register_next_step_handler(a, add_minusy_profil)
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        a = bot.send_message(message.chat.id, 'Введите Ваши положительные качества')
        bot.register_next_step_handler(a, add_plusy_profil)

def add_minusy_profil(message):
    if message.content_type == "text":
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        minusy = message.text
        id_use = show_id({'id_tg' : message.chat.id})
        add_minusy(id_use,minusy) # вставляет плюсы в базу данных
        bot.send_message(message.chat.id, 'Укажите Ваш пол', reply_markup=male_female())
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        a = bot.send_message(message.chat.id, 'Введите Ваши отрицательные черты')
        bot.register_next_step_handler(a, add_minusy_profil)
def add_pic1(message):
    if message.content_type == "photo":
        file_photo = bot.get_file(message.photo[-1].file_id)
        file_extension = os.path.splitext(file_photo.file_path)
        downl_file_photo = bot.download_file(file_photo.file_path)
        scr = 'downloads_photo_user/' + str(message.chat.id) + '_1'+ file_extension[1]
        id_use = show_id({'id_tg': message.chat.id})
        save_foto_tg(id_use, scr)
        with open(scr, 'wb') as new_file:
            new_file.write(downl_file_photo)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Хотите еще добавить фотографию в профиль?', reply_markup=add_pic_profil1())

    else:
        a = bot.send_message(message.chat.id, 'Нужна фотография')
        bot.register_next_step_handler(a, add_pic1)

def add_pic2(message):
    if message.content_type == "photo":
        file_photo = bot.get_file(message.photo[-1].file_id)
        file_extension = os.path.splitext(file_photo.file_path)
        downl_file_photo = bot.download_file(file_photo.file_path)
        scr = 'downloads_photo_user/' + str(message.chat.id) + '_2'+ file_extension[1]
        id_use = show_id({'id_tg': message.chat.id})
        save_foto_tg(id_use, scr)
        with open(scr, 'wb') as new_file:
            new_file.write(downl_file_photo)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        a = bot.send_message(message.chat.id, 'Теперь опишите свои намерения на данной платформе')
        bot.register_next_step_handler(a, add_descr_profil)

    else:
        a = bot.send_message(message.chat.id, 'Нужна фотография')
        bot.register_next_step_handler(a, add_pic2)
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'registration':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        text = 'Введите логин (минимальное количество символов 6)'
        a = bot.send_message(call.message.chat.id, text)
        bot.register_next_step_handler(a, add_login)
    elif 'town' in call.data:
        a = call.data
        a = a.split(';')[1]
        add_place({'id_tg': call.message.chat.id}, a)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите,что хотите сделать", reply_markup=do_after_regostr())
    elif call.data =='Start_profil':
        text = 'Пришлите первую фотографию'
        bot.delete_message(call.message.chat.id, call.message.message_id)####
        a = bot.send_message(call.message.chat.id, text)
        bot.register_next_step_handler(a, add_pic)
    elif call.data == 'add_pic1':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        text = 'Пришлите вторую фотографию'
        a = bot.send_message(call.message.chat.id, text)
        bot.register_next_step_handler(a, add_pic1)
    elif call.data == 'add_pic2':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        text = 'Пришлите третью фотографию'
        a = bot.send_message(call.message.chat.id, text)
        bot.register_next_step_handler(a, add_pic2)
    elif call.data == 'stop_pic':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        a = bot.send_message(call.message.chat.id, 'Теперь опишите свои намерения на данной платформе')
        bot.register_next_step_handler(a, add_descr_profil)
    elif call.data == '18-25' or call.data == '25-40' or call.data == '40-55':
        zak = str(call.data)
        zak = zak.split('-')
        a1 = int(zak[0])
        a2 = int(zak[1])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите свой возраст", reply_markup=age18_25a(a1, a2))
    elif "age_count" in call.data:
        bot.delete_message(call.message.chat.id, call.message.message_id)###
        age = str(call.data)
        age = age.split()[1]
        print(age)
        id_use = show_id({'id_tg': call.message.chat.id})
        add_age(id_use,age) #добавление в базу данных
        a = bot.send_message(call.message.chat.id, 'Опишите ваши положительные черты')
        bot.register_next_step_handler(a, add_plusy_profil)
    elif call.data == 'show_my_profil':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        #формирование своей карточки на показ
        id_use = show_id({'id_tg': call.message.chat.id})
        list_of_photos = show_path_photos(id_use) #писок с фото
        if len(list_of_photos)>=2:
            info = show_info_profil(id_use)
            text_kart = f'❤️{info[6]},{info[3]}❤️\n🌏Локализация: {info[5]}\n📄Описание: {info[0]}\n➕Плюсы: {info[1]}\n➖Минусы: {info[2]}\n'
            media = []
            i = 0
            for photo in list_of_photos:
                if i == 0:
                    media.append(telebot.types.InputMediaPhoto(open(photo, 'rb'), caption=text_kart))
                    i+=1
                else:
                    media.append(telebot.types.InputMediaPhoto(open(photo, 'rb')))
                    i += 1
            bot.send_media_group(call.message.chat.id,
                                 media)
            bot.send_message(call.message.chat.id,"Прекрасный профиль",reply_markup=start_search())
        else: #если фотка всего одна
            info = show_info_profil(id_use)
            text_kart = f'{info[-1]},{info[3]}\nЛокализация: {info[4]}\nОписание: {info[0]}\nПлюсы:{info[1]}\nМинусы:{info[2]}\n'
            photo1 = open(list_of_photos[0], 'rb')
            bot.send_photo(call.message.chat.id, photo=photo1, caption=text_kart, reply_markup=start_search())

    elif call.data == 'girl' or call.data == 'boy':
        if call.data == 'girl':
            id_use = show_id({'id_tg': call.message.chat.id})
            add_gender(id_use, 1)
        else:
            id_use = show_id({'id_tg': call.message.chat.id})
            add_gender(id_use, 0)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Хотите начать поиск?", reply_markup=start_search())
    elif call.data == 'start_seerch':
        try:
            a = str(call.message.chat.id)
            del param_dict[a]
        except:
            pass
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите пол, который вас интересует", reply_markup=male_female_param())
    elif 'plec' in call.data:
        a = str(call.data).split()[1]
        mini_dict = {}
        mini_dict['women'] = a
        param_dict[str(call.message.chat.id)]=mini_dict
        print(param_dict)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите предпочительный диапазон возраста", reply_markup=zakresy_lat_param())
    elif 'laty' in call.data:
        a = str(call.data).split()[1]
        param_dict[str(call.message.chat.id)]['range_age'] = a
        print(param_dict)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите предпочительную локализацию", reply_markup=chose_town_param())
    elif 'TOWN' in call.data:
        print("Пошло на поиск города")
        a = str(call.data).split(';')[1]
        param_dict[str(call.message.chat.id)]['place'] = a
        print(param_dict)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вперед!",reply_markup=poisk())
    elif call.data == "GET_KART" or call.data == "GET_KART1" or call.data == "GET_KART2":
        stop = False
        reklama = is_acrive_add()
        #cчетчик
        if str(call.message.chat.id) in dict_for_add and reklama == True:
            a = dict_for_add[str(call.message.chat.id)] #берем кол-во кликов
            count_add = find_count_add() #проверка раз в какое кол-во идет реклама
            if a%count_add == 0:
                for x in range(4):
                    try:
                        bot.delete_message(call.message.chat.id, call.message.message_id-x)
                    except:
                        pass
                print("время рекламы")
                text = 'Реклама'
                id_use = show_id({'id_tg': call.message.chat.id}) #id для поиска рекламы
                for_del = []
                if id_use in name_aad_stp.keys():
                    for k,v in name_aad_stp[id_use].items():
                        if v>=2:
                            for_del.append(k)
                            n = find_id_add(k)
                            write_to_add_stp(id_use,n)

                    if for_del != []:
                        print(f'del - {for_del}')
                        for i in for_del:
                            del name_aad_stp[id_use][i]
                        for_del = []
                else:
                    name_aad_stp[id_use]={}

                if call.message.chat.id in last_add.keys():
                    ph_name = find_add2(id_use,last_add[call.message.chat.id])
                    last_add[call.message.chat.id] = ph_name
                    if ph_name in name_aad_stp[id_use].keys():
                        name_aad_stp[id_use][ph_name] += 1
                    else:
                        # name_aad_stp[id_use] = {}
                        # name_aad_stp[id_use][ph_name] = 1
                        name_aad_stp[id_use].setdefault(ph_name, 1)
                else:
                    ph_name = find_add2(id_use, "")
                    last_add[call.message.chat.id] = ph_name
                    if ph_name in name_aad_stp[id_use].keys():
                        name_aad_stp[id_use][ph_name] += 1
                    else:
                        # name_aad_stp[id_use] = {}
                        # name_aad_stp[id_use][ph_name] = 1
                        name_aad_stp[id_use].setdefault(ph_name, 1)
                photo1 = open(ph_name, 'rb')
                bot.send_photo(call.message.chat.id, photo=photo1, caption=text, reply_markup=add_keyb1())
                dict_for_add[str(call.message.chat.id)] +=1
                stop = True
                print(f'----{name_aad_stp[id_use]}-----')
            else:
                dict_for_add[str(call.message.chat.id)] += 1
        else:
            dict_for_add[str(call.message.chat.id)] = 1
            print("отсчет пошел")
        if call.data == "GET_KART1" and stop == False: #Удаление старого
            bot.delete_message(call.message.chat.id, call.message.message_id)
            try:
                bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            except:
                pass
            try:
                bot.delete_message(call.message.chat.id, call.message.message_id - 2)
            except:
                pass
            try:
                bot.delete_message(call.message.chat.id, call.message.message_id - 3)
            except:
                pass
        elif call.data == "GET_KART2" and stop == False:
            for i in range(1,6):
                try:
                    bot.delete_message(call.message.chat.id, call.message.message_id - i)
                except:
                    pass

        number = find_for_kartoczka(param_dict[str(call.message.chat.id)])
        print(number)
        if number != None and stop == False:
            list_of_photos = show_path_photos(number)  # писок с фото
            if len(list_of_photos) >= 2:
                info = show_info_profil(number)
                text_kart = f'❤️️{info[6]},{info[3]}❤️\n🌏Локализация: {info[5]}\n📄Описание: {info[0]}\n➕Плюсы: {info[1]}\n➖Минусы:{info[2]}\n'
                media = []
                i = 0
                for photo in list_of_photos:
                    if i == 0:
                        media.append(telebot.types.InputMediaPhoto(open(photo, 'rb'), caption=text_kart))
                        i += 1
                    else:
                        media.append(telebot.types.InputMediaPhoto(open(photo, 'rb')))
                        i += 1
                bot.send_media_group(call.message.chat.id,
                                     media)
                bot.send_message(call.message.chat.id, "Прекрасный профиль", reply_markup=what_do(str(number)))
            else:  # если фотка всего одна
                info = show_info_profil(number)
                text_kart = f'{info[-1]},{info[3]}\nЛокализация: {info[4]}\nОписание: {info[0]}\nПлюсы:{info[1]}\nМинусы:{info[2]}\n'
                photo1 = open(list_of_photos[0], 'rb')
                bot.send_photo(call.message.chat.id, photo=photo1, caption=text_kart, reply_markup=what_do(str(number)))
    elif "Like" in call.data:
        bot.answer_callback_query(call.id, "вы поставили лайк", show_alert=False)
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        except:
            pass
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id - 2)
        except:
            pass
        tgid_whom = str(call.data).split()[1]
        who = show_id({'id_tg': call.message.chat.id})
        who_whom_likes(who, tgid_whom)#запись в базу
        him_likes = does_he_like_me(tgid_whom) #проверка кого он лайкнул
        if str(who) in him_likes:
            name_sob = find_login(tgid_whom)
            itsmatch(who, tgid_whom)
            bot.send_message(call.message.chat.id, f"У вас взаимность с {name_sob} ☺️ ",reply_markup=dialog(tgid_whom))
        else:
            for x in range(6):
                try:
                    bot.delete_message(call.message.chat.id, call.message.message_id - x)
                except:
                    pass
            number = find_for_kartoczka(param_dict[str(call.message.chat.id)])
            print(number)
            if number != None:
                list_of_photos = show_path_photos(number)  # писок с фото
                if len(list_of_photos) >= 2:
                    info = show_info_profil(number)
                    text_kart = f'{info[6]},{info[3]}\nЛокализация: {info[5]}\nОписание: {info[0]}\nПлюсы:{info[1]}\nМинусы:{info[2]}\n'
                    media = []
                    i = 0
                    for photo in list_of_photos:
                        if i == 0:
                            media.append(telebot.types.InputMediaPhoto(open(photo, 'rb'), caption=text_kart))
                            i += 1
                        else:
                            media.append(telebot.types.InputMediaPhoto(open(photo, 'rb')))
                            i += 1
                    bot.send_media_group(call.message.chat.id,
                                         media)
                    bot.send_message(call.message.chat.id, "Прекрасный профиль", reply_markup=what_do(str(number)))
                else:  # если фотка всего одна
                    info = show_info_profil(number)
                    text_kart = f'{info[-1]},{info[3]}\nЛокализация: {info[4]}\nОписание: {info[0]}\nПлюсы:{info[1]}\nМинусы:{info[2]}\n'
                    photo1 = open(list_of_photos[0], 'rb')
                    bot.send_photo(call.message.chat.id, photo=photo1, caption=text_kart,
                                   reply_markup=what_do(str(number)))

    # elif "Dialog" in call.data: #функция для отпртавки сообщения
    #     who = show_id({'id_tg': call.message.chat.id})
    #     whom = str(call.data).split()[1]
    #     a = bot.send_message(call.message.chat.id, "Напишите свое перове сообщение")
    #     bot.register_next_step_handler(a, sending_message,who,whom) #кто отправляет whom кому отправляет
    elif "Answer" in call.data or "Dialog" in call.data:
        who = show_id({'id_tg': call.message.chat.id})
        # print(str(call.data).split()[1])
        whom = str(call.data).split()[1]
        a = bot.send_message(call.message.chat.id, "Напишите свое сообщение")
        bot.register_next_step_handler(a, sending_message, who, whom)
    elif "ProfilSob" in call.data:
        sobes = str(call.data).split()[1]
        list_of_photos = show_path_photos(sobes)  # писок с фото
        if len(list_of_photos) >= 2:
            info = show_info_profil(sobes)
            text_kart = f'{info[6]},{info[3]}\nЛокализация: {info[5]}\nОписание: {info[0]}\nПлюсы:{info[1]}\nМинусы:{info[2]}\n'
            media = []
            i = 0
            for photo in list_of_photos:
                if i == 0:
                    media.append(telebot.types.InputMediaPhoto(open(photo, 'rb'), caption=text_kart))
                    i += 1
                else:
                    media.append(telebot.types.InputMediaPhoto(open(photo, 'rb')))
                    i += 1
            bot.send_media_group(call.message.chat.id,
                                 media)
    elif 'Admin_answer' in call.data:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        komu = str(call.data).split()[1]
        a = bot.send_message(call.message.chat.id, "Напишите свое сообщение")
        bot.register_next_step_handler(a, answer_from_admin, komu)


print("Ready")
bot.infinity_polling()
