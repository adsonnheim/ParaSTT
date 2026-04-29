from fastapi import FastAPI, UploadFile, File, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv
import nemo.collections.asr as nemo_asr
import tempfile
import os

app = FastAPI()

load_dotenv(".env.local")

API_KEYS = set(filter(None, os.environ.get("API_KEYS", "").split(",")))
api_key_header = APIKeyHeader(name="X-API-Key")

def validate_key(key: str = Security(api_key_header)):
    if key not in API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return key

@app.on_event("startup")
async def load_model():
    global model
    model = nemo_asr.models.ASRModel.from_pretrained("nvidia/parakeet-tdt-0.6b-v3")

@app.post("/transcribe")
async def transcribe(
    file: UploadFile = File(...),
    api_key: str = Security(validate_key)
):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
    try:
        transcriptions = model.transcribe([tmp_path])
        return {"transcript": transcriptions[0]}
    finally:
        os.unlink(tmp_path)

@app.get("/health")
async def health():
    return {"status": "ok"}