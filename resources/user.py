import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Username are miss!"
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='Password are miss'
                        )


    def post(self):

        data = UserRegister.parser.parse_args()

        user = UserModel.db_find_by_user(data['username'])

        #如果用户存在就不再添加
        if user:
            return {'message':f"{data['username']} already exist"}

        user = UserModel(**data)
        #user = UserModel(data['username'],data['password'])

        user.save_to_db()

        '''
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'INSERT INTO users VALUES (NULL,?,?)'  #因为id是自增的 所有第一个row 参数传NULL
        cursor.execute(query,(data['username'],data['password']))

        connection.commit()
        connection.close()
        '''

        return {'message':'User create success'},201