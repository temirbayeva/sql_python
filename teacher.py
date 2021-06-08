import datetime.date
import psycopg2
from  psycopg2 import sql
conn= psycopg2.connect(dbname="decode_python", user="decode_user", 
                       password="password", host="localhost")

cursor=conn.cursor()

# Create table
cursor.execute("""
                CREATE TABLE teacher(id SERIAL, name VARHAR, experience_id VARHAR(255), 
                    adress_id VARHAR(255))
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
        ('1', 'Filimonova A.A', datetime.date.now(), '5 years', 'Abai street 25'),
        ('2', 'Temirbayeva A.A', datetime.date.now(), '2 year', 'Auezova street 67'),
        ('3', 'Abenova B.S', datetime.date.now(), '10 years', 'Mametova street 54'), 
    ]
    insert = sql.SQL('INSERT INTO teacher(name, experience_id, adress_id  ) VALUES {}').format(
    sql.SQL(',').join(map(sql.literal, values))  
    )
    cursor.execute(insert)