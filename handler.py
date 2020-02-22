import json
import boto3
import uuid

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    print(str(event))
    print(str(bucket))
    print(str(file_name))
    
    json_object = s3_client.get_object(Bucket=bucket,Key=file_name)
    id_bd = str(uuid.uuid4())
    
    
    table = dynamodb.Table('Logs')
    table.put_item(Item={
        'id': id_bd,
        'arquivo_name': file_name,
        'bucket_name': bucket
        
    })
    
   