import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field price cannot be left blank"
                        )

    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="This field store_id cannot be left blank"
                        )

    # 在调用get路由之前 先判断用户登录状态是否正确
    @jwt_required()
    def get(self,name): #xxxx/student/strum
        item = ItemModel.finditem_by_name(name)
        if item:
            return item.json(),201
        return {'message':f'not find {name} item'},404



    @jwt_required()
    def post(self,name):
        item = ItemModel.finditem_by_name(name)
        if item is not None:
            return {'message':"an item with name '{}' already exists ".format(name)},400
        else:
            data = Item.parser.parse_args()
            # n_item = {'name':name,'price':data['price']}
            n_item = ItemModel(name,data['price'],data['store_id'])

            try:
                # ItemModel.insertItem(n_item)
                # n_item.insertItem()
                n_item.save_to_db()
            except:
                return {'message':'500 server error occured'},500

            return n_item.json(),201



    @jwt_required()
    def delete(self,name):
        item = ItemModel.finditem_by_name(name)
        if item is None:
            return {'message':f'item {name} is not exist'},400
        try:
            # ItemModel.deleteItem(name)
            item.delete_from_db()
        except:
            return {'message':'500 server error occured'},500

        return {'message':f'Item {name} deleted'},200




    @jwt_required()
    def put(self,name):
        data = Item.parser.parse_args()
        # n_item = {'name': name, 'price': data['price']}
        # n_item = ItemModel(name,data['price'])
        item = ItemModel.finditem_by_name(name)

        if item is None:
            try:
                item = ItemModel(name,data['price'],data['store_id'])
                # ItemModel.insertItem(n_item)
                # n_item.insertItem()
                item.save_to_db()
            except:
                return {'message':'500 server error occured'},500
        else:
            try:
                 # ItemModel.updateItem(n_item)
                 item.price = data['price']
                 item.save_to_db()
            except:
                return {'message':'500 server error occured'},500

        return item.json()






class ItemList(Resource):
    def get(self):
        items = ItemModel.getAllItems()
        return items
