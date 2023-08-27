import json
import jwt
import boto3

dynamodb = boto3.resource("dynamodb", region_name="us-west-2")
table = dynamodb.Table('unisearchdb-dev')

def handler(event, context):
  print('received event:')
  print(event)

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
  # papers = {paper.strip() for paper in event['body']['papers']}
  papers_to_add = event['body']['add']
  papers_to_remove = event['body']['remove']

  print(f"papers to add: {papers_to_add} \n papers to remove: {papers_to_remove}")
  
  '''
  papers_to_add = [
            {
                "id": "github.com",
                "authors": ["author1", "author2"],
                "title": "title"
            },
            {
                "id": "linkedin.com",
                "authors": ["author3"],
                "title": "title2"
            }
        ],
  papers_to_remove = []

  '''

  with table.batch_writer() as batch:
    for paper in papers_to_add:
      print(paper['id'])
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
      print(paper['id'])
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