import os

import boto3
import csv
import io
from botocore.exceptions import ClientError
s3_client = boto3.client('s3')

bucket_name = 'aws-learning-omm'
file_key = 'test_aws_omm.csv'
key=os.getenv('AWS_ACCESS_KEY_ID')
secret=os.environ.get('AWS_SECRET_ACCESS_KEY')
region=os.getenv('AWS_DEFAULT_REGION')

print(f"AWS Default Region: {region}")

try:
    response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    csv_content = response['Body'].read().decode('utf-8')
    text_stream = io.StringIO(csv_content)

    reader = csv.DictReader(text_stream)

    for row in reader:
        print(row)

except ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == 'NoSuchBucket':
        print(f"Error: Bucket '{bucket_name}' does not exist.")
    elif error_code == 'NoSuchKey':
        print(f"Error: File key '{file_key}' was not found in bucket.")
    elif error_code == 'AccessDenied':
        print("Error: Access denied. Check your AWS credentials or IAM permissions.")
    else:
        print(f"AWS S3 Error: {e}")

def upsertEntries(dataDf,bucketDetails):
    
