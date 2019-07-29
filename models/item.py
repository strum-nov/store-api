
import sqlite3

from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2)) #精度为小数点后2位

    # stores.id 就是  id = db.Column(db.Integer, primary_key=True)
    #store_id 的 外键是 stores 表中的 id 而这个id 是 store的主键
    # stores.id 就是  items表的外键
    # stores.id 的外键必须唯一
    store_id = db.Column(db.Integer,db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id


    def json(self):
        return {'name':self.name,'price':self.price,'store_id':self.store_id}


    #根据name 查询 item
    @classmethod
    def finditem_by_name(cls,name):

        '''
               connection = sqlite3.connect('data.db')
               cursor = connection.cursor()
               query = 'SELECT * FROM items WHERE name=?'

               result = cursor.execute(query, (name,))
               item = result.fetchone()
               if item:
                   return cls(*item)
               return None
        '''
        # return ItemModel.query.filter_by(name=name)  #SELECT * FROM __tablename__ WHERE name = ? 返回的可能是多个
        # return ItemModel.query.filter_by(name=name).first() # item = result.fetchone() SELECT * FROM __tablename__ WHERE name = ? LIMIT 1
        return cls.query.filter_by(name=name).first() # item = result.fetchone() SELECT * FROM __tablename__ WHERE name = ? LIMIT 1



    def save_to_db(self):
        '''
         session : is a collection of objects 一个collection对象
                    we going to write to the database
                    we can add multiple objects to the session
                    
         add 包括upate
        '''
        db.session.add(self)
        db.session.commit()



    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


#------------------  sqlite handle ------------

    # 插入item
    def insetItem(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(query, (self.name, self.price))
        connection.commit()  # 保存的时候 才需要commit
        connection.close()


    #更新item
    def updateItem(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'UPDATE items SET price=? WHERE name=?'
        cursor.execute(query, (self.price, self.name))
        connection.commit()  # 保存的时候 才需要commit
        connection.close()
        pass



    #根据name删除item
    @classmethod
    def deleteItem(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'DELETE FROM items WHERE name=?'
        cursor.execute(query, (name,))
        connection.commit()  # 保存的时候 才需要commit
        connection.close()
        pass



    #获取所有的 items
    @classmethod
    def getAllItems(cls):

        '''
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        rows = cursor.execute(query)

        items = []
        for row in rows:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()
        '''
        return {'items': [ item.json() for item in ItemModel.query.all()]}
        # return {'items':list(map(lambda x:x.json(),ItemModel.query.all()))}











