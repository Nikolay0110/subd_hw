import psycopg2
from password import password


class Base:
    def __init__(self, database, user, password):
        self.client_db = database
        self.postgres = user
        self.password = password

    def create_db(self, conn):
        conn = psycopg2.connect(database=self.client_db, user=self.postgres, password=self.password)
        with conn.cursor() as cur:
            sql = 'CREATE DATABASE client_db'
            cur.execute(sql)
            print('База данных успешно создана')

            cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(60) NOT NULL,
                last_name VARCHAR(60) NOT NULL,
                email VARCHAR(60) NOT NULL);
            ''')

            cur.execute('''
            CREATE TABLE IF NOT EXISTS phone (
                id SERIAL PRIMARY KEY,
                number_1 VARCHAR(11),
                number_2 VARCHAR(11),
                number_3 VARCHAR(11),
                number_4 VARCHAR(11),
                number_5 VARCHAR(11),
                number_6 VARCHAR(11),
                number_7 VARCHAR(11),
                number_8 VARCHAR(11),
                number_9 VARCHAR(11),
                number_10 VARCHAR(11));
            ''')

            cur.execute('''
            CREATE TABLE IF NOT EXISTS client_phone (
                id SERIAL PRIMARY KEY	,
                user_id integer REFERENCES users(id),
                phone_id INTEGER REFERENCES phone(id));
            ''')
        conn.close()

    create_db()

#
# import subprocess
#
# cmd = "date" # Здесь вместо date Ваша команда для git
#
# returned_output = subprocess.check_output(cmd) # returned_output содержит вывод в виде строки байтов
#
# print('Результат выполнения команды:', returned_output.decode("utf-8")) # Преобразуем байты в строку


# def add_client(conn, first_name, last_name, email, phones=None):
#     pass
#
#
# def add_phone(conn, client_id, phone):
#     pass
#
#
# def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
#     pass
#
#
# def delete_phone(conn, client_id, phone):
#     pass
#
#
# def delete_client(conn, client_id):
#     pass
#
#
# def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
#     pass
#
#
# with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
#     pass  # вызывайте функции здесь
#
# conn.close()
