from Scripts.extract import extract_data
from Scripts.transform import transform_data
from Scripts.load import load_data, load_aggregated_data
import logging

def run_pipeline():
    try:
        logging.info("ETL pipeline started")

        logging.info("Extracting data...")
        df = extract_data("C:/Users/Ranjha/Desktop/ETL Project/Data/Order.csv")

        logging.info("Transforming data...")
        df_clean = transform_data(df)

        logging.info("Loading data to PostgreSQL (orders table)...")
        load_data(df_clean)

        logging.info("Creating aggregated data...")
        load_aggregated_data(df_clean)

        logging.info("ETL pipeline completed successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()