import json
import requests
import os
os.environ['NO_PROXY'] = '127.0.0.1'

def response_answer(originaltext):
    response = requests.post(
        "YOUR EYEPROMPT LINK",
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer API KEY",
        },
        json={
            "variables": {
                "Player_name": f"{originaltext}"
            },
            "user": "testing",
        },
    )
    res = response.json()['choices'][0]['text']
    res = res.split('\n')[1]

    return res


def lambda_handler(event, context):
    body = json.loads(event['body'])
    originaltext = body['text']
    res = response_answer(originaltext)

    response = {
        "output": res
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response),
    }
