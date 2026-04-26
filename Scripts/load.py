from sqlalchemy import create_engine
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

engine = create_engine("postgresql://postgres:pass123@localhost:5432/ETL_Project")

def load_data(df):
    logging.info("Loading main orders table")
    df.to_sql(
    "orders",
    engine,
    if_exists="replace",   # 👈 change this
    index=False
)


def load_aggregated_data(df):
    logging.info("Creating daily sales aggregation")

    daily_sales = (
        df.groupby("order_date")["total_amount"]
        .sum()
        .reset_index()
    )

    logging.info("Loading daily_sales table")
    daily_sales.to_sql("daily_sales", engine, if_exists="replace", index=False)