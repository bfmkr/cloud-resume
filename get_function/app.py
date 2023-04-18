import json
import boto3

db = boto3.resource('dynamodb')
table_name = 'cloud-resume-challenge'
table = db.Table(table_name)


def get_function(event, context):

    response = table.get_item(Key = {"ID": "visitors"})
    visits = int(response["Item"]['visits'])

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
        },
        "body": json.dumps({"visits": visits}),
    }

