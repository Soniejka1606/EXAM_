import datetime
import os
import requests
import vk_api
from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
from keyb_vk import *

from DATABASE import *
GROUP_ID = '219364686'
GROUP_TOKEN = 'vk1.a.QTSvYwYIGmfz5_ArnSV2oTR5huKn3q6WMihaJGgqKGHld1VbQDJQBJyJy98spHmmW0DYlpvS9C92A8OnnEVETV1rOggZS31H0Iz_XIVxFnZh69lwJdLn2eZsgJ8u2sdnjTZbgKAC3d9uRqi-0fp_89WuRJTJbU83w31KBONTF21XCzXqEk1QSrOv1Y3347zubaxf9NEa5XHwh24X0eeY8Q'
API_VERSION = '5.120'

settings1 = dict(one_time=False, inline=False)
settings2 = dict(one_time=False, inline=True)

admin = '134828772'
vk_session = VkApi(token=GROUP_TOKEN, api_version=API_VERSION)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk)
longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)



def send_messege(id_user,text,ot_kogp):
    vk.messages.send(
        user_id=id_user,
        random_id=get_random_id(),
        peer_id=id_user,
        message=text,
        keyboard=answer(ot_kogp).get_keyboard())