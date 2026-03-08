import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("SELECT * FROM marks top1")
print(cursor.fetchall())

cursor.execute(f'''
select *
from students s
join `groups` g on s.group_id=g.id
where g.title='BGPA_107227' and s.name='Ivan' and s.second_name='Petrov'
''')
print(cursor.fetchall())

cursor.execute(f'''
select *
from students s
join `groups` g on s.group_id=g.id
where g.title='GR_O222' and s.name='Petr' and s.second_name='Ivanov'
''')
print(cursor.fetchall())


db.close()