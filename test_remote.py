import requests

audio_file_path = "test_audio.wav"
api_key = "nqWJrJTOzKHM5O0m_yxOLLbeYJteaANON8xfuRuAcm8"
public_url = f"https://8000-01kqctw5a497z7q12f5cdrt64y.cloudspaces.litng.ai/transcribe?api_key={api_key}"

with open(audio_file_path, "rb") as f:
    response = requests.post(
        public_url,
        files={"file": f}
    )

print("Status:", response.status_code)
print("Raw response:", response.text)