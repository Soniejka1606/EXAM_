import os
import sqlite3 as sl


"""
SELECT ('столбцы или * для выбора всех столбцов; обязательно')
FROM ('таблица; обязательно')
WHERE ('условие/фильтрация, например, city = 'Moscow'; необязательно')
GROUP BY ('столбец, по которому хотим сгруппировать данные; необязательно')
HAVING ('условие/фильтрация на уровне сгруппированных данных; необязательно')
ORDER BY ('столбец, по которому хотим отсортировать вывод; необязательно')
"""

con = sl.connect('DATATinder.db', check_same_thread=False)

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS Active (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            is_active BOOLEAN DEFAULT 1);
    """)

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS ADD_ (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            picture BLOB,
            women  BOOLEAN,
            age INTEGER);
    """)


with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS RegisterInfo (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            login TEXT,
            password TEXT,
            place TEXT,
            id_tg TEXT,
            id_vk TEXT,
            kart INTEGER);
    """)

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS PhotoProfil (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            picture BLOB,
            id_regis_user INTEGER);
    """)

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS Introducing (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            plusy TEXT ,
            minusy TEXT,
            age INTEGER,
            id_user INTEGER);
    """)

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS WhomLikes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            who TEXt,
            whom TEXt);
    """)

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS Itsamatch (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            person1 TEXt,
            person2 TEXt);
    """)
def search_id_tg():
    '''
    :return: список с айдишками телеги
    '''
    try:
        data = con.execute(f"SELECT id_tg FROM RegisterInfo")
        data = data.fetchall()
        user_id_tg = []
        for i in data:
            for k in i:
                user_id_tg.append(k)
        return user_id_tg
    except:
        return False
# print(search_id_tg())

def search_id_vk():
    '''
    :return: список с айдишками телеги
    '''
    try:
        data = con.execute(f"SELECT id_vk FROM RegisterInfo")
        data = data.fetchall()
        user_id_tg = []
        for i in data:
            for k in i:
                user_id_tg.append(k)
        return user_id_tg
    except:
        return False
# print(search_id_vk())
def add_login_and_id(dict_,login):
    '''
    :param dict_: словрь типа {id_tg : 55255}, "login"
    :param login: создает начало регистрации
    :return:
    '''
    if "id_tg" in dict_.keys():
        try:
            sql_insert = f"INSERT INTO RegisterInfo (id_tg,login) values(?,?)"
            with con:
                con.execute(sql_insert, (dict_['id_tg'], login))
        except Exception as e:
            return print(e)
    else:
        try:
            sql_insert = f"INSERT INTO RegisterInfo (id_vk,login) values(?,?)"
            with con:
                con.execute(sql_insert, (dict_['id_vk'], login))
        except Exception as e:
            return print(e)



def add_place(dict_,place):
    '''
    :param dict_: словрь типа {id_tg : 55255}, "login"
    :param login: добавляет место
    :return:
    '''
    if "id_tg" in dict_.keys():
        try:
            sql_insert = f"UPDATE  RegisterInfo SET place = ? WHERE id_tg = ?"
            with con:
                con.execute(sql_insert, (place,dict_['id_tg']))
        except Exception as e:
            return print(e)
    else:
        try:
            sql_insert = f"UPDATE RegisterInfo SET place = ? WHERE id_vk = ?"
            with con:
                con.execute(sql_insert, (place,dict_['id_vk']))
        except Exception as e:
            return print(e)
# add_place({'id_tg' : '598388419'},'БРЕСТ')

def add_password1(dict_,password):
    '''
    :param dict_: словрь типа {id_tg : 55255}, "login"
    :param login: добавляет место
    :return:
    '''
    if "id_tg" in dict_.keys():
        try:
            sql_insert = f"UPDATE  RegisterInfo SET password = ? WHERE id_tg = ?"
            with con:
                con.execute(sql_insert, (password,dict_['id_tg']))
        except Exception as e:
            return print(e)
    else:
        try:
            sql_insert = f"UPDATE RegisterInfo SET password = ? WHERE id_vk = ?"
            with con:
                con.execute(sql_insert, (password,dict_['id_vk']))
        except Exception as e:
            return print(e)

# add_password({'id_tg' : '598388419'},'БРЕСТ1')

def show_id(dict_):
    '''
    :param dict_: словрь типа {id_tg : 55255},
    :return: находит айди этого человека
    '''
    if "id_tg" in dict_.keys():
        try:
            data = con.execute(f"SELECT id FROM RegisterInfo WHERE id_tg = {dict_['id_tg']}")
            data = data.fetchall()
            id_ = 0
            for i in data:
                for k in i:
                    id_= k
            return id_
        except:
            return False
    else:
        try:
            data = con.execute(f"SELECT id FROM RegisterInfo WHERE id_vk = {dict_['id_vk']}")
            data = data.fetchall()
            id_ = 0
            for i in data:
                for k in i:
                    id_= k
            return id_
        except:
            return False
# print(show_id({'id_tg' : '598388419'}))

def add_descriptiom(id_user,text):
    '''
    :param id_user: берет айдишку зарегистрированного пользователя
    :param text: текст с описание
    :return:
    '''
    try:
        sql_insert = f"INSERT INTO Introducing  (description,id_user) values(?,?)"
        with con:
            con.execute(sql_insert, (text, id_user))
    except Exception as e:
        return print(e)
# print(add_descriptiom(26,"text-descriptiom"))
def add_age(id_user,age):
    rg_ge = ""
    if int(age)>=18 and int(age)<=25:
        rg_ge = '18-25'
    elif int(age)>=26 and int(age)<=40:
        rg_ge = '25-40'
    else:
        rg_ge = '40-55'
    try:
        sql_insert = f"UPDATE Introducing SET age = ?,range_age = ? WHERE id_user = ?"
        with con:
            con.execute(sql_insert, (age,rg_ge, id_user))
    except Exception as e:
        return print(e)
    try:
        sql_insert = f"UPDATE RegisterInfo SET range_age = ? WHERE id = ?"
        with con:
            con.execute(sql_insert, (rg_ge, id_user))
    except Exception as e:
        return print(e)

# print(add_age(27,38))

def add_plusy(id_user,plusy):
    '''
    :param id_user:
    :param plusy:
    :return: вставляет в базу данных положительные качества
    '''
    try:
        sql_insert = f"UPDATE Introducing SET plusy = ? WHERE id_user = ?"
        with con:
            con.execute(sql_insert, (plusy, id_user))
    except Exception as e:
        return print(e)

# print(add_plusy(26,"very good"))

def add_minusy(id_user,minusy):
    '''
    :param id_user:
    :param minusy:
    :return: вставляет в таблицу отрицательные качества
    '''
    try:
        sql_insert = f"UPDATE Introducing SET minusy = ? WHERE id_user = ?"
        with con:
            con.execute(sql_insert, (minusy, id_user))
    except Exception as e:
        return print(e)

# print(add_minusy(26,"not good"))

def add_gender(id_user,liczba):
    '''
    :param id_user:
    :param minusy: принисает один или ноль
    :return: вставляет в таблицу отрицательные качества
    '''
    try:
        sql_insert = f"UPDATE RegisterInfo SET women = ? WHERE id = ?"
        with con:
            con.execute(sql_insert, (liczba, id_user))
    except Exception as e:
        return print(e)
# print(add_gender(26,1))

def save_foto_tg(id,photo):
    try:
        sql_insert = f"INSERT INTO PhotoProfil  (picture,id_regis_user) values(?,?)"
        with con:
            con.execute(sql_insert, (photo, id))
    except Exception as e:
        return print(e)
# print(save_foto_tg(26,"598388419.jpg"))

def show_path_photos(id):
    try:
        data = con.execute(f"SELECT picture FROM PhotoProfil WHERE id_regis_user = {id}")
        data = data.fetchall()
        list_photos = []
        for i in data:
            for k in i:
                list_photos.append(k)
        return list_photos
    except:
        return False
# print(show_path_photos(26))

def show_info_profil(id):
    '''
    :param id: айди зарегестрированного пользователя
    :return: список с информацией первое описание потом плюсы минусы возраст и область и логин инфо
    '''
    try:
        data = con.execute(f"SELECT * FROM Introducing WHERE id_user = {id}")
        data = data.fetchall()
        list_= []
        for i in data:
            for k in i:
                list_.append(k)
        list_ = list_[1:-1]
        # return list_
    except Exception as e:
        return e
    try:
        data = con.execute(f"SELECT place,login FROM RegisterInfo WHERE id = {id} ")
        data = data.fetchall()
        list_.append(data[0][0])
        list_.append(data[0][1])
        return list_
    except Exception as e:
        return e
# print(show_info_profil(32))

def find_for_kartoczka(dict_):
    '''
    {'plec': '1', 'laty': '25-40', 'town': 'Гомельская область'}
    берет словарь со значениями нужными как выше и ищет айди нужного человека случайное
    :return: id из таблицы зарегистрированного юзера
    '''
    values = list(dict_.values())
    count_none = values.count("None")

    if count_none == 3:
        try:
            data = con.execute("SELECT id_user FROM Introducing ORDER BY RANDOM() LIMIT 1")
            data = data.fetchall()
            if data:
                return data[0][0]
            else:
                return None
        except Exception as e:
            return None

    condition = 'WHERE '
    conditions = []
    for key, value in dict_.items():
        if value != "None":
            conditions.append(f"{key} = '{value}'")

    condition += ' AND '.join(conditions)

    try:
        query = f"SELECT id FROM RegisterInfo {condition} ORDER BY RANDOM() LIMIT 1"
        data = con.execute(query)
        data = data.fetchall()
        if data:
            return data[0][0]
        else:
            return None
    except Exception as e:
        return None
# print(find_for_kartoczka({'women': '0', 'range_age': '40-55', 'place': 'Минск'}))
# print(find_for_kartoczka({'plec': 'None', 'laty': 'None', 'town': 'None'}))

def find_for_kartoczka1(dict_):
    '''
    {'plec': '1', 'laty': '25-40', 'town': 'Гомельская область'}
    берет словарь со значениями нужными как выше и ищет айди нужного человека случайное
    :return: id из таблицы зарегистрированного юзера
    '''
    k_values = list(dict_.values())
    count_none = k_values.count("None")

    if count_none == 3:
        try:
            data = con.execute("SELECT id_user FROM Introducing ORDER BY RANDOM() LIMIT 1")
            data = data.fetchall()
            if data:
                return data[0][0]
            else:
                return None
        except Exception as e:
            return None

    elif count_none == 1:
        condition = 'WHERE '
        for key, value in dict_.items():
            if value != "None":
                condition += f'{key} = \'{value}\' AND '

        condition = condition[:-5]  # Удаляем последний "AND"
        try:
            data = con.execute(f"SELECT id FROM RegisterInfo {condition} ORDER BY RANDOM() LIMIT 1")
            data = data.fetchall()
            if data:
                return data[0][0]
            else:
                return None
        except Exception as e:
            return None

    elif count_none == 2 or count_none == 0:
        for key, value in dict_.items():
            if value != "None":
                try:
                    data = con.execute(f"SELECT id FROM RegisterInfo WHERE {key} = '{value}' ORDER BY RANDOM() LIMIT 1")
                    data = data.fetchall()
                    if data:
                        return data[0][0]
                    else:
                        return None
                except Exception as e:
                    return None


# Примеры использования
print(find_for_kartoczka1({'women': '0', 'range_age': '40-55', 'place': 'Минск'}))
# print(find_for_kartoczka({'plec': 'None', 'laty': 'None', 'town': 'None'}))


def who_whom_likes(who,whom):
    '''
    :param who: id кто лайкнул
    :param whom: айфди кого лайкнул
    :return: запписывает в таблицу
    '''
    try:
        sql_insert = f"INSERT INTO WhomLikes (who,whom) values(?,?)"
        with con:
            con.execute(sql_insert, (who,whom))
    except Exception as e:
        return print(e)

# print(who_whom_likes(2,1))

def does_he_like_me(id_need_user):
    '''
    :param id_need_user:
    :return: дает список кого лойкнул тот или иной человек
    '''
    try:
        data = con.execute(f"SELECT whom FROM WhomLikes WHERE who = {id_need_user}")
        data = data.fetchall()
        ids = []
        for i in data:
            for k in i:
                ids.append(k)
        if len(ids) == 0:
            return []
        return set(ids)
    except Exception as e:
        return None
# print(does_he_like_me(33))

def itsmatch(person1,person2):
    '''
        добавляет взаимность
    '''
    try:
        sql_insert = f"INSERT INTO Itsamatch (person1,person2) values(?,?)"
        with con:
            con.execute(sql_insert, (person1,person2))
    except Exception as e:
        return print(e)

# print(itsmatch(2,1))

def find_tg_id(id):
    '''
    :param id_need_user:
    :return: айди тг
    '''
    try:
        data = con.execute(f"SELECT id_tg FROM RegisterInfo WHERE id = {id}")
        data = data.fetchall()
        ids = data[0][0]
        return ids
    except Exception as e:
        return None
# print(find_tg_id(44))

def find_login(id):
    '''
    :param id_need_user:
    :return: login тг
    '''
    try:
        data = con.execute(f"SELECT login FROM RegisterInfo WHERE id = {id}")
        data = data.fetchall()
        ids = data[0][0]
        return ids
    except Exception as e:
        return None

# print(find_login(40))

def find_count_add():
    '''
    :param id_need_user:
    :return: ищет раз в сколько кликов должна попасться реклама
    '''
    try:
        data = con.execute(f"SELECT add_count FROM Active WHERE id = 1")
        data = data.fetchall()
        ids = data[0][0]
        return int(ids)
    except Exception as e:
        return None

# print(find_count_add())

def find_add(id):
    '''
    :param id:
    :return: находит нужную рекламу для человек
    '''
    #ПОиск возраста и пола
    try:
        data = con.execute(f"SELECT range_age FROM Introducing WHERE id_user = {id}")
        data = data.fetchall()
        range_age = data[0][0]
    except Exception as e:
        return None
    try:
        data = con.execute(f"SELECT women FROM RegisterInfo WHERE id = {id}")
        data = data.fetchall()
        women = data[0][0]
    except Exception as e:
        return None
    try:
        data = con.execute(f"SELECT picture FROM ADD_ WHERE women = '{women}' AND age = '{range_age}' ORDER BY RANDOM() LIMIT 1")
        data = data.fetchall()
        return data[0][0]
    except Exception as e:
        return None

# print(find_add(62))

#-----------------vk
def registration_vk(dict_):
    # регистрация в вк
    try:
        sql_insert = f"INSERT INTO RegisterInfo (login,password,place,id_vk,women,range_age) values(?,?,?,?,?,?)"
        with con:
            con.execute(sql_insert, (dict_['name'], dict_['password'],dict_['town'],dict_['vk_id'],dict_['women'],dict_['range_age']))
    except Exception as e:
        return print(e)
    # поиск последнего добавленного пользователя
    try:
        id_user = con.execute(f"SELECT id FROM RegisterInfo WHERE id_vk={dict_['vk_id']} ORDER BY id DESC LIMIT 1")
        id_user = id_user.fetchall()
        for i in id_user:
            for k in i:
                id_user = k
    except:
        return False
    try:
        sql_insert = f"INSERT INTO Introducing (id_user,age,range_age) values(?,?,?)"
        with con:
            con.execute(sql_insert, (id_user,dict_['age'],dict_['range_age']))
    except Exception as e:
        return print(e)
#print(registration_vk({'name': 'Skxkxkxixxkxkx', 'vk_id': 153883425, 'password': 'Cjkckckckc', 'women': '0', 'town': 'Минск', 'age': '19', 'range_age': '18-25'}

def find_id_using_vk_id(id):
    '''
    :param id_vk:
    :return: находит айди регистрации
    '''
    try:
        data = con.execute(f"SELECT id FROM RegisterInfo WHERE id_vk = {id}")
        data = data.fetchall()
        ids = data[0][0]
        return ids
    except Exception as e:
        return None
# print(find_id_using_vk_id(153883425))

def add_descriptiom_vk(id_user,text):
    '''
    :param id_user: берет айдишку зарегистрированного пользователя
    :param text: текст с описание
    :return:
    '''
    try:
        sql_insert = f"UPDATE Introducing SET description = ? WHERE id_user = ?"
        with con:
            con.execute(sql_insert, (text, id_user))
    except Exception as e:
        return print(e)

# print(add_descriptiom(26,"text-descriptiom"))

def find_tg_or_vk(id):
    '''
    :param id: айди регистрации
    :return: находит айли вк или тг
    '''
    vk = False
    try:
        data = con.execute(f"SELECT id_tg FROM RegisterInfo WHERE id = {id}")
        data = data.fetchall()
        ids = data[0][0]
    except Exception as e:
        ids == None
    if ids == None:
        try:
            data = con.execute(f"SELECT id_vk FROM RegisterInfo WHERE id = {id}")
            data = data.fetchall()
            ids = data[0][0]
            vk = True
        except Exception as e:
            ids == None
    if vk == True:
        ids = [ids,"vk"]
    else:
        ids = [ids,"tg"]
    return ids

# print(find_tg_or_vk(62))



def write_to_add_stp(id_user,name_add):
    '''
    :param id_user: id регистрации пользователя
    :param name_add: имя рекламы
    :return: записывает в таблицу какие рекламы нельзя показывать пользователю
    '''
    try:
        sql_insert = f"INSERT INTO stop_add (id_reg_user,name_add) values(?,?)"
        with con:
            con.execute(sql_insert, (id_user,name_add))
    except Exception as e:
        return print(e)

# print(write_to_add_stp(12,"name_add"))

def find_id_add(name_add):
    try:
        data = con.execute(f"SELECT id FROM ADD_ WHERE picture = '{str(name_add)}'")
        data = data.fetchall()
        data = data[0][0]
        return data
    except Exception as e:
        print(e)
# print(find_id_add('ADD_pictures/5ADD.jpg'))

def is_acrive_add():
    '''
    :return: проверяет активна ли реклама или нет
    '''
    try:
        data = con.execute(f"SELECT is_active FROM active WHERE id = 1")
        data = data.fetchall()
        data = data[0][0]
        if data == 1:
            return True
        elif data == 0:
            return False
    except Exception as e:
        print(e)

# print(is_acrive_add())

def change_active(t):
    '''
    :return: изменяет значение на актив или не актив
    '''
    try:
        # print(id_)
        com = f"UPDATE active SET is_active = ? WHERE id = ?"
        with con:
            con.execute(com, (t,1))
    except Exception as e:
        print(e)
# print(change_active(True))

def is_count_add():
    '''
    :return: частоту появления рекламы
    '''
    try:
        data = con.execute(f"SELECT add_count FROM active WHERE id = 1")
        data = data.fetchall()
        data = data[0][0]
        return data
    except Exception as e:
        print(e)

# print(is_count_add())

def change_count_add(count):
    '''
    :return: изменяет значение на актив или не актив
    '''
    try:
        # print(id_)
        com = f"UPDATE active SET add_count = ? WHERE id = ?"
        with con:
            con.execute(com, (count,1))
    except Exception as e:
        print(e)
# print(change_count_add(5))

def reklama_in_table(list_):
    '''
    :return: Добавляет все в таблицу
    list_for_table = [photo_to_table, women, age, max_views, descr]
    '''
    list_=tuple(list_)
    try:
        sql_insert = f"INSERT INTO ADD_ (picture,women,age, max_views, descr) values(?,?,?,?,?)"
        with con:
            con.execute(sql_insert, list_)
    except Exception as e:
        return print(e)
# print(reklama_in_table(['Add_pictures/heart.jpg', 1, '18-25', '5', 'лорпа']))

def info_table_add():
    '''
    :return: дает инфу с реламы
    '''
    list_table = []
    try:
        data = con.execute(f"SELECT id,picture,max_views,descr,views,is_work  FROM ADD_")
        data = data.fetchall()

        for i in data:
            a = []
            for k in range(6):
                a.append(i[k])
            list_table.append(a)

        return list_table
    except Exception as e:
        print(e)

# print(info_table_add())

def otmena_add(id,count):
    '''
    :return: изменяет значение на актив или не актив
    '''
    try:
        # print(id_)
        com = f"UPDATE ADD_ SET is_work = ? WHERE id = ?"
        with con:
            con.execute(com, (count,id))
    except Exception as e:
        print(e)
# print(otmena_add(1,0))

def find_add2(id,photo):
    '''
    :param id:
    :return: находит нужную рекламу для человек находит рекламу исходя из количеств просмотров
    '''
    list_of_stop_add = []
    #Поиск ненужной реламы отдается список айди
    try:
        data = con.execute(f"SELECT name_add FROM stop_add WHERE id_reg_user = {id}")
        data = data.fetchall()
        for i in data:
            if i[0]!=None:
                list_of_stop_add.append(i[0])
    except Exception as e:
        pass
    # print(list_of_stop_add)
    if photo != '':
        try:
            data = con.execute(f"SELECT id FROM ADD_ WHERE picture = '{photo}'")
            data = data.fetchall()
            id_stop_photo = data[0][0]
            print(id_stop_photo)
        except Exception as e:
            pass
    else:
        id_stop_photo = None

    if id_stop_photo!= None and list_of_stop_add !=[] :
        list_of_stop_add = list(map(int, list_of_stop_add))
        list_of_stop_add.append(id_stop_photo)
        list_of_stop_add = tuple(list_of_stop_add)
        print(list_of_stop_add)
    elif id_stop_photo!= None and list_of_stop_add ==[]:
        list_of_stop_add.append(id_stop_photo)
        list_of_stop_add = tuple(list_of_stop_add)
        print(list_of_stop_add)
    elif id_stop_photo == None and list_of_stop_add!=[]:
        list_of_stop_add = list(map(int, list_of_stop_add))
        list_of_stop_add = tuple(list_of_stop_add)
        print(list_of_stop_add)
    else:
        list_of_stop_add.append(0)
        list_of_stop_add = tuple(list_of_stop_add)
        print(list_of_stop_add)
    # ПОиск возраста и пола
    try:
        data = con.execute(f"SELECT range_age FROM Introducing WHERE id_user = {id}")
        data = data.fetchall()
        range_age = data[0][0]
        print(f'Возраст{range_age}')
    except Exception as e:
        return None
    try:
        data = con.execute(f"SELECT women FROM RegisterInfo WHERE id = {id}")
        data = data.fetchall()
        women = data[0][0]
        print(f'Пол {women}')
    except Exception as e:
        return None

    try:
        placeholders = ','.join('?' * len(list_of_stop_add))
        data = "SELECT picture FROM ADD_ WHERE views < max_views AND women = ? AND age = ? AND is_work = ? AND id NOT IN ({}) ORDER BY RANDOM() LIMIT 1".format(
            placeholders)
        params = [women, range_age, 1] + list(list_of_stop_add)  # Преобразование кортежа в список
        cursor = con.execute(data, params)
        data = cursor.fetchall()
        reklama = data[0][0]
        print(f'reklama {reklama}')
    except Exception as e:
        reklama ='ADD_pictures/my.jpg'

    try:
        com = f"UPDATE ADD_ SET views = views + 1 WHERE picture = ?"
        with con:
            con.execute(com, (reklama,))
        # print("добавился просмотр")
    except Exception as e:
        print(e)
    return reklama

# print(find_add2(64,"Add_pictures/photo_2023-06-19_12-43-46.jpg"))

def add_max_views(id,count):
    '''
    :return: добавляет макс просмотров
    '''
    try:
        # print(id_)
        com = f"UPDATE ADD_ SET max_views = max_views + ? WHERE id = ?"
        with con:
            con.execute(com, (count,id))
    except Exception as e:
        print(e)
# print(add_max_views(1,1))