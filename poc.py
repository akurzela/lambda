import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')
db = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('trial')

def lambda_handler(event, context):
    print(event)
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    eventtime=event['Records'][0]['eventTime']
    name = event['Records'][0]['s3']['object']['key']
    address = 'https://'+bucket+'.s3.eu-central-1.amazonaws.com/'+name

    table.put_item(Item ={'Name': name, 'bucket': bucket, 'address':address, 'eventtime':eventtime})
     
