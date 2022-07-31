import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv()


mydb = mysql.connect(
    host=os.environ.get('host'),
    user=os.environ.get('name'),
    password=os.environ.get('password'),
    database=os.environ.get('database')
)

conn = mydb.cursor()

# conn.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# conn.execute("SHOW TABLES")

# for table in conn:
#     print(table)

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#     ("John", "Street 231"),
#     ("Jake", "Street 45645"),
#     ("James", "Street kjl"),
# ]

# conn.executemany(sql, val)

# mydb.commit()


# print(conn.rowcount)


# conn.execute("SELECT * FROM customers")

# data = conn.fetchall()
# data = conn.fetchone()


# print(data)
# for row in data:
#     with open('data.txt', 'a') as f:
#         row_data = "name: {}, address: {} \n".format(row[0], row[1])
#         f.write(row_data)








# print(mydb)
# mycursor.execute("CREATE DATABASE newdb")
# mycursor.execute("SELECT * FROM PERSON WHERE id=2")


# import models 

# # class Person(models)
# #     name = databasefield
# #     age = int 
# #     address = text field


# obj = Person.objects.get(name='john')

# obj.name 
# obj.address 

# print(mydb)

