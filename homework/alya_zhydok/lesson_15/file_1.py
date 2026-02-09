import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
# create student
query_student = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
values = ('Alya', 'Zhydok')
cursor.execute(query_student, values)
student_id = cursor.lastrowid
cursor.execute('SELECT * FROM students WHERE id = %s', (student_id,))
print(cursor.fetchone())
# create books
query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [
    ('my_book1', student_id),
    ('my_book2', student_id)
]
cursor.executemany(query, values)
# create group
query_group = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('my_group1', '01-09-2025', '31-05-2026')
cursor.execute(query_group, values)
gr_id = cursor.lastrowid
cursor.execute('SELECT * FROM `groups` WHERE id = %s', (gr_id,))
print(cursor.fetchone())
# update student
cursor.execute("UPDATE students SET group_id = %s where id = %s", (gr_id, student_id))
# create subjects


def create_subject(cursor, title):
    query_subject = "INSERT INTO subjects (title) VALUES (%s)"
    cursor.execute(query_subject, (title,))
    subject_id = cursor.lastrowid
    cursor.execute('SELECT * FROM subjects WHERE id = %s', (subject_id,))
    return subject_id, cursor.fetchall()


subject1_id, result1 = create_subject(cursor, 'geography_1')
print(result1)
subject2_id, result2 = create_subject(cursor, 'geography_2')
print(result2)
# create lesson


def create_lesson(cursor, title, subject_id):
    query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
    cursor.execute(query, (title, subject_id))
    lesson_id = cursor.lastrowid
    return lesson_id


lesson1_id = create_lesson(cursor, 'lesson1', subject1_id)
lesson2_id = create_lesson(cursor, 'lesson2', subject1_id)
lesson3_id = create_lesson(cursor, 'lesson3', subject2_id)
lesson4_id = create_lesson(cursor, 'lesson4', subject2_id)
# set marks
# insert into marks (value, lesson_id, student_id) values (9, 12729, 21304)
insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        (8, lesson1_id, student_id),
        (9, lesson2_id, student_id),
        (7, lesson3_id, student_id),
        (10, lesson4_id, student_id)
    ]
)
# answer
cursor.execute(f'SELECT * from marks where student_id = {student_id}')
print(cursor.fetchall())
cursor.execute(f'SELECT * from books where taken_by_student_id = {student_id}')
print(cursor.fetchall())
cursor.execute(f'''
select *
from students s
join books b on s.id=b.taken_by_student_id
join `groups` g on s.group_id=g.id
join marks m on s.id=m.student_id
join lessons l on m.lesson_id=l.id
join subjects sub on l.subject_id=sub.id
where s.id= {student_id}
''')
print(cursor.fetchall())
db.commit()

db.close()
