# src/preprocessing.py

import pandas as pd


def handle_missing_values(df):
    """
    Fill missing numeric values with median
    and categorical values with mode.
    """

    for col in df.columns:

        if df[col].dtype == "object":
            df[col].fillna(df[col].mode()[0], inplace=True)

        else:
            df[col].fillna(df[col].median(), inplace=True)

    return df


def encode_categorical(df):
    """
    Apply one-hot encoding.
    """

    categorical_cols = df.select_dtypes(include="object").columns

    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df