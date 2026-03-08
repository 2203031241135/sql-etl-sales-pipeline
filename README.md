**SQL-Based ETL Workflow Simulation
Project Overview**

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python and SQL. The pipeline processes a sales dataset containing more than 10,000 records and transforms raw transactional data into structured analytical tables.

The workflow simulates a typical data engineering pipeline where raw data is ingested, cleaned, and transformed into reporting tables for business insights.

**ETL Workflow**
Raw CSV Dataset
       ↓
Raw Table (raw_sales)
       ↓
Data Cleaning & Transformation
       ↓
Cleaned Table (cleaned_sales)
       ↓
Aggregated Reporting Table (sales_summary)

**Technologies Used**

Python
Pandas
SQLite
SQL
Git & GitHub

SQL-Based ETL Workflow Simulation
│
├── data
│   └── sales_data_sample.csv
│
├── scripts
│   └── etl_pipeline.py
│
├── sql
│   └── analysis_queries.sql
│
├── results
│   └── sales_database.db
│
└── README.md

ETL Pipeline Steps
**1 Extract**

The pipeline reads raw sales data from a CSV file.

sales_data_sample.csv

This dataset contains more than 10k sales records including product details, order information, and customer data.

**2 Transform**

Data cleaning and transformation steps include:

Removing duplicate records

Handling missing values

Standardizing column names

Preparing the dataset for analytics

These transformations ensure data quality before loading into the database.

**3 Load**

The processed data is loaded into a SQLite database with three main tables:

Table	Description
raw_sales	Stores original unprocessed data
cleaned_sales	Stores cleaned and standardized data
sales_summary	Aggregated reporting table


**SQL Analysis**

The project also demonstrates SQL analytical queries including:
GROUP BY
Calculate revenue by product line.
HAVING
Filter products with revenue greater than a threshold.
Subqueries
Identify records with sales above average.
JOIN
Example join queries for relational analysis.
These queries simulate real-world business intelligence reporting.

**How to Run the Project**

Clone the repository
git clone https://github.com/2203031241135/sql-etl-sales-pipeline.git
Navigate to the project directory
cd sql-etl-sales-pipeline
Run the ETL pipeline
python scripts/etl_pipeline.py
This will generate the database:
results/sales_database.db
Example Output Tables
raw_sales
Contains the original dataset.
cleaned_sales
Cleaned version of the dataset after transformation.
sales_summary

Aggregated reporting table with total sales by product line.
Key Learning Outcomes
Building an end-to-end ETL pipeline
Data cleaning using Pandas
Loading structured data into SQL databases
Performing analytical SQL queries
Managing projects with Git and GitHub

Author
Siva Kumar Rongali

B.Tech Computer Science
Aspiring Data Engineer

