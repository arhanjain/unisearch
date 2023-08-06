import json

def build_response(code, **kwargs):

    return {
        "statusCode": code,
        "body": json.dumps(kwargs)
    }