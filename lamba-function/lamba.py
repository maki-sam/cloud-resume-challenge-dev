import json
import boto3
from decimal import Decimal

# Initialize the DynamoDB resource and table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('makisam-resume-challenge')

def lambda_handler(event, context):
    try:
        # Get the current view count
        response = table.get_item(Key={'id': '0'})
        if 'Item' in response:
            views = int(response['Item']['view'])  # Convert Decimal to int
        else:
            # Initialize view count if the item doesn't exist
            views = 0

        # Increment the view count
        views += 1

        # Update the item with the new view count
        table.put_item(
            Item={
                'id': '0',
                'view': views
            }
        )

        # Return the updated view count
        return {
            'statusCode': 200,
            'body': json.dumps({'views': views})
        }
    except Exception as e:
        # Handle errors
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }