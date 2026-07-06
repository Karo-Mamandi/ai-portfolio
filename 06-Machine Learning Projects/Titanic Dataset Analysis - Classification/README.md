# 🚢 Titanic Survival Prediction using Machine Learning

A comprehensive machine learning project that predicts passenger survival on the Titanic using multiple classification models with feature engineering and hyperparameter tuning.

---

## 🎯 Project Overview

This project builds and compares multiple machine learning models to predict Titanic passenger survival based on features like age, gender, ticket class, fare, and more. The project includes extensive exploratory data analysis (EDA), feature engineering, model training, and evaluation.

---

## 🚀 Key Features

- **Exploratory Data Analysis (EDA)**: Comprehensive visualization and analysis
- **Feature Engineering**: Creating new features from existing data
- **Data Preprocessing**: Handling missing values, encoding categorical variables, feature scaling
- **Multiple Models**:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Extra Trees
  - XGBoost
  - CatBoost
  - LightGBM
- **Cross-Validation**: 5-fold cross-validation for robust evaluation
- **Model Evaluation**: Accuracy, Precision, Recall, F1-Score, Classification Report, Confusion Matrix

---

## 🛠️ Tech Stack

- Python 3.x
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- XGBoost
- CatBoost
- LightGBM

---

## 📊 Dataset

**Titanic Dataset (Kaggle)**
- 891 training samples
- 418 test samples
- 12 features
- Target: Survived (0 = No, 1 = Yes)

**Features:**
- PassengerId, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked

---

## 📁 Project Structure
```
Titanic-Survival-Prediction/
│
├── data/
│   ├── train.csv              # Training data
│   ├── test.csv               # Test data
│   └── gender_submission.csv  # Sample submission format (reference only)
│
├── notebooks/
│ └── titanic_survival.ipynb # Main notebook
│
├── requirements.txt # Dependencies
└── README.md # Project documentation
```

## 👤 Author
#### Karo Mamandiazar
