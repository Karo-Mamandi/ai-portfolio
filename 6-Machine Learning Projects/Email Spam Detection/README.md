# 📧 Email Spam Detection

A machine learning project to classify emails as **Spam** or **Ham (Not Spam)** using multiple classifiers and ensemble learning techniques.

---

## 🎯 Project Overview

This project builds and compares multiple machine learning models to detect spam emails. It uses **TF-IDF** vectorization for feature extraction and evaluates several classifiers including Logistic Regression, Decision Tree, KNN, Random Forest, and SVM. A **Stacking Classifier** is also implemented to combine the strengths of all models for improved performance.

---

## 🚀 Key Features

- Text preprocessing and cleaning
- TF-IDF feature extraction
- Multiple classification models:
  - Logistic Regression
  - Decision Tree
  - K-Nearest Neighbors (KNN)
  - Random Forest
  - Support Vector Machine (SVM)
- Ensemble learning with Stacking Classifier
- Performance evaluation (Accuracy, Precision, Recall, F1-Score)

---

## 🛠️ Tech Stack

- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Matplotlib

---

## 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | | | | |
| Decision Tree | | | | |
| KNN | | | | |
| Random Forest | | | | |
| SVM | | | | |
| Stacking Classifier | | | | |

*(Update with your actual results)*

---

```
📁 Project Structure
email-spam-detection/
│
├── data/
│ └── spam.csv # Dataset
│
├── notebooks/
│ └── spam_detection.ipynb # Jupyter notebook
│
├── requirements.txt # Dependencies
└── README.md # Project documentation
```

## 📈️ How It Works

* Data Preprocessing: Clean the email text (remove special characters, stopwords, etc.)
* 
* Feature Extraction: Convert text to numerical features using TF-IDF Vectorizer

* Model Training: Train multiple classifiers on the training data

* Ensemble Learning: Combine models using Stacking Classifier with SVM as meta-learner
* 
* Evaluation: Compare all models using classification metrics

## 📊️ Dataset
The dataset used is the SMS Spam Collection Dataset, containing:

* 5,574 SMS messages

* Labeled as spam or ham (not spam)

## 👤 Author
### Karo Mamandiazar
