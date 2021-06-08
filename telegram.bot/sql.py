import datetime.date
import psycopg2
from  psycopg2 import sql
conn= psycopg2.connect(dbname="decode_python", user="decode_user", 
                       password="password", host="localhost")

cursor=conn.cursor()

# Create table
cursor.execute("""
                CREATE TABLE book(id SERIAL, name VARHAR, author_id VARHAR(255), 
                    added DATE, book_author VARHAR(255))
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
        ('Book 1', '14545432', datetime.date.now(), 'Author 1'),
        ('Book 2', '14545432', datetime.date.now(), 'Author 1'),
        ('Book 3', '14545432', datetime.date.now(), 'Author 1'), 
    ]
    insert = sql.SQL('INSERT INTO book(name,author_id, added, book_author) VALUES {}').format(
    sql.SQL(',').join(map(sql.literal, values))  
    )
    cursor.execute(insert)
     