import logging
import pandas as pd   # ✅ correct import

def transform_data(df):
    logging.info("Cleaning and transforming data")

    df = df.dropna()
    df.columns = [col.lower() for col in df.columns]

    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total_amount'] = df['price'] * df['quantity']

    return df