import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')  # Replace with your DynamoDB table name

def handler(event, context):
    try:
        user_id = event['pathParameters']['UserID']
        data = json.loads(event['body'])
        
        update_expression = []
        expression_attribute_values = {}
        
        if 'Name' in data:
            update_expression.append("Name = :n")
            expression_attribute_values[':n'] = data['Name']
        
        if 'Email' in data:
            update_expression.append("Email = :e")
            expression_attribute_values[':e'] = data['Email']
        
        if 'Age' in data:
            update_expression.append("Age = :a")
            expression_attribute_values[':a'] = data['Age']
        
        if not update_expression:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'No valid fields to update'})
            }
        
        # Update item in DynamoDB
        response = table.update_item(
            Key={
                'UserID': user_id
            },
            UpdateExpression="SET " + ", ".join(update_expression),
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="UPDATED_NEW"
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'User updated successfully', 'attributes': response['Attributes']})
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
