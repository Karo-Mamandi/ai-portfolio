 # 🏡 California Housing Price Predictor
 
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-teal)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange)
![Docker](https://img.shields.io/badge/Deployment-Docker-blue)
![License](https://img.shields.io/badge/License-MIT-green)
 
An end-to-end regression project that predicts median house values in California using demographic, geographic, and housing-density features. Covers the full ML lifecycle — EDA, feature engineering, model selection, hyperparameter tuning, and deployment as a containerized REST API.
 
---
 
## 📊 Project Overview
 
**Goal:** Predict `Median_House_Value` for California census block groups using features like income, location, room counts, and distance to the coast.
 
**Final Model:** Tuned XGBoost Regressor
 
| Metric | Score |
|---|---|
| Test R² | **0.876** |
| Test MAE | **~$26,115** |
| Test RMSE | **~$41,838** |
 
---
 
## 🗂️ Dataset
 
Derived from the classic California Housing dataset (20,640 rows), extended with engineered features.
 
| Column | Description |
|---|---|
| `Median_House_Value` | Target variable (USD) |
| `Median_Income` | Median income in the block group |
| `Median_Age` | Median age of houses |
| `Tot_Rooms`, `Tot_Bedrooms` | Total rooms/bedrooms in the block group |
| `Population`, `Households` | Population and household counts |
| `Latitude`, `Longitude` | Geographic coordinates |
| `Distance_to_coast` | Distance to the nearest coastline |
| `Rooms_per_Household`, `Population_per_Household`, `Bedrooms_per_Rooms` | Engineered ratio features |
| `*_log` columns | Log-transformed versions of skewed features |
| `Is_Capped` | Flag for houses capped at the dataset's max value ($500,001) |
 
---
 
## 🔍 Project Workflow
 
### 1. Exploratory Data Analysis
Checked distributions, nulls, and skewness/kurtosis across all columns. Found strong right-skew in count-based features and identified that ~4.68% of houses were capped at the dataset's maximum value.
 
### 2. Feature Engineering
- Created ratio features (`Rooms_per_Household`, `Population_per_Household`, `Bedrooms_per_Rooms`)
- Applied `log1p` transforms to skewed features
- Flagged capped houses with a binary `Is_Capped` indicator
- Dropped redundant raw columns in favor of log-transformed counterparts to reduce multicollinearity
### 3. Train/Test Split
80/20 split, **stratified on `Is_Capped`** to preserve the rare capped-house ratio in both sets.
 
### 4. Scaling
`StandardScaler` for linear models; tree-based models (Random Forest, XGBoost) trained on raw, unscaled features.
 
### 5. Baseline Models
 
| Model | Test R² | Test RMSE ($) | Test MAE ($) |
|---|---|---|---|
| Linear Regression | 0.724 | $65,476 | $43,695 |
| Ridge Regression | 0.723 | $65,754 | $43,755 |
| Lasso Regression | 0.719 | $65,963 | $44,342 |
| Random Forest | 0.856 | $44,633 | $26,982 |
| **XGBoost** | **0.868** | **$42,686** | **$27,147** |
 
### 6. Cross-Validation
5-fold CV confirmed the results were stable, not an artifact of a lucky split:
 
| Model | CV R² Mean | CV R² Std |
|---|---|---|
| XGBoost | 0.858 | 0.006 |
| Random Forest | 0.851 | 0.006 |
| Linear Regression | 0.717 | 0.008 |
 
### 7. Residual Analysis
Capped houses (~4.68% of data) showed ~31% higher prediction error (MAE $35,002 vs $26,762) than non-capped houses — an inherent data limitation, since the true value of capped houses is unknown above $500,001, not a model flaw.
 
### 8. Hyperparameter Tuning
`RandomizedSearchCV` (50 iterations, 5-fold CV) on XGBoost improved test performance and reduced overfitting:
 
| Metric | Untuned | Tuned |
|---|---|---|
| Test R² | 0.868 | **0.876** |
| Test RMSE ($) | $42,686 | **$41,838** |
| Test MAE ($) | $27,147 | **$26,115** |
| Train/Test RMSE gap ratio | 1.68x | **1.50x** |
 
**Best hyperparameters:**
```python
{
  'colsample_bytree': 0.610,
  'gamma': 0.054,
  'learning_rate': 0.019,
  'max_depth': 9,
  'min_child_weight': 1,
  'n_estimators': 663,
  'reg_alpha': 0.563,
  'reg_lambda': 1.391,
  'subsample': 0.656
}
```
 
### 9. Deployment
The final model is served via a **FastAPI** REST API with a `/predict` endpoint, containerized with **Docker** for portable, reproducible deployment.
 
---
 
## 🗄️ Project Structure
 
```
California-Housing-With-AI/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .dockerignore
├── Dockerfile
├── LICENSE
│
├── notebooks/
│   └── practice.ipynb          # EDA, feature engineering, training & tuning
│
├── app.py                      # FastAPI application
├── preprocessing.py            # Feature engineering (shared: training & inference)
│
└── model_artifacts/
    ├── xgb_model.pkl           # Final tuned XGBoost model
    ├── scaler.pkl              # StandardScaler (used for linear models)
    └── feature_names.pkl       # Exact feature order expected by the model
```
 
---
 
## ⚙️ Setup & Installation
 
### Option A: Local (Python + venv)
 
```bash
git clone https://github.com/<your-username>/California-Housing-With-AI.git
cd California-Housing-With-AI
 
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
 
pip install -r requirements.txt
 
uvicorn app:app --reload
```
 
### Option B: Docker (recommended)
 
```bash
git clone https://github.com/<your-username>/California-Housing-With-AI.git
cd California-Housing-With-AI
 
docker build -t housing-price-api .
docker run -p 8000:8000 housing-price-api
```
 
Either way, the API will be available at:
- **Base URL:** `http://127.0.0.1:8000`
- **Interactive docs (Swagger UI):** `http://127.0.0.1:8000/docs`
---
 
## 🚀 Usage
 
### Example Request
 
**POST** `/predict`
 
```json
{
  "Median_Income": 5.5,
  "Median_Age": 25,
  "Tot_Rooms": 3000,
  "Tot_Bedrooms": 600,
  "Population": 1500,
  "Households": 550,
  "Latitude": 34.05,
  "Longitude": -118.25,
  "Distance_to_coast": 5000.0
}
```
 
**Response:**
```json
{
  "predicted_price": 342567.89
}
```
 
### cURL Example
 
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "Median_Income": 5.5,
  "Median_Age": 25,
  "Tot_Rooms": 3000,
  "Tot_Bedrooms": 600,
  "Population": 1500,
  "Households": 550,
  "Latitude": 34.05,
  "Longitude": -118.25,
  "Distance_to_coast": 5000.0
}'
```
 
---
 
## ✅ Validation Results
 
The model correctly captures real-world California housing patterns:
 
| Scenario | Median Income | Distance to Coast | Predicted Price |
|---|---|---|---|
| Coastal LA, high income | 5.5 | 5,000m | ~$342,568 |
| Inland Central Valley, low income | 1.8 | 150,000m | $52,805 |
 
This ~6.5x spread, driven by income and coastal proximity, aligns with known real-world California housing dynamics.
 
---
 
## ⚠️ Known Limitations
 
- **Capped values:** ~4.68% of training houses were capped at $500,001. The model systematically underpredicts very high-value properties since the true value above the cap is unknown. New/unseen inputs default `Is_Capped` to `0`, since it cannot be known in advance.
- **No luxury home ceiling handling:** Predictions above ~$500k should be treated with reduced confidence.
- **Static feature engineering:** Input data must match the exact preprocessing pipeline defined in `preprocessing.py`.
---
 
## 🔮 Possible Future Improvements
 
- [ ] Two-stage model: classifier for `Is_Capped` + separate regressor for capped vs. non-capped homes
- [ ] Feature importance / SHAP analysis for deeper interpretability
- [ ] Public hosting (Render, Hugging Face Spaces, Railway)
- [ ] Simple Streamlit front-end for non-technical users
- [ ] CI/CD pipeline (GitHub Actions) for automated testing & Docker image publishing
---
 
## 🛠️ Tech Stack
 
- **Language:** Python 3.11
- **Data & ML:** pandas, numpy, scikit-learn, XGBoost
- **API:** FastAPI, Uvicorn
- **Model persistence:** joblib
- **Deployment:** Docker
---
 
## 📄 License
 
This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
 

## 🔍 Project Workflow
 
### 1. Exploratory Data Analysis
Checked distributions, nulls, and skewness/kurtosis across all columns. Found strong right-skew in count-based features and identified that ~4.68% of houses were capped at the dataset's maximum value.
 
### 2. Feature Engineering
- Created ratio features (`Rooms_per_Household`, `Population_per_Household`, `Bedrooms_per_Rooms`)
- Applied `log1p` transforms to skewed features
- Flagged capped houses with a binary `Is_Capped` indicator
- Dropped redundant raw columns in favor of log-transformed counterparts to reduce multicollinearity
### 3. Train/Test Split
80/20 split, **stratified on `Is_Capped`** to preserve the rare capped-house ratio in both sets.
 
### 4. Scaling
`StandardScaler` for linear models; tree-based models (Random Forest, XGBoost) trained on raw, unscaled features.
 
### 5. Baseline Models
 
| Model | Test R² | Test RMSE ($) | Test MAE ($) |
|---|---|---|---|
| Linear Regression | 0.724 | $65,476 | $43,695 |
| Ridge Regression | 0.723 | $65,754 | $43,755 |
| Lasso Regression | 0.719 | $65,963 | $44,342 |
| Random Forest | 0.856 | $44,633 | $26,982 |
| **XGBoost** | **0.868** | **$42,686** | **$27,147** |
 
### 6. Cross-Validation
5-fold CV confirmed the results were stable, not an artifact of a lucky split:
 
| Model | CV R² Mean | CV R² Std |
|---|---|---|
| XGBoost | 0.858 | 0.006 |
| Random Forest | 0.851 | 0.006 |
| Linear Regression | 0.717 | 0.008 |
 
### 7. Residual Analysis
Capped houses (~4.68% of data) showed ~31% higher prediction error (MAE $35,002 vs $26,762) than non-capped houses — an inherent data limitation, since the true value of capped houses is unknown above $500,001, not a model flaw.
 
### 8. Hyperparameter Tuning
`RandomizedSearchCV` (50 iterations, 5-fold CV) on XGBoost improved test performance and reduced overfitting:
 
| Metric | Untuned | Tuned |
|---|---|---|
| Test R² | 0.868 | **0.876** |
| Test RMSE ($) | $42,686 | **$41,838** |
| Test MAE ($) | $27,147 | **$26,115** |
| Train/Test RMSE gap ratio | 1.68x | **1.50x** |
 
**Best hyperparameters:**
```python
{
  'colsample_bytree': 0.610,
  'gamma': 0.054,
  'learning_rate': 0.019,
  'max_depth': 9,
  'min_child_weight': 1,
  'n_estimators': 663,
  'reg_alpha': 0.563,
  'reg_lambda': 1.391,
  'subsample': 0.656
}
```
 
### 9. Deployment
The final model is served via a **FastAPI** REST API with a `/predict` endpoint, containerized with **Docker** for portable, reproducible deployment.
 
---
 
## 🗄️ Project Structure
 
```
California-Housing-With-AI/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .dockerignore
├── Dockerfile
├── LICENSE
│
├── notebooks/
│   └── practice.ipynb          # EDA, feature engineering, training & tuning
│
├── app.py                      # FastAPI application
├── preprocessing.py            # Feature engineering (shared: training & inference)
│
└── model_artifacts/
    ├── xgb_model.pkl           # Final tuned XGBoost model
    ├── scaler.pkl              # StandardScaler (used for linear models)
    └── feature_names.pkl       # Exact feature order expected by the model
```
 
---
 
## ⚙️ Setup & Installation
 
### Option A: Local (Python + venv)
 
```bash
git clone https://github.com/<your-username>/California-Housing-With-AI.git
cd California-Housing-With-AI
 
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
 
pip install -r requirements.txt
 
uvicorn app:app --reload
```
 
### Option B: Docker (recommended)
 
```bash
git clone https://github.com/<your-username>/California-Housing-With-AI.git
cd California-Housing-With-AI
 
docker build -t housing-price-api .
docker run -p 8000:8000 housing-price-api
```
 
Either way, the API will be available at:
- **Base URL:** `http://127.0.0.1:8000`
- **Interactive docs (Swagger UI):** `http://127.0.0.1:8000/docs`
---
 
## 🚀 Usage
 
### Example Request
 
**POST** `/predict`
 
```json
{
  "Median_Income": 5.5,
  "Median_Age": 25,
  "Tot_Rooms": 3000,
  "Tot_Bedrooms": 600,
  "Population": 1500,
  "Households": 550,
  "Latitude": 34.05,
  "Longitude": -118.25,
  "Distance_to_coast": 5000.0
}
```
 
**Response:**
```json
{
  "predicted_price": 342567.89
}
```
 
### cURL Example
 
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "Median_Income": 5.5,
  "Median_Age": 25,
  "Tot_Rooms": 3000,
  "Tot_Bedrooms": 600,
  "Population": 1500,
  "Households": 550,
  "Latitude": 34.05,
  "Longitude": -118.25,
  "Distance_to_coast": 5000.0
}'
```
 
---
 
## ✅ Validation Results
 
The model correctly captures real-world California housing patterns:
 
| Scenario | Median Income | Distance to Coast | Predicted Price |
|---|---|---|---|
| Coastal LA, high income | 5.5 | 5,000m | ~$342,568 |
| Inland Central Valley, low income | 1.8 | 150,000m | $52,805 |
 
This ~6.5x spread, driven by income and coastal proximity, aligns with known real-world California housing dynamics.
 
---
 
## ⚠️ Known Limitations
 
- **Capped values:** ~4.68% of training houses were capped at $500,001. The model systematically underpredicts very high-value properties since the true value above the cap is unknown. New/unseen inputs default `Is_Capped` to `0`, since it cannot be known in advance.
- **No luxury home ceiling handling:** Predictions above ~$500k should be treated with reduced confidence.
- **Static feature engineering:** Input data must match the exact preprocessing pipeline defined in `preprocessing.py`.
---
 
## 🔮 Possible Future Improvements
 
- [ ] Two-stage model: classifier for `Is_Capped` + separate regressor for capped vs. non-capped homes
- [ ] Feature importance / SHAP analysis for deeper interpretability
- [ ] Public hosting (Render, Hugging Face Spaces, Railway)
- [ ] Simple Streamlit front-end for non-technical users
- [ ] CI/CD pipeline (GitHub Actions) for automated testing & Docker image publishing
---
 
## 🛠️ Tech Stack
 
- **Language:** Python 3.11
- **Data & ML:** pandas, numpy, scikit-learn, XGBoost
- **API:** FastAPI, Uvicorn
- **Model persistence:** joblib
- **Deployment:** Docker
---
 
## 📄 License
 
This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
 
