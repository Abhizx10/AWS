import boto3

sns = boto3.client('sns')

def handler(event,context):
    sns.publish(
        PhoneNumber='+999999999', 
        Message=(
            'Hello! This is your reminder service '
        )
    )
    return 'success'
