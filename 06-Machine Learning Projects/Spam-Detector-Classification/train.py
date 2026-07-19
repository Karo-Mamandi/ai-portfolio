"""
Spam Email Detection - Training Pipeline
-----------------------------------------
Improvements over the original notebook:
  1. Text cleaning (lowercasing, URL/number/punctuation stripping) before TF-IDF.
  2. class_weight='balanced' on models that support it (dataset is ~87% ham / 13% spam).
  3. Dropped KNN (poor fit for high-dimensional sparse TF-IDF vectors, slow at inference).
  4. GridSearchCV with 5-fold cross-validation + F1 scoring (not just accuracy) to tune
     the strongest candidates.
  5. Model selection driven by test F1 / recall on the spam class, not raw accuracy
     (accuracy is misleading on an imbalanced dataset like this one).
  6. Persists the winning model AND the fitted vectorizer with joblib so the exact
     same feature space is used at inference time in the API.
"""

import json
import joblib
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

from text_utils import clean_text

RANDOM_STATE = 42


# ---------------------------------------------------------------------------
# 2. Load + prep data
# ---------------------------------------------------------------------------
print("Loading data...")
data = pd.read_csv("spam-email-detection.csv")
data = data.dropna(subset=["Category", "Message"]).drop_duplicates()

data["clean_message"] = data["Message"].astype(str).apply(clean_text)

# spam -> 0, ham -> 1  (kept consistent with the original notebook's convention)
data["label"] = data["Category"].map({"spam": 0, "ham": 1})

X = data["clean_message"]
y = data["label"].astype(int)

print(f"Total rows after cleanup: {len(data)}")
print(y.value_counts(normalize=True).rename({0: "spam", 1: "ham"}))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)

# ---------------------------------------------------------------------------
# 3. Feature extraction
# ---------------------------------------------------------------------------
vectorizer = TfidfVectorizer(
    stop_words="english",
    lowercase=True,
    min_df=2,
    ngram_range=(1, 2),
)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# ---------------------------------------------------------------------------
# 4. Candidate models (balanced class weights, light grid search)
# ---------------------------------------------------------------------------
candidates = {
    "logistic_regression": (
        LogisticRegression(class_weight="balanced", max_iter=1000, random_state=RANDOM_STATE),
        {"C": [0.5, 1, 5, 10]},
    ),
    "linear_svc": (
        SVC(kernel="linear", class_weight="balanced", probability=True, random_state=RANDOM_STATE),
        {"C": [0.5, 1, 5]},
    ),
    "random_forest": (
        RandomForestClassifier(class_weight="balanced", random_state=RANDOM_STATE, n_jobs=-1),
        {"n_estimators": [200, 400], "max_depth": [None, 30]},
    ),
    "decision_tree": (
        DecisionTreeClassifier(class_weight="balanced", random_state=RANDOM_STATE),
        {"max_depth": [None, 20, 40]},
    ),
}

results = {}
fitted_models = {}

print("\nTuning candidate models (5-fold CV, scoring=f1)...")
for name, (estimator, grid) in candidates.items():
    print(f"  -> {name}")
    search = GridSearchCV(estimator, grid, scoring="f1_weighted", cv=5, n_jobs=-1)
    search.fit(X_train_vec, y_train)
    best_model = search.best_estimator_
    fitted_models[name] = best_model

    train_pred = best_model.predict(X_train_vec)
    test_pred = best_model.predict(X_test_vec)

    results[name] = {
        "best_params": search.best_params_,
        "train_accuracy": accuracy_score(y_train, train_pred),
        "test_accuracy": accuracy_score(y_test, test_pred),
        # pos_label=0 -> spam is the class we care most about catching
        "spam_precision": precision_score(y_test, test_pred, pos_label=0),
        "spam_recall": recall_score(y_test, test_pred, pos_label=0),
        "spam_f1": f1_score(y_test, test_pred, pos_label=0),
        "weighted_f1": f1_score(y_test, test_pred, average="weighted"),
    }

results_df = pd.DataFrame(results).T.sort_values("spam_f1", ascending=False)
print("\n=== Model comparison (sorted by spam F1) ===")
print(results_df.to_string())

# ---------------------------------------------------------------------------
# 5. Pick the winner
# ---------------------------------------------------------------------------
best_name = results_df.index[0]
best_model = fitted_models[best_name]
print(f"\nSelected model: {best_name}")
print(classification_report(y_test, best_model.predict(X_test_vec), target_names=["spam", "ham"]))
print("Confusion matrix (rows=true, cols=pred, order=[spam, ham]):")
print(confusion_matrix(y_test, best_model.predict(X_test_vec)))

# ---------------------------------------------------------------------------
# 6. Persist model + vectorizer + metadata
# ---------------------------------------------------------------------------
joblib.dump(best_model, "model/model.joblib")
joblib.dump(vectorizer, "model/vectorizer.joblib")

metadata = {
    "model_name": best_name,
    "label_map": {"0": "spam", "1": "ham"},
    "metrics": results[best_name],
    "clean_text_fn": "lowercase + strip URLs + strip non-alpha chars",
}
with open("model/metadata.json", "w") as f:
    json.dump(metadata, f, indent=2, default=float)

print("\nSaved model/model.joblib, model/vectorizer.joblib, model/metadata.json")
