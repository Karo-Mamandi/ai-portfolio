<div align="center">

# 📬 Mail Sorter — Spam Email Detector

A machine learning spam classifier with a FastAPI backend, a postal-themed web UI, and one-command Docker deployment.

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.139-009688.svg)](https://fastapi.tiangolo.com/)
[![scikit--learn](https://img.shields.io/badge/scikit--learn-1.8-f89939.svg)](https://scikit-learn.org/)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

</div>

> Paste a message in, hit **Sort this mail**, and it gets stamped **SPAM** or **HAM** with a confidence score — backed by a TF-IDF + Linear SVM model trained and tuned in the included notebook.
>
> <!-- Add a screenshot once it's running: drop an image at docs/screenshot.png and uncomment below -->
> <!-- <p align="center"><img src="docs/screenshot.png" alt="Mail Sorter screenshot" width="700"></p> -->

---

## Table of contents

- [Features](#features)
- [Demo](#demo)
- [Model performance](#model-performance)
- [Project structure](#project-structure)
- [Getting started](#getting-started)
  - [Run with Docker (recommended)](#run-with-docker-recommended)
  - [Run locally without Docker](#run-locally-without-docker)
- [API reference](#api-reference)
- [Retraining on your own data](#retraining-on-your-own-data)
- [How the model works](#how-the-model-works)
- [Known limitations](#known-limitations)
- [Roadmap](#roadmap)
- [Tech stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- 🧠 **Tuned ML pipeline** — TF-IDF (uni+bigrams) → Linear SVM, chosen out of 4 tuned candidates (Logistic Regression, Decision Tree, Random Forest, SVM) via 5-fold `GridSearchCV`, optimizing for spam-class F1 on an imbalanced dataset (87% ham / 13% spam).
- ⚡ **FastAPI backend** — a small, typed REST API (`/api/predict`, `/api/health`) with request validation via Pydantic.
- 🎨 **Postal-themed frontend** — vanilla HTML/CSS/JS, no build step, a running "sorting log" of everything you've checked in the session.
- 🐳 **Dockerized** — `docker compose up --build` and you're live on `localhost:8000`.
- 📓 **Full training notebook included** — every modeling decision is explained inline, with real executed outputs, so you can see (and rerun) the reasoning, not just the final artifact.
- 💾 **Reproducible inference** — the exact fitted vectorizer is persisted alongside the model, so training and serving never drift apart.

## Demo

| Input | Result |
|---|---|
| `CONGRATULATIONS! You've won a $1000 Amazon gift card! Click here to claim your prize now: http://bit.ly/win-now` | 🟥 **SPAM** (100% confidence) |
| `Hey, are we still meeting for coffee at 10am tomorrow?` | 🟩 **HAM** (100% confidence) |

## Model performance

Trained on 5,169 deduplicated messages, evaluated on a stratified 20% held-out test set (1,034 messages):

| Model | Test Accuracy | Spam Precision | Spam Recall | Spam F1 |
|---|---|---|---|---|
| Logistic Regression | 0.9836 | 0.919 | 0.954 | 0.936 |
| Decision Tree | 0.9429 | 0.777 | 0.771 | 0.774 |
| Random Forest | 0.9787 | 0.991 | 0.840 | 0.909 |
| **Linear SVM (selected)** | **0.9855** | **0.933** | **0.954** | **0.943** |

> Metrics are reported for the **spam** class specifically — with an 87/13 class imbalance, overall accuracy alone hides how well a model actually catches spam. See [`spam-email-detection.ipynb`](spam-email-detection.ipynb) for the full comparison, confusion matrix, and reasoning behind each modeling choice.

## Project structure

```
spam-detector/
├── spam-email-detection.ipynb   # training notebook — full reasoning + executed outputs
├── spam-email-detection.csv     # training data (Category, Message)
├── train.py                     # standalone training script (same pipeline as the notebook)
├── text_utils.py                # shared text-cleaning fn — used by BOTH training and the API
├── model/
│   ├── model.joblib              # trained classifier (Linear SVM)
│   ├── vectorizer.joblib         # fitted TF-IDF vectorizer
│   └── metadata.json             # winning model name + its test metrics
├── app/
│   ├── main.py                   # FastAPI app (REST API + serves the static frontend)
│   └── static/
│       ├── index.html
│       ├── style.css
│       └── script.js
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .dockerignore
```

## Getting started

### Run with Docker (recommended)

```bash
git clone https://github.com/<your-username>/spam-detector.git
cd spam-detector
docker compose up --build
```

Open **http://localhost:8000**

Or without compose:

```bash
docker build -t mail-sorter .
docker run -p 8000:8000 mail-sorter
```

### Run locally without Docker

Requires Python 3.10+.

```bash
git clone https://github.com/<your-username>/spam-detector.git
cd spam-detector
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open **http://localhost:8000**

## API reference

### `GET /api/health`

```json
{ "status": "ok", "model": "linear_svc" }
```

### `POST /api/predict`

**Request**
```json
{ "message": "CONGRATULATIONS! You've won a free prize, click here now!" }
```

**Response**
```json
{ "label": "spam", "is_spam": true, "confidence": 1.0 }
```

`confidence` is a float between 0 and 1. Interactive Swagger docs are available at **`/docs`** once the server is running.

## Retraining on your own data

Replace `spam-email-detection.csv` with your own CSV — it needs a `Category` column (`spam` / `ham`) and a `Message` column — then run:

```bash
python train.py
```

This overwrites `model/model.joblib`, `model/vectorizer.joblib`, and `model/metadata.json`. Restart the server (or rebuild the Docker image) to pick up the new model.

Alternatively, open `spam-email-detection.ipynb` to retrain interactively and see metrics/plots for every candidate model along the way.

## How the model works

1. **Clean** — lowercase, strip URLs and non-alphabetic characters, collapse whitespace (`text_utils.py`).
2. **Vectorize** — `TfidfVectorizer` with English stop-word removal, unigrams + bigrams, `min_df=2`.
3. **Classify** — a Linear SVM (`class_weight='balanced'` to handle the 87/13 class imbalance), tuned via 5-fold cross-validated grid search over `C`.
4. **Serve** — FastAPI loads the persisted model + vectorizer once at startup and reuses them for every request.

The exact same `clean_text()` function is imported by both `train.py` and `app/main.py`, so the vectorizer never sees a different token distribution at inference time than it was fit on.

## Known limitations

The training data is the classic **SMS Spam Collection** dataset — ~5,500 short SMS messages from around 2011, mostly UK prize/lottery/ringtone spam. It performs strongly on that style of spam, but is noticeably weaker on modern email-phishing phrasing (e.g. "your account will be suspended, verify now") since that vocabulary is barely represented in training. For production use on real email, retrain on a larger/modern corpus — e.g. [Enron-Spam](https://github.com/MWiechmann/enron_spam_data) combined with SpamAssassin's public corpus. The pipeline (clean → TF-IDF → tuned linear model) carries over unchanged; only the CSV needs to change.

## Roadmap

- [ ] Retrain on a modern email corpus (Enron-Spam + SpamAssassin)
- [ ] Add a `/api/predict/batch` endpoint for scoring multiple messages at once
- [ ] Persist the sorting log server-side (currently client-side only, per session)
- [ ] Add basic auth / rate limiting before exposing publicly
- [ ] CI workflow to re-run the notebook and fail on metric regressions

## Tech stack

**ML:** scikit-learn (TF-IDF, Linear SVM, Logistic Regression, Random Forest, Decision Tree), pandas, joblib
**Backend:** FastAPI, Pydantic, Uvicorn
**Frontend:** vanilla HTML / CSS / JavaScript (no build step, no framework)
**Deployment:** Docker, docker-compose

## Contributing

Issues and PRs welcome. If you're changing the model, please rerun `spam-email-detection.ipynb` (or `train.py`) and update the metrics table in this README so the numbers stay honest.

## License

[MIT](LICENSE) — do whatever you want with it, just don't blame me if it lets a prize scam through.

## 👤 Author
### Karo Mamandiazar
