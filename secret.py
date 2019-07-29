
from werkzeug.security import safe_str_cmp

from models.user import UserModel

def authenticate(username,password):
    #user = username_mapping.get(username,None) #效果跟 ["username"],但是会返回默认值 如果set中没有找打key,就会返回None
    # if user and user.password == password:
    user = UserModel.db_find_by_user(username)
    if user and safe_str_cmp(user.password,password):
        print(user.json())
        return user


def identity(payload):
    print('payload-:')
    print(payload)
    #{'exp': 1563777182, 'iat': 1563776882, 'nbf': 1563776882, 'identity': 3}
    user_id = payload['identity']
    # return userid_mapping.get(user_id,None)
    return UserModel.db_find_by_id(user_id)


