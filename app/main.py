from fastapi import FastAPI, UploadFile, File
import os
from app.s3_upload import upload_to_s3
from app.transcriber import start_transcription_job

app = FastAPI()

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    contents = await file.read()
    filename = file.filename

    # Upload to S3
    s3_uri = upload_to_s3(contents, filename)

    # Start transcription
    transcript_uri = start_transcription_job(s3_uri)

    return {
        "transcription_url": transcript_uri
    }

def main():
    pass

if __name__ == '__main__':
    main()