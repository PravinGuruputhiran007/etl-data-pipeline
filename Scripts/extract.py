import pandas as pd
import logging

def extract_data(filepath):
    logging.info(f"Reading file from {filepath}")
    return pd.read_csv(filepath)