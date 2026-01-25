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
cursor.execute("INSERT INTO students (name, second_name) VALUES ('Alya2', 'Zhydok2')")
student_id = cursor.lastrowid
# cursor.execute(f'SELECT * from students where id = {student_id}')
# print(cursor.fetchone())

# create books
query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [
        ('my_book1', student_id),
        ('my_book2', student_id)
    ]
cursor.executemany(query, values)
# cursor.execute(f'SELECT * from books where taken_by_student_id = {student_id}')
# print(cursor.fetchall())

# create group
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('my_group1', '01-09-2025', '31-05-2026')")
gr_id = cursor.lastrowid
# cursor.execute(f'SELECT * from `groups` where id = {gr_id}')
# print(cursor.fetchone())

# update student
cursor.execute("UPDATE students SET group_id = %s where id = %s", (gr_id, student_id))
# cursor.execute(f'SELECT * from students where id = {student_id}')
# print(cursor.fetchall())

# create subject1
cursor.execute("INSERT INTO subjects (title) VALUES ('geography_1')")
subject1_id = cursor.lastrowid
# cursor.execute(f'SELECT * from subjects where id = {subject1_id}')
# print(cursor.fetchone())

# create subject2
cursor.execute("INSERT INTO subjects (title) VALUES ('geography_2')")
subject2_id = cursor.lastrowid
# cursor.execute(f'SELECT * from subjects where id = {subject2_id}')
# print(cursor.fetchone())

# create lesson1
query1 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = [
        ('lesson1', subject1_id)
    ]
cursor.executemany(query1, values)
lesson1_id = cursor.lastrowid

# create lesson2
query2 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = [
        ('lesson2', subject1_id)
    ]
cursor.executemany(query2, values)
lesson2_id = cursor.lastrowid
# cursor.execute(f'SELECT * from lessons where subject_id = {subject1_id}')
# print(cursor.fetchall())

# create lesson3
query3 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = [
        ('lesson3', subject2_id)
    ]
cursor.executemany(query3, values)
lesson3_id = cursor.lastrowid

# create lesson4
query4 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = [
        ('lesson4', subject2_id)
    ]
cursor.executemany(query4, values)
lesson4_id = cursor.lastrowid
# cursor.execute(f'SELECT * from lessons where subject_id = {subject2_id}')
# print(cursor.fetchall())

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
