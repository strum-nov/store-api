from flask import Flask
from flask_restful import Resource,Api
from flask_jwt import JWT

from secret import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,ItemList
from resources.store import Store,StoreList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

#取消 跟踪所有字段改变 比如id username  ， 只要存储到database里才进行跟踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

app.secret_key = 'strumprivatekey'

''' 添加到 run.py
# heroku 注释   本地调试-》打开

@app.before_first_request
def create_tables():
    db.create_all()
'''

'''
db.create_all() 
1：会找到 resources import 的 Store
2: 而 Store中 from models.store import StoreModel
   会找到Model中的 StoreModel：
   
   class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    
   接下来找到 __tablename__ id name  于是就创建了 stores 表
   

'''


jwt = JWT(app,authenticate,identity)
#jwt 会自动创建 /auth 路由

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

# heroku 注释   本地调试-》打开
# if __name__ == '__main__':
    #如果允许的python文件是main 那么就启动flask
    #如果 app import 其他文件 __name__就不是 main 了


    # from db import db
    # db.init_app(app)
    # app.run(port=5000,debug=True)




