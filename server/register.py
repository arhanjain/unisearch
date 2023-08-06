import boto3
import utils

dynamodb = boto3.resource('dynamodb', region_name="us-west-2")
table = dynamodb.Table('unisearchdb')
async def get_user(username):

    user = table.get_item(Key={"username": username})
    return user


async def register(username, pw):
    if not (username and pw):
        utils.build_response(401, message="Username and password required!")

    user = await get_user(username)

    return utils.build_response(200, message=user)