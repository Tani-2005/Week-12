# src/feature_engineering.py


def create_date_features(df):
    """
    Extract useful features from Date column if present.
    """

    if "Date" in df.columns:

        df["Date"] = pd.to_datetime(df["Date"])

        df["Year"] = df["Date"].dt.year
        df["Month"] = df["Date"].dt.month
        df["Day"] = df["Date"].dt.day
        df["Weekday"] = df["Date"].dt.weekday

    return df