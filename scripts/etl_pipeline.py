import pandas as pd
import sqlite3
import os

# -----------------------------
# PATH SETUP
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "sales_data_sample.csv")
db_path = os.path.join(BASE_DIR, "results", "sales_database.db")

# -----------------------------
# EXTRACT
# -----------------------------
df = pd.read_csv(data_path, encoding="latin1")

print("Raw Data")
print(df.head())

# -----------------------------
# CONNECT DATABASE
# -----------------------------
conn = sqlite3.connect(db_path)

# -----------------------------
# LOAD RAW TABLE
# -----------------------------
df.to_sql("raw_sales", conn, if_exists="replace", index=False)

print("Raw table created")

# -----------------------------
# TRANSFORM (Cleaning)
# -----------------------------
df_clean = df.drop_duplicates()
df_clean = df_clean.dropna()

# convert column names to lowercase
df_clean.columns = df_clean.columns.str.lower()

print("Cleaned Data")
print(df_clean.head())

# -----------------------------
# LOAD CLEANED TABLE
# -----------------------------
df_clean.to_sql("cleaned_sales", conn, if_exists="replace", index=False)

print("Cleaned table created")

# -----------------------------
# CREATE REPORTING TABLE
# -----------------------------
query = """
CREATE TABLE IF NOT EXISTS sales_summary AS
SELECT
    productline,
    SUM(quantityordered) AS total_quantity,
    SUM(sales) AS total_revenue
FROM cleaned_sales
GROUP BY productline
"""

conn.execute("DROP TABLE IF EXISTS sales_summary")
conn.execute(query)

print("Reporting table created")

# -----------------------------
# CLOSE DATABASE
# -----------------------------
conn.close()

print("ETL Pipeline Completed Successfully")