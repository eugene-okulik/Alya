import csv
import os

import mysql.connector as mysql
import dotenv

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.csv')
homework_path = os.path.dirname(os.path.dirname(base_path))
# print(homework_path)
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_16', 'hw_data', 'data.csv')
# print(eugene_file_path)

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
cursor.execute(f'''
select s.name, s.second_name, g.title, b.title, sub.title, l.title, m.value
from students s
join `groups` g on s.group_id=g.id
join books b on s.id=b.taken_by_student_id
join marks m on s.id=m.student_id
join lessons l on m.lesson_id=l.id
join subjects sub on l.subject_id=sub.id
''')
db_rows = cursor.fetchall()

# Создаем множество (set) для быстрого поиска
db_set = set((row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in db_rows)

# Чтение CSV файла
csv_filename = '/Users/ez/Desktop/projects/Alya/homework/eugene_okulik/Lesson_16/hw_data/data.csv'
csv_rows = []

with open(csv_filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # предполагается, что в CSV есть колонки
        name = row['name'].strip()
        second_name = row['second_name'].strip()
        group_title = row['group_title'].strip()
        book_title = row['book_title'].strip()
        subject_title = row['subject_title'].strip()
        lesson_title = row['lesson_title'].strip()
        mark_value = row['mark_value'].strip()
        csv_rows.append((name, second_name, group_title, book_title, subject_title, lesson_title, mark_value))

# Находим записи из CSV, которых нет в базе
missing_in_db = [row for row in csv_rows if row not in db_set]

# Выводим результат
for name, second_name, group_title, book_title, subject_title, lesson_title, mark_value in missing_in_db:
    print(f"{name} {second_name} {group_title} {book_title} {subject_title} {lesson_title} {mark_value}")

# закрываем соединение
db.close()
