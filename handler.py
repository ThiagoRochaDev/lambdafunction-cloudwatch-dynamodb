import json
import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    print(str(event))
    
    json_object = s3_client.get_object(Bucket=bucket, Key=file_name)
    jsonFileReader = json_object.read(json_object)
    jsonArray = json.loads(jsonFileReader)
    
    table = dynamodb.Table('logs')
    table.put_item(Item=jsonArray)
    