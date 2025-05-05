from unittest.mock import Mock
from app.s3_upload import upload_to_s3  
def test_upload_file_to_s3(monkeypatch):
    mock_s3_client = Mock()
    monkeypatch.setattr("app.s3.boto3.client", lambda service: mock_s3_client)

    test_file = Mock()
    test_file.filename = "test.wav"
    test_file.read = lambda: b"fake file content"

    result = upload_to_s3(test_file, "test-bucket")

    assert result.startswith("s3://test-bucket/")
    mock_s3_client.upload_fileobj.assert_called_once()
