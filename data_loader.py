# src/config.py

import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DATA_PATHS = {
    "churn": os.path.join(BASE_DIR, "data", "customer_churn.csv"),
    "sales": os.path.join(BASE_DIR, "data", "sales_data.csv"),
    "house": os.path.join(BASE_DIR, "data", "house_prices.csv"),
}


MODEL_PATHS = {
    "churn": os.path.join(BASE_DIR, "deployment", "churn_model.pkl"),
    "sales": os.path.join(BASE_DIR, "deployment", "sales_model.pkl"),
    "house": os.path.join(BASE_DIR, "deployment", "house_price_model.pkl"),
}