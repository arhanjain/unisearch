from . import utils
import bcrypt
import jwt
import os
from datetime import datetime, timedelta
from .globals import table


def get_user(username):
    return table.get_item(Key={"username": username},
                          ProjectionExpression="password_hash")
def put_user(username, pw):
    return table.put_item(Item= {
        "username": username,
        "password_hash": bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
    })

def login(username, pw):
    if not (username and pw):
        return utils.build_response(401, message="Username and password required!")
    user = get_user(username)
    if not utils.check_200(user):
        return utils.build_response(402, message="Database interaction failed.")
    if not 'Item' in user:
        return utils.build_response(403, message="Login failed.")
    
    # check pw
    pw_hash = user["Item"]["password_hash"].encode("utf-8")
    if not bcrypt.checkpw(pw.encode("utf-8"), pw_hash):
        return utils.build_response(403, message="Login failed.")

    # create jwt
    payload = {"username": username,
               "exp": datetime.utcnow() + timedelta(hours=1)}
    token = jwt.encode(payload=payload,
                       key=os.environ['JWT_SECRET'],
                       algorithm="HS256",)
    
    return utils.build_response(200, username=username, token=token)
    

def register(username, pw):
    username, pw = username.strip(), pw.strip()
    if not (username and pw):
        return utils.build_response(401, message="Username and password required!")

    user = get_user(username)
    if not utils.check_200(user):
        return utils.build_response(402, message="Database interaction failed.")
    if 'Item' in user:
        return utils.build_response(401, message="User already exists!")

    res = put_user(username, pw)
    if not utils.check_200(res):
        return utils.build_response(402, message="Database interaction failed.")

    return utils.build_response(200, message="User creation successful!")