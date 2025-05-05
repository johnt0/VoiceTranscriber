import boto3
import os
import io
from dotenv import load_dotenv

load_dotenv()

def upload_to_s3(file_bytes, filename):
    s3 = boto3.client('s3')
    bucket_name = os.getenv('AWS_S3_BUCKET_NAME')

    try:
        file_obj = io.BytesIO(file_bytes)
        s3.upload_fileobj(file_obj, bucket_name, filename)
    
        return f"s3://{bucket_name}/{filename}"
    except Exception as e:
        print(e)
        return