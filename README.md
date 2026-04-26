# ETL Data Pipeline (Python + PostgreSQL)

## 📖 Overview
This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Python and PostgreSQL.

The pipeline ingests raw CSV data, performs data cleaning and transformation, and loads the processed data into a relational database for analytics.

---

## 🏗️ Architecture
CSV File → Extract → Transform → PostgreSQL → Aggregation Table

---

## ⚙️ Tech Stack
- Python (Pandas)
- PostgreSQL
- SQLAlchemy
- Logging (Python logging module)

---

## 🔄 Pipeline Steps

### 1. Extract
- Reads raw data from CSV file
- Handles file validation

### 2. Transform
- Removes null values
- Standardizes column names
- Converts data types (e.g., order_date)
- Creates derived column: `total_amount`

### 3. Load
- Loads processed data into `orders` table
- Creates aggregated table `daily_sales`

---

## 📊 Output Tables

### Orders Table
Stores cleaned transactional data.

### Daily Sales Table
Aggregated data:
- Total sales per day

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py