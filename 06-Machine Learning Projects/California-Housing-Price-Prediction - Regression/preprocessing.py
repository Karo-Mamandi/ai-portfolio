# Build a clean inference/preprocessing function
"""
 This replicates every transformation step (log, ratios, etc.) so raw new data can be turned into a prediction.
 This is often the part people forget — and it's the #1 source of bugs in deployment (train/serve skew).
"""

import numpy as np
import joblib


def preprocess_new_data(raw_df):
    df = raw_df.copy()

    df['Rooms_per_Household'] = df['Tot_Rooms'] / df['Households']
    df['Population_per_Household'] = df['Population'] / df['Households']
    df['Bedrooms_per_Rooms'] = df['Tot_Bedrooms'] / df['Tot_Rooms']

    df['Population_log'] = np.log1p(df['Population'])
    df['Tot_Rooms_log'] = np.log1p(df['Tot_Rooms'])
    df['Tot_Bedrooms_log'] = np.log1p(df['Tot_Bedrooms'])
    df['Households_log'] = np.log1p(df['Households'])
    df['Median_Income_log'] = np.log1p(df['Median_Income'])
    df['Rooms_per_Household_log'] = np.log1p(df['Rooms_per_Household'])
    df['Population_per_Household_log'] = np.log1p(df['Population_per_Household'])

    df['Is_Capped'] = 0

    feature_names = joblib.load('model_artifacts/feature_names.pkl')
    df = df[feature_names]

    return df