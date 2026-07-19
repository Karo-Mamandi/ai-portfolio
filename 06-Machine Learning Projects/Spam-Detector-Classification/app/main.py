import json
from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from text_utils import clean_text

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "model"
STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI(
    title="Spam Email Detector",
    description="TF-IDF + ML classifier that labels a message as spam or ham.",
    version="1.0.0",
)

# ---------------------------------------------------------------------------
# Load model artifacts once at startup
# ---------------------------------------------------------------------------
model = joblib.load(MODEL_DIR / "model.joblib")
vectorizer = joblib.load(MODEL_DIR / "vectorizer.joblib")
with open(MODEL_DIR / "metadata.json") as f:
    metadata = json.load(f)

LABEL_MAP = {int(k): v for k, v in metadata["label_map"].items()}  # {0: "spam", 1: "ham"}


class PredictRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=20000, description="Raw email/message text")


class PredictResponse(BaseModel):
    label: str
    is_spam: bool
    confidence: float


@app.get("/api/health")
def health():
    return {"status": "ok", "model": metadata["model_name"]}


@app.post("/api/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    text = payload.message.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    cleaned = clean_text(text)
    features = vectorizer.transform([cleaned])

    pred = int(model.predict(features)[0])
    label = LABEL_MAP[pred]

    # confidence: use predict_proba if the model supports it, else decision_function
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(features)[0]
        confidence = float(max(proba))
    elif hasattr(model, "decision_function"):
        import numpy as np
        score = model.decision_function(features)[0]
        confidence = float(1 / (1 + np.exp(-abs(score))))  # squashed to (0.5, 1)
    else:
        confidence = 1.0

    return PredictResponse(label=label, is_spam=(pred == 0), confidence=round(confidence, 4))


# ---------------------------------------------------------------------------
# Serve the frontend
# ---------------------------------------------------------------------------
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
def index():
    return FileResponse(str(STATIC_DIR / "index.html"))
