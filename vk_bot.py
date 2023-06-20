import datetime
import os
import requests
import vk_api
from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json

import cenzura
from keyb_vk import *

from DATABASE import *
from send_to_vk import send_messege
from sent_to_tg import sending_message_vk

# GROUP_ID = '219364665'
# GROUP_TOKEN = 'vk1.a.Udr_3z5uGE0H0VcDsiUrnxXt8YXuiYaQZPdLIYC1YrzbFTxRZvvelbhTEFiB0-0cdRJ21Xy2M31lVbaXR3HWI0AWBQz74S0p8cjDs1A2BM6DGzIcirs90Jw0kyp2sbFuDkecVixcmfEY4FbN01pD7MR6520v-GN5Zfzm8GpP4xbaDPsC7IBlszgiaLxLo65XLAzAAp4Efm-tBI-N4n9mbQ'
# API_VERSION = '5.120'

GROUP_ID = '219364686'
GROUP_TOKEN = 'vk1.a.QTSvYwYIGmfz5_ArnSV2oTR5huKn3q6WMihaJGgqKGHld1VbQDJQBJyJy98spHmmW0DYlpvS9C92A8OnnEVETV1rOggZS31H0Iz_XIVxFnZh69lwJdLn2eZsgJ8u2sdnjTZbgKAC3d9uRqi-0fp_89WuRJTJbU83w31KBONTF21XCzXqEk1QSrOv1Y3347zubaxf9NEa5XHwh24X0eeY8Q'
API_VERSION = '5.120'

settings1 = dict(one_time=False, inline=False)
settings2 = dict(one_time=False, inline=True)

admin = '134828772'

"""Все id"""

id_all_dict = []
state_list = {}
reg_dict = {}
param = {}
dict_for_add = {}
dict_to_write = {}


last_add = {}

name_aad_stp = {}
def all_id():
    global id_all_dict
    id_all_dict = search_id_vk()
def upload_photo(photo):
    response = upload.photo_messages(photo)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return f'photo{owner_id}_{photo_id}_{access_key}'

all_id()
HI = ["start", "Start", "начать", "Начало", "Начать", "начало", "Бот", "бот", "Старт", "старт", "скидки", "Скидки"]

# Основное меню
""" Клавиатура меню"""






state_list = {}
state_profil = {}


# Запускаем бот
vk_session = VkApi(token=GROUP_TOKEN, api_version=API_VERSION)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk)
longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)

CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app', 'text', 'callback')

reser = ['запустить бота', 'меню', 'заказать', 'запустить бота', 'help', 'Зарегистрироваться!', 'HELP']



def upload_photo(photo):
    response = upload.photo_messages(photo)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return f'photo{owner_id}_{photo_id}_{access_key}'


print('Ready VK')

for event in longpoll.listen():
    # print(event)
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.message['text'] != '':
            user_id = event.obj.message['from_id']
            if event.from_user:
                if event.obj.message['text']:
                    user_id = event.obj.message['from_id']
                    if str(user_id) not in id_all_dict:
                        try:
                            if len(state_list[user_id]) > 0 and 'st3' in state_list[user_id]:
                                print('ljofghjh---')
                                if 55>=int(event.obj.message['text'])>=18:
                                    reg_dict[user_id].setdefault('age', event.obj.message['text'])
                                    age = int(event.obj.message['text'])
                                    #поиск диапазона возраста
                                    rg_ge = ""
                                    if int(age) >= 18 and int(age) <= 25:
                                        rg_ge = '18-25'
                                    elif int(age) >= 26 and int(age) <= 40:
                                        rg_ge = '25-40'
                                    else:
                                        rg_ge = '40-55'
                                    reg_dict[user_id].setdefault('range_age', rg_ge)
                                    print(reg_dict[user_id])
                                    registration_vk(reg_dict[user_id]) # добавление в базу данных
                                    state_list[user_id].clear()
                                    reg_dict[user_id].clear()
                                    #после регистрации добавляем его в список зарегистрированных
                                    all_id()
                                    state_profil[user_id] = ['photo1']
                                    vk.messages.send(
                                        user_id=event.obj.message['from_id'],
                                        random_id=get_random_id(),
                                        peer_id=event.obj.message['from_id'],
                                        message=f"Поздравляем вы зарегистрировались, для создания профиля нажмите на 'Создать профиль'",
                                        keyboard=create_profil().get_keyboard())
                                else:
                                    vk.messages.send(
                                        user_id=event.obj.message['from_id'],
                                        random_id=get_random_id(),
                                        peer_id=event.obj.message['from_id'],
                                        message=f"Вы некорректно ввели возраст. \n Попробуйте снова")
                            elif len(state_list[user_id]) > 0 and 'st2' in state_list[user_id]:
                                #записывает пароль и предлагает выбрать пол
                                reg_dict[user_id].setdefault('password', event.obj.message['text'])
                                vk.messages.send(
                                    user_id=event.obj.message['from_id'],
                                    random_id=get_random_id(),
                                    peer_id=event.obj.message['from_id'],
                                    message=f"Ваш пароль {event.obj.message['text']}. \n Выберите пол",
                                    keyboard=women_men().get_keyboard()
                                )

                            elif len(state_list[user_id]) > 0 and 'st1' in state_list[user_id]:
                                if event.obj.message['text'] not in reser:
                                    reg_dict[user_id] = {'name': event.obj.message['text']}
                                    reg_dict[user_id].setdefault('vk_id', user_id)
                                    state_list[user_id].append('st2')
                                    print(reg_dict)
                                    vk.messages.send(
                                        user_id=event.obj.message['from_id'],
                                        random_id=get_random_id(),
                                        peer_id=event.obj.message['from_id'],
                                        message=f"Ваш логин {event.obj.message['text']}\n Введите пароль"
                                        )
                                else:
                                    vk.messages.send(
                                        user_id=event.obj.message['from_id'],
                                        random_id=get_random_id(),
                                        peer_id=event.obj.message['from_id'],
                                        message=f"Вы некорректно ввели логин. \n Попробуйте снова"
                                        )
                        except:
                            if event.obj.message['text'] == 'Зарегистрироваться!':
                                vk.messages.send(
                                    user_id=event.obj.message['from_id'],
                                    random_id=get_random_id(),
                                    peer_id=event.obj.message['from_id'],
                                    message=f"Введите логин.",
                                    keyboard=keyboard_1.get_keyboard())
                                state_list[user_id] = ['st1']
                            elif event.obj.message['text'] == 'HELP':
                                vk.messages.send(
                                    user_id=event.obj.message['from_id'],
                                    random_id=get_random_id(),
                                    peer_id=event.obj.message['from_id'],
                                    message='Краткий текст помощи')
                            elif event.obj.message['text'] and str(user_id) not in id_all_dict:
                                print(id_all_dict)
                                vk.messages.send(
                                    user_id=event.obj.message['from_id'],
                                    random_id=get_random_id(),
                                    peer_id=event.obj.message['from_id'],
                                    message='Здравствуйте вам надо зарегистрироваться, нажмите на кнопку "Зарегистрироваться!"',
                                    keyboard=keyboard_1.get_keyboard())



                    elif event.obj.message['text'] == '/описание' and state_profil[user_id] != ['photo1']:
                        state_profil[user_id] = ['desc']
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            peer_id=event.obj.message['from_id'],
                            message=f"Цель Ваших знакомсв")

                    elif event.obj.message['text'] and user_id in state_profil.keys() and state_profil[user_id] == ['desc']:
                        id_user_reg = find_id_using_vk_id(event.obj.message['from_id'])# находим айди регистрации
                        add_descriptiom_vk(id_user_reg, event.obj.message['text']) #записываем данные
                        state_profil[user_id] = ['plusy']
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            peer_id=event.obj.message['from_id'],
                            message=f"Опишите Ваши положительные качества")
                    elif event.obj.message['text'] and user_id in state_profil.keys() and state_profil[user_id] == ['plusy']:
                        id_user_reg = find_id_using_vk_id(event.obj.message['from_id'])# находим айди регистрации
                        add_plusy(id_user_reg, event.obj.message['text'])
                        state_profil[user_id] = ['minusy']
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            peer_id=event.obj.message['from_id'],
                            message=f"Опишите Ваши отрицательные качества")
                    elif event.obj.message['text'] and user_id in state_profil.keys() and state_profil[user_id] == ['minusy']:
                        id_user_reg = find_id_using_vk_id(event.obj.message['from_id'])# находим айди регистрации
                        add_minusy(id_user_reg, event.obj.message['text'])
                        state_profil[user_id] = ['the_end']
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            peer_id=event.obj.message['from_id'],
                            message=f"Внизу можете начать поиск либо посмотреть свою карточку",
                            keyboard=start_search_or_show_my_profil().get_keyboard())
                    elif event.obj.message['text'] == 'Посмотреть мой профиль':
                        id_user_reg = find_id_using_vk_id(event.obj.message['from_id'])# находим айди регистрации
                        list_of_photos = show_path_photos(id_user_reg) #показывает список с фото
                        info = show_info_profil(id_user_reg)
                        text_kart = f'{info[6]},{info[3]}\nЛокализация: {info[5]}\nОписание: {info[0]}\nПлюсы:{info[1]}\nМинусы:{info[2]}\n'
                        photo_urls = []
                        for i in list_of_photos:
                            ph = upload_photo(i)
                            photo_urls.append(ph)
                        attachments = ','.join(photo_urls)
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            peer_id=event.obj.message['from_id'],
                            attachment=attachments,
                            message=text_kart,
                            keyboard=start_search_or_show_my_profil().get_keyboard())
                    elif event.obj.message['text'] == 'Начать поиск':
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            peer_id=event.obj.message['from_id'],
                            message="Выберите какой пол Вас интересует",
                            keyboard=chose_women().get_keyboard())
                    elif user_id in dict_to_write:
                        pr = str(event.obj.message['text'])
                        a = cenzura.cenzura1(pr)
                        if a == False:
                            vk.messages.send(
                                user_id=event.obj.message['from_id'],
                                random_id=get_random_id(),
                                peer_id=event.obj.message['from_id'],
                                message="сообщение не прошло цензуру попробуйте еще")
                        else:
                            # dict_to_write[user_id_vk] = [who,whom] так выглядит словарь
                            proverka = find_tg_or_vk(dict_to_write[user_id_vk][1])
                            if proverka[1]=="tg":
                                print("проверку на тг прошло")
                                text = event.obj.message['text']
                                try:
                                    whom = find_tg_id(dict_to_write[user_id_vk][1])#кому
                                    who = dict_to_write[user_id_vk][0]#от кого
                                    sending_message_vk(text,who,whom)
                                except Exception as e:
                                    print(e)
                            if proverka[1] == "vk":
                                text = event.obj.message['text']
                                send_messege(proverka[0], text, dict_to_write[user_id_vk][0])
                                #proverka[0] = id_vk, dict_to_write[user_id_vk][0] = id_reg
                                # vk.messages.send(
                                #     user_id=event.obj.message['from_id'],
                                #     random_id=get_random_id(),
                                #     peer_id=event.obj.message['from_id'],
                                #     message=event.obj.message['text'],
                                #     keyboard=answer(dict_to_write[user_id_vk][0]).get_keyboard())
                            del dict_to_write[user_id_vk]

        elif event.obj.message['attachments'] and state_profil[user_id][0] in ['photo1','photo2','photo3']:
            # print(state_profil[user_id])
            # print('ПРИШЛО ФОТО')
            # Получение информации о фотографии
            user_id = event.obj.message['from_id']
            # Выбираем наибольший размер фотографии
            photo_url = event.obj.message['attachments'][0]['photo']['sizes'][-1]['url']
            file_names = os.listdir('downloads_photo_user')  # cписок фото в папке
            user_id_name = user_id
            response = requests.get(photo_url)
            if response.status_code == 200:
                if state_profil[user_id] == ['photo1']:
                    user_id_name = user_id

                elif state_profil[user_id] == ['photo2']:
                        user_id_name = str(user_id_name) + '_1'
                elif state_profil[user_id] == ['photo3']:
                    user_id_name = str(user_id_name) + '_2'
                if state_profil[user_id] == ['photo1']:
                    state_profil[user_id] = ['photo2']
                elif state_profil[user_id] == ['photo2']:
                    state_profil[user_id] = ['photo3']
                elif state_profil[user_id] == ['photo3']:
                    state_profil[user_id] = ['photo4']
                with open(f'downloads_photo_user/{user_id_name}.jpg', 'wb') as file:
                    file.write(response.content)
                print('Фотография сохранена')
                id_user_reg = find_id_using_vk_id(event.obj.message['from_id'])
                save_foto_tg(id_user_reg, f'downloads_photo_user/{user_id_name}.jpg')
            else:
                print('Не удалось загрузить фотографию')
    elif event.type == VkBotEventType.MESSAGE_EVENT:
        #print(event)

        if event.object.payload.get('type') in CALLBACK_TYPES:
            vk.messages.sendMessageEventAnswer(
                event_id=event.object.event_id,
                user_id=event.object.user_id,
                peer_id=event.object.peer_id,
                event_data=json.dumps(event.object.payload))
        elif event.object.payload.get('type') == 'указать пол':
            reg_dict[user_id].setdefault('women', event.object.payload.get('women'))
            last_id = vk.messages.edit(
                peer_id=event.obj.peer_id,
                message=f"Выберите город",
                conversation_message_id=event.obj.conversation_message_id,
                keyboard=towns_keyb().get_keyboard())
        elif event.object.payload.get('type') == 'Город':
            #записываю город человека
            reg_dict[user_id].setdefault('town', event.object.payload.get('town'))
            print(reg_dict)
            state_list[user_id].append('st3')
            last_id = vk.messages.edit(
                peer_id=event.obj.peer_id,
                message=f"Укажите свой возраст от 18-55",
                conversation_message_id=event.obj.conversation_message_id)
        elif event.object.payload.get('type') == 'help':
            last_id = vk.messages.edit(
                peer_id=event.obj.peer_id,
                message=f"Справочная информация по регистрации",
                conversation_message_id=event.obj.conversation_message_id)
        elif event.obj.payload.get('type') == 'Создать профиль':
            user_id_vk = event.object['user_id']
            state_profil[user_id_vk] = ['photo1']
            last_id = vk.messages.edit(
                peer_id=event.obj.peer_id,
                message=f"Пришлите фотографии по порядку до трех фото, после добавления кнопок введите '/описание'",
                conversation_message_id=event.obj.conversation_message_id,
                keyboard=desc_1.get_keyboard())

        elif event.obj.payload.get('type') == 'выбрать пол':
            user_id_vk = event.object['user_id']
            param[user_id_vk] = {}
            param[user_id_vk]['women'] = event.obj.payload.get('women')
            last_id = vk.messages.edit(
                peer_id=event.obj.peer_id,
                message=f"Выберите интересующий Вас диапазон",
                conversation_message_id=event.obj.conversation_message_id,
                keyboard=chose_diapazon().get_keyboard())
        elif event.obj.payload.get('type') == 'выбрать диапазон':
            user_id_vk = event.object['user_id']
            param[user_id_vk]['range_age'] = event.obj.payload.get('range_age')
            last_id = vk.messages.edit(
                peer_id=event.obj.peer_id,
                message=f"Выберите интересующий Вас город",
                conversation_message_id=event.obj.conversation_message_id,
                keyboard=choice_towns_keyb().get_keyboard())
        elif event.obj.payload.get('type') == 'Город выбор':
            user_id_vk = event.object['user_id']
            param[user_id_vk]['place'] = event.obj.payload.get('town')
            last_id = vk.messages.edit(
                peer_id=event.obj.peer_id,
                message=f"Нажмите чтобы начать поиск",
                conversation_message_id=event.obj.conversation_message_id,
                keyboard=start().get_keyboard())
        elif event.obj.payload.get('type') == 'Поиск собеседника' or event.obj.payload.get('type') == 'Следующий':
            stop = False
            reklama = is_acrive_add()

            user_id_vk = event.object['user_id']
            # print(user_id_vk)
            if str(user_id_vk) in dict_for_add and reklama == True:
                a = dict_for_add[str(user_id_vk)]  # берем кол-во кликов
                count_add = find_count_add()  # проверка раз в какое кол-во идет реклама
                if a % count_add == 0:
                    # print("время рекламы")
                    text = 'Реклама'
                    id_user_reg = find_id_using_vk_id(int(user_id_vk))# id для поиска рекламы
                    # ph_name = find_add(id_user_reg)
                    #----вставака рекламы
                    for_del = []
                    if id_user_reg in name_aad_stp.keys():
                        for k, v in name_aad_stp[id_user_reg].items():
                            if v >= 2:
                                for_del.append(k)
                                n = find_id_add(k)
                                write_to_add_stp(id_user_reg, n)

                        if for_del != []:
                            print(f'del - {for_del}')
                            for i in for_del:
                                del name_aad_stp[id_user_reg][i]
                            for_del = []
                    else:
                        name_aad_stp[id_user_reg] = {}

                    if user_id_vk in last_add.keys():
                        print(f'прошлая реклама {last_add[user_id_vk]}')
                        ph_name = find_add2(id_user_reg, last_add[user_id_vk])
                        last_add[user_id_vk] = ph_name
                        if ph_name in name_aad_stp[id_user_reg].keys():
                            name_aad_stp[id_user_reg][ph_name] += 1
                        else:
                            # name_aad_stp[id_use] = {}
                            # name_aad_stp[id_use][ph_name] = 1
                            name_aad_stp[id_user_reg].setdefault(ph_name, 1)
                    else:
                        ph_name = find_add2(id_user_reg, "")
                        last_add[user_id_vk] = ph_name
                        if ph_name in name_aad_stp[id_user_reg].keys():
                            name_aad_stp[id_user_reg][ph_name] += 1
                        else:
                            # name_aad_stp[id_use] = {}
                            # name_aad_stp[id_use][ph_name] = 1
                            name_aad_stp[id_user_reg].setdefault(ph_name, 1)
                    # ----вставака рекламы
                    last_id = vk.messages.edit(
                        peer_id=event.obj.peer_id,
                        attachment=upload_photo(ph_name),
                        message=text,
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=add_next().get_keyboard())
                    dict_for_add[str(user_id_vk)] += 1
                    stop = True
                else:
                    dict_for_add[str(user_id_vk)] += 1
            else:
                dict_for_add[str(user_id_vk)] = 1
                # print("отсчет пошел")
            user_id_vk = event.object['user_id']
            txt = str(param[user_id_vk])
            number = find_for_kartoczka(param[user_id_vk]) #поиск человека
            if number != None and stop == False:
                list_of_photos = show_path_photos(number)
                info = show_info_profil(number)
                text_kart = f'{info[6]},{info[3]}\nЛокализация: {info[5]}\nОписание: {info[0]}\nПлюсы:{info[1]}\nМинусы:{info[2]}\n'
                photo_urls = []
                for i in list_of_photos:
                    ph = upload_photo(i)
                    photo_urls.append(ph)
                attachments = ','.join(photo_urls)
                last_id = vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    attachment=attachments,
                    message=text_kart,
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=scroll(number).get_keyboard())
        elif event.obj.payload.get('type') == 'like':
            try:
                user_id_vk = event.object['user_id']
                who = find_id_using_vk_id(int(user_id_vk))
                whom = event.obj.payload.get('like_who')
                who_whom_likes(who, whom)  # запись в базу
                him_likes = does_he_like_me(whom)  # проверка кого он лайкнул
                if str(who) in him_likes:
                    name_sob = find_login(whom)
                    itsmatch(who, who)
                    text_s = f"У вас взаимность с {name_sob} "
                    vk.messages.send(
                        peer_id=event.obj.peer_id,
                        random_id=get_random_id(),
                        message=text_s,
                        keyboard=write_to_sob(whom).get_keyboard()
                    )
                else:
                    vk.messages.send(
                        peer_id=event.obj.peer_id,
                        random_id=get_random_id(),
                        message="вы поставили лайк можете продолжать поиск"
                        )


            except Exception as e:
                print(e)
        elif event.obj.payload.get('type') == 'Профиль собеседника':
            him_id = event.obj.payload.get('him_id')
            list_of_photos = show_path_photos(him_id)  # показывает список с фото
            info = show_info_profil(him_id)
            text_kart = f'{info[6]},{info[3]}\nЛокализация: {info[5]}\nОписание: {info[0]}\nПлюсы:{info[1]}\nМинусы:{info[2]}\n'
            photo_urls = []
            for i in list_of_photos:
                ph = upload_photo(i)
                photo_urls.append(ph)
            attachments = ','.join(photo_urls)
            vk.messages.send(
                peer_id=event.obj.peer_id,
                random_id=get_random_id(),
                attachment=attachments,
                message=text_kart,
            )
        elif event.obj.payload.get('type') == 'Написать соб':
            user_id_vk = event.object['user_id']
            who = find_id_using_vk_id(int(user_id_vk))#мой айди
            whom = event.obj.payload.get('him_id')#кому айди
            dict_to_write[user_id_vk] = [who,whom] # создаем состояние для написания
            name_sob = find_login(whom)
            vk.messages.send(
                peer_id=event.obj.peer_id,
                random_id=get_random_id(),
                message=f"напишите сообщение {name_sob}"
            )




