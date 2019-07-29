
from flask_restful import Resource,reqparse
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(),200

        return {'message':"store cant find '{}' ".format(name)},400



    def post(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message': "store '{}' already exist ".format(name)}, 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'message': "an server error occurred"}, 500

        return store.json(),200


    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message','delete success'},200




class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}