import json
import boto3
import jwt

dynamodb = boto3.resource("dynamodb", region_name="us-west-2")
table = dynamodb.Table('unisearchdb')

def handler(event, context):
  print('received event:')
  print(event)

  token = event["headers"]["Authorization"]
  try: 
    decoded_token = jwt.decode(token, algorithms=[jwt.get_unverified_header(token)["alg"]], options={"verify_signature": False})
  except Exception as e:
    print(e)
    return {
      'statusCode': 401,
    }
  
  match event['path']:
    case '/add_papers':
      username = decoded_token['cognito:username']
      papers = events[]
    case '/remove_papers':
      pass


  return {
      'statusCode': 200,
      # 'headers': {
      #     'Access-Control-Allow-Headers': '*',
      #     'Access-Control-Allow-Origin': '*',
      #     'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      # },
      'body': json.dumps('Hello from your new Amplify Python lambda!')
  }

if __name__ == "__main__":
  t = "eyJraWQiOiJINk1reXZUeTlUZlZ5bjY3c2hCZnZlTFBndmQzUjBidXpwT2FaWXFsdnIwPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI3OGQxYTNhMC05MGMxLTcwYjgtNDhkMy0wM2IxMDNmMWE0ZDYiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tXC91cy13ZXN0LTJfZlYzUjFOeWtBIiwiY29nbml0bzp1c2VybmFtZSI6Ijc4ZDFhM2EwLTkwYzEtNzBiOC00OGQzLTAzYjEwM2YxYTRkNiIsIm9yaWdpbl9qdGkiOiIxZjU4MmVjYS0zN2Y5LTRmODgtYTdiYy00NDY5Y2Q5NTI0NDQiLCJhdWQiOiJpNWtxZjFzNzhoNG9ydW1oa3Z0Z3VtY2Y4IiwiZXZlbnRfaWQiOiJjNDRhZWEwMy01NTVlLTQ3NGMtOTE2Ny1hZmEzODhjM2FjMWYiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY5MjEzMzc1MywiZXhwIjoxNjkyMTM3MzUzLCJpYXQiOjE2OTIxMzM3NTMsImp0aSI6IjE2NzA4OWNlLTBmMWEtNDc3Ni1iNjcxLTM3MjM1YzkzNzk1OCIsImVtYWlsIjoiYXJoYW4uajA0QGdtYWlsLmNvbSJ9.b12s7fHANhDUmtuHTp7QKVPBdEolkSvF1LsBbW6jbqtbYoNraw99UlMn7ew143288a79SolQatHT2bVmAVaH39m2wlWnMyYaCjSMRHHjCgxDP5mtMg-2Q4xZ-s3CP9oyM_dWbtbT653orL35utqsDaKLBkZZbOX8f6g4m77U4LMOBPIxTKoCiN7kTAHPlOBTG6Kv1W2niNLRGjHz1eUtPG-z_MNMMMc0HltYmJazDphqW0Ib11-iXZ-pPbwFpt5OIPXnwLEnPMKjOEHkn_euwOYIsVZEYJxHTxGaCCLokJcCpip1Ngxz-8EymvKPwh2GIZcx39dPNCTeCAKk6-CmMw"
  event = {
    "headers": {
      "Authorization": t
    }
  }
  handler(event, None)