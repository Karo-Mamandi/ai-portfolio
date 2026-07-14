# Medical Insurance Cost Prediction

## Project Overview

This project predicts individual medical insurance charges based on demographic and lifestyle factors using various machine learning regression models.

The dataset contains information such as age, sex, BMI, number of children, smoking status, and residential region. Several regression algorithms are trained and compared to determine the best-performing model.

---

## Dataset

**Dataset:** Medical Insurance Dataset

### Features

| Feature | Description |
|----------|-------------|
| age | Age of the primary beneficiary |
| sex | Gender of the beneficiary |
| bmi | Body Mass Index |
| children | Number of dependents covered by health insurance |
| smoker | Smoking status (Yes/No) |
| region | Residential region in the US |
| charges | Individual medical insurance charges (Target Variable) |

---

## Project Workflow

1. Import required libraries
2. Load and inspect the dataset
3. Data cleaning and preprocessing
4. Exploratory Data Analysis (EDA)
5. Feature encoding and scaling
6. Train-test split
7. Model training
8. Hyperparameter tuning using GridSearchCV
9. Model evaluation
10. Save the best model using Pickle

---

## Machine Learning Models

The following regression algorithms were implemented:

- Linear Regression
- Ridge Regression
- Random Forest Regressor
- Support Vector Regressor (SVR)

---

## Evaluation Metrics

Models were evaluated using:

- R² Score
- Mean Squared Error (MSE)
- Cross Validation Score

---

## Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle

---

## Project Structure

```
Medical-Insurance-Prediction/
│
├── notebooks/Medical_Insurance.ipynb
├── data/insurance.csv
├── model_saved/model.pkl
├── requirements.txt
├── README.md
└── images/..
```


## Model Saving

The trained model is saved using Pickle.

```python
import pickle

pickle.dump(model, open("model.pkl", "wb"))
```

Load the model

```python
model = pickle.load(open("model.pkl", "rb"))
```

## License

This project is intended for educational purposes.
