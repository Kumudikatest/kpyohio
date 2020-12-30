import boto3
sns = boto3.client("sns")
from os import environ

def handler(event, context):
    try:
        data = sns.publish(
            Message="test",
            TopicArn="arn:aws:sns:us-east-2:318300609668:dynamodb",
            MessageStructure="String",
            MessageAttributes={}
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
