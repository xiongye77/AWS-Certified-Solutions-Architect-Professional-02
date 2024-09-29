import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')  # Replace with your DynamoDB table name

def handler(event, context):
    try:
        user_id = event['pathParameters']['UserID']
        
        # Delete item from DynamoDB
        response = table.delete_item(
            Key={
                'UserID': user_id
            },
            ConditionExpression='attribute_exists(UserID)'  # Ensure the user exists
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'User deleted successfully'})
        }
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'User not found'})
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Internal server error'})
            }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request'})
        }
