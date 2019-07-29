import sqlite3


connection = sqlite3.connect('data.db')

#cursor ： 光标
cursor = connection.cursor()

create_table = 'CREATE TABLE IF NOT EXISTS users (id int, username text ,password text)'

cursor.execute(create_table)

user = (1,'josn','asdf')

insert_query = "INSERT INTO users VALUES (?,?,?)"

cursor.execute(insert_query,user)


users = [
    (2,'josn','asdf'),
    (3,'josn','asdf')
]

cursor.executemany(insert_query,users)


select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

"""
(1, 'josn', 'asdf')
(2, 'josn', 'asdf')
(3, 'josn', 'asdf')
"""

connection.commit()

connection.close()