import json
import time
import helpers.paper_tracker as paper_tracker
import helpers.utils as utils
import helpers.account as account
import asyncio

def lambda_handler(event, context):
    # loop = asyncio.get_event_loop()

    match event['path']:
        case '/register':
            if not utils.check_keys(["username", "password"], event):
                return utils.build_response(401, message="Username and password required!") 
            return account.register(event["username"], event["password"])

        case '/login':
            if not utils.check_keys(["username", "password"], event):
                return utils.build_response(401, message="Username and password required!") 
            return account.login(event["username"], event["password"])

        case '/add_papers' | '/remove_papers' | '/get_papers':
            if not utils.check_keys(["token"], event):
                return utils.build_response(401, message="Missing fields.")
            
            # verify token
            decoded_payload = utils.verify_token(event["token"])
            if decoded_payload is None:
                return utils.build_response(405, message="Expired token!!!")
                
            match event["path"]:
                case '/add_papers':
                    if not utils.check_keys(["links"], event):
                        return utils.build_response(401, message="Missing fields.")
                    return paper_tracker.add_paper(link=event["links"], 
                                                   username=decoded_payload["username"])
                case '/remove_papers':
                    if not utils.check_keys(["links"], event):
                        return utils.build_response(401, message="Missing fields.")
                    return paper_tracker.remove_paper(link=event["links"], 
                                                   username=decoded_payload["username"])
                case '/get_papers':
                    return paper_tracker.get_papers(username=decoded_payload["username"])

        case _:
            return utils.build_response(200, "Hello from Lambda!")



if __name__ == '__main__':
    event = {
        'path': '/login',
        'username': "pillujain02",
        'password': "dog"
    }

    event = {
        'path': '/get_papers',
        # 'username': "pillujain02",
        'token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InBpbGx1amFpbjAyIiwiZXhwIjoxNjkxNDU3NDg2fQ.l6r5qrb_f9zWI6tFrBhhQIETQVc23eEQvmKGfvMjwEQ",
        # 'link': "https://arhanjain.github.io/"
    }

    r = lambda_handler(event, None)
    print(r)