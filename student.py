import datetime

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="a1s2s3e4m5a6",
    database="decode"
)
cursor = conn.cursor()

import pdb
pdb.set_trace()
# Create table
cursor.execute("""
                CREATE TABLE student(id SERIAL, name VARHAR, course_id VARHAR(255), 
                    record book_id VARHAR(255))
                             """)
conn.commit()

# ALTER TABLE
cursor.execute("""
                ALTER TABLE book
                ADD COLUMN url varhar(255), 
                             """)

with conn.cursor() as cursor:
    conn.autokommit=True
    values=[
        ('1', 'Galeev Alan', datetime.date.now(), '2', '00001'),
        ('2', 'Utebaev Vlad', datetime.date.now(), '2', '00002'),
        ('3', 'Zolotko Aleksandr', datetime.date.now(), '3', '00003'), 
    ]
    insert = sql.SQL('INSERT INTO student(name,course_id, record book_id ) VALUES {}').format(
    sql.SQL(',').join(map(sql.literal, values))  
    )
    cursor.execute(insert)