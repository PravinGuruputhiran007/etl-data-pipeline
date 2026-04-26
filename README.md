# ETL Data Pipeline (Python + PostgreSQL)

## 📖 Overview
This project implements an end-to-end ETL pipeline that:
- Extracts data from CSV
- Transforms data using Pandas
- Loads data into PostgreSQL
- Generates aggregated insights

## ⚙️ Tech Stack
- Python
- Pandas
- PostgreSQL
- SQLAlchemy

## 🔄 Pipeline Flow
1. Extract: Read CSV data
2. Transform:
   - Data cleaning
   - Column normalization
   - Derived field (total_amount)
3. Load:
   - Insert into PostgreSQL
   - Create aggregated table (daily_sales)

## 🚀 How to Run
bash
pip install -r requirements.txt
python main.py