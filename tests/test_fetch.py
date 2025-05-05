from app.transcriber import fetch_transcript
import requests
from unittest.mock import patch

@patch("app.transcriber.requests.get")
def test_fetch_transcript(mock_get):
    mock_get.return_value.json.return_value = {
        "results": {
            "transcripts": [{"transcript": "hello world"}]
        }
    }

    text = fetch_transcript("https://fakeurl.com/transcript.json")
    assert text == "hello world"
