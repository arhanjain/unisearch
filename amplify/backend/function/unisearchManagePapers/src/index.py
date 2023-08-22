import json
import jwt
import boto3

dynamodb = boto3.resource("dynamodb", region_name="us-west-2")
table = dynamodb.Table('unisearchdb-dev')

def handler(event, context):

  token = event["headers"]["Authorization"]
  decoded_token = None
  try: 
    decoded_token = jwt.decode(token, algorithms=[jwt.get_unverified_header(token)["alg"]], options={"verify_signature": False})
  except Exception as e:
    print(e)
    return {
      'statusCode': 401,
    }

  username = decoded_token['cognito:username']
  papers_to_add = event['body']['add']
  papers_to_remove = event['body']['remove']

  with table.batch_writer() as batch:
    for paper in papers_to_add:
      batch.put_item(
        Item={
          "username": username,
          "paper_id": paper["id"],
          "paper_title": paper["title"],
          "paper_authors": set(paper["authors"]),
        },
        # ConditionExpression="attribute_not_exists(paper_id)"
      )
    for paper in papers_to_remove:
      batch.delete_item(
        Key={
          "username": username,
          "paper_id": paper["id"],
        }
      )
  
  return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps('Hello from your new Amplify Python lambda!')
  }