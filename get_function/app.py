import json
import boto3


def get_DynamoDB_data():

    db = boto3.resource('dynamodb')
    table_name = 'cloud-resume-challenge'
    return db.Table(table_name)


def get_function(event, context):
    """Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    table = get_DynamoDB_data()
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

