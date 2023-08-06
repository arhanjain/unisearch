import json
import bcrypt
import register
import asyncio

def lambda_handler(event, context):
    loop = asyncio.get_event_loop()

    res = None
    match event['path']:
        case '/health':
            pass
        case '/register':
            res = loop.run_until_complete(register.register("arhan!", "jain!"))
        case _:
            res ={
                'statusCode': 200,
                'body': json.dumps('Hello from Lambda!')
            }


    return res 

if __name__ == '__main__':
    event = {
        'path': '/register',
    }
    r = lambda_handler(event, None)
    print(r)