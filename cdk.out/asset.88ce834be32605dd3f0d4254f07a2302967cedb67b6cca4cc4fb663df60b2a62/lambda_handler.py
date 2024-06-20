import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ravali-test')

def handler(event, context):
    body = json.loads(event['body'])
    response = table.put_item(
        Item={
            'id': body['id'],
            'data': body['data']
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Item added successfully!')
    }