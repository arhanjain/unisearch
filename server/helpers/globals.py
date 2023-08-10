import boto3

boto3.setup_default_session(profile_name="arhan_home_pc")
dynamodb = boto3.resource('dynamodb', region_name="us-west-2")
table = dynamodb.Table('unisearchdb')