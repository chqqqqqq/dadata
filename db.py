import sqlite3


#Создание таблицы со значениями по умолчанию в БД
def create_table():
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        drop_table_query = '''DROP TABLE IF EXISTS user_settings;'''
        create_table_query = '''CREATE TABLE user_settings 
                                (url TEXT, api_key TEXT, language TEXT);'''
        insert_table_query = '''INSERT INTO user_settings
                                (url, language)
                                VALUES
                                ("https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address", "ru");'''
        cursor.execute(drop_table_query)
        cursor.execute(create_table_query)
        cursor.execute(insert_table_query)
        connection.commit()
        cursor.close()
    finally:
        if connection:
            connection.close()

#Получение значений из таблицы в БД
def select_all():
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        get_table_query = '''SELECT * from user_settings;'''
        cursor.execute(get_table_query)
        data = cursor.fetchall()[0]
        cursor.close()
        return data
    finally:
        if connection:
            connection.close()

#Обновление значений таблицы в БД
def update_all(settings):
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        update_table_query = '''UPDATE user_settings SET url = ?, api_key = ?, language = ?;'''
        data = settings
        cursor.execute(update_table_query, data)
        connection.commit()
        cursor.close()
    finally:
        if connection:
            connection.close()