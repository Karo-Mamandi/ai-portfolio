# Wrap it in an API (FastAPI — lightweight, production-friendly)

# save as app.py
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import numpy as np

app = FastAPI(title="California Housing Price Predictor")

model = joblib.load('model_artifacts/xgb_model.pkl')
feature_names = joblib.load('model_artifacts/feature_names.pkl')

class HouseFeatures(BaseModel):
    Median_Income: float
    Median_Age: int
    Tot_Rooms: int
    Tot_Bedrooms: int
    Population: int
    Households: int
    Latitude: float
    Longitude: float
    Distance_to_coast: float

@app.post("/predict")
def predict(house: HouseFeatures):
    raw_df = pd.DataFrame([house.dict()])

    # feature engineering (reuse function from above)
    from preprocessing import preprocess_new_data
    X_new = preprocess_new_data(raw_df)

    log_pred = model.predict(X_new)
    price = float(np.expm1(log_pred)[0])

    return {"predicted_price": round(price, 2)}

@app.get("/")
def health_check():
    return {"status": "ok"}