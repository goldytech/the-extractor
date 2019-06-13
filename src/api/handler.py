import json


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

# region for debugging purpose
# with open('data.json', 'r') as txt:
#     jsondata = txt.read()
# payload = json.loads(jsondata)
# summary = hello(payload, None)
# print(summary)
# endregion
