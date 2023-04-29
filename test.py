import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="1604", host="127.0.0.1")
cursor = conn.cursor()

conn.autocommit = True
# команда для создания базы данных metanit
sql = "CREATE DATABASE metanit"

# выполняем код sql
cursor.execute(sql)
print("База данных успешно создана")

cursor.close()
conn.close()













# def create_database(database_name, user, password, host, port):
#     """Создание базы данных"""
#     try:
#         # Установка соединения с PostgreSQL
#         conn = psycopg2.connect(
#             database="postgres",
#             user=user,
#             password=password,
#             host=host,
#             port=port
#         )
#
#         # Создание курсора
#         cur = conn.cursor()
#
#         # Создание базы данных
#         cur.execute(f"CREATE DATABASE {database_name}")
#
#         # Закрытие курсора и подтверждение изменений
#         cur.close()
#         conn.commit()
#
#         print(f"База данных {database_name} успешно создана")
#
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#
#     finally:
#         # Закрытие соединения
#         if conn is not None:
#             conn.close()
#
# # Пример использования
# create_database("mydatabase", "myuser", "mypassword", "localhost", "5432")