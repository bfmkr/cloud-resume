import json
import boto3

db = boto3.resource('dynamodb')
table_name = 'cloud-resume-challenge'
table = db.Table(table_name)

def put_function(event, context):

    response = table.update_item(
        Key = {'ID': 'visitors'},
        UpdateExpression = 'ADD visits :val',
        ExpressionAttributeValues = {':val': 1},
        ReturnValues = 'UPDATED_NEW'
        )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*"
            }
        }