import csv
import os

import mysql.connector as mysql
import dotenv


dotenv.load_dotenv()

# Подключение к базе данных
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

# Загрузка данных из базы данных
cursor = db.cursor()
cursor.execute("SELECT name, second_name FROM students")
db_rows = cursor.fetchall()

# Создаем множество (set) для быстрого поиска
db_set = set((row[0], row[1]) for row in db_rows)

# Чтение CSV файла
csv_filename = '/Users/ez/Desktop/projects/Alya/homework/eugene_okulik/Lesson_16/data.csv'
csv_rows = []

with open(csv_filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # предполагается, что в CSV есть колонки 'Name' и 'last'
        name = row['Name'].strip()
        last = row['last'].strip()
        csv_rows.append((name, last))

# Находим записи из CSV, которых нет в базе
missing_in_db = [row for row in csv_rows if row not in db_set]

# Выводим результат
for name, second_name in missing_in_db:
    print(f"{name} {second_name}")

# закрываем соединение
db.close()