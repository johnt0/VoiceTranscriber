import boto3
import uuid
import time
import os

def start_transcription_job(s3_uri, media_format="flac", output_bucket=None, language_code="en-US"):
    file_ext = os.path.splitext(s3_uri)[1].lower().strip(".")
    
    transcribe = boto3.client("transcribe", region_name="us-east-1")
    job_name = "transcription_" + str(uuid.uuid4())

    response = transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={"MediaFileUri": s3_uri},
        MediaFormat=file_ext,  # Use extension as format (e.g., 'flac')
        LanguageCode="en-US",
        OutputBucketName=os.getenv("AWS_S3_BUCKET_NAME")
    )

    return f"https://s3.amazonaws.com/{os.getenv('AWS_S3_BUCKET_NAME')}/{job_name}.json"