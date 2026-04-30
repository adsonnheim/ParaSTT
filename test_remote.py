import requests
import os
from dotenv import load_dotenv

load_dotenv(".env.local")

audio_file_path = "test_audio.wav"

api_key = os.environ.get("PARAKEET_API_KEY")
public_url = str(os.environ.get("PARAKEET_API_URL") + f"transcribe?api_key={api_key}")
#print(public_url)
with open(audio_file_path, "rb") as f:
    response = requests.post(
        public_url,
        files={"file": f}
    )

print("Status:", response.status_code)
print("Raw response:", response.text)