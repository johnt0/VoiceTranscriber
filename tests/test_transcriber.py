from app.transcriber import start_transcription_job

def test_start_transcription_job(monkeypatch):
    def mock_start_transcription_job(s3_uri, media_format="flac", output_bucket=None, language_code="en-US"):
        return "https://s3.amazonaws.com/test-bucket/test.json"

    monkeypatch.setattr("app.transcriber.start_transcription_job", mock_start_transcription_job)
    result = start_transcription_job("s3://test-bucket/test.flac")
    assert "http://" in result