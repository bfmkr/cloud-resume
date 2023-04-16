import json
import boto3


db = boto3.resource('dynamodb')
table_name = 'cloud-resume-challenge'
table = db.Table(table_name)


def put_function(event, context):

    response = table.get_item(
        Key = {'ID':'visitors'}
        )

    visit_count = response['Item']['visits']
    visit_count = str(int(visit_count)+1)

    response = table.put_item(
            Item = {
            'ID': 'visitors',
            'visits': visit_count
            }
        )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
        },
        'body': json.dumps({'visits': visit_count})
    }