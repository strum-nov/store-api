import sqlite3
from db import db

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String)


    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.other = 'xxx'


    def json(self):
        return {'username':self.username,'password':self.password}


    #------------------ sqlalchemy handle

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def db_find_by_user(cls,name):
        return cls.query.filter_by(username=name).first()



    @classmethod
    def db_find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()



    #------------------ sqlite3 handle

    @classmethod
    def find_by_user(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query,(name,)) #(name,) 这是一个tuple 所以只有一个元素也要加 ,
        row = result.fetchone()

        if row:
            # user = cls(row[0],row[1],row[2])
            user = cls(*row) # 使用 *args 代替 row[0],row[1],row[2]
        else:
            user =None

        connection.close()
        return user



    @classmethod
    def find_by_id(cls,_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        cursor.execute(query,(_id,))
        row =  cursor.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user