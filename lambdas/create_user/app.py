import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')  # Replace with your DynamoDB table name

def handler(event, context):
    try:
        data = json.loads(event['body'])
        user_id = data['UserID']
        name = data['Name']
        email = data['Email']
        age = data['Age']
        
        # Put item into DynamoDB
        table.put_item(
            Item={
                'UserID': user_id,
                'Name': name,
                'Email': email,
                'Age': age
            },
            ConditionExpression='attribute_not_exists(UserID)'  # Prevent overwrite
        )
        
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'User created successfully'})
        }
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'User already exists'})
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Internal server error'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Invalid request'})
        }
