import json
import os
import jwt
from jwt.exceptions import ExpiredSignatureError

def build_response(code, **kwargs):

    return {
        "statusCode": code,
        "body": json.dumps(kwargs)
    }

def check_200(response):
    return response['ResponseMetadata']['HTTPStatusCode'] == 200

def check_keys(keys, d):
    return all(key in d for key in keys)

def verify_token(token):
    try:
        return jwt.decode(
                token,
                key=os.environ["JWT_SECRET"],
                algorithms=[jwt.get_unverified_header(token)['alg']]
            )
    except ExpiredSignatureError as err:
        return None
    
    