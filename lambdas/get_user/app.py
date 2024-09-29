import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')  # Replace with your DynamoDB table name

def handler(event, context):
    try:
        user_id = event['pathParameters']['UserID']
        
        # Get item from DynamoDB
        response = table.get_item(
            Key={
                'UserID': user_id
            }
        )
        
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'User not found'})
            }
            
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error'})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request'})
        }
