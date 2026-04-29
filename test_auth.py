# test_auth.py
import requests

with open("test_audio.wav", "rb") as f:
    response = requests.post(
        "http://localhost:8000/transcribe",
        headers={"X-API-Key": "nqWJrJTOzKHM5O0m_yxOLLbeYJteaANON8xfuRuAcm8"},
        files={"file": f}
    )

print("Status:", response.status_code)
print("Response:", response.json())