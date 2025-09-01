# main.py
"""
📊 Data Analysis Basics

This script demonstrates:
- Reading and saving data in different formats (CSV, XLSX, JSON, DB).
- Checking and converting column data types.
- Detecting and handling missing values (fill with mean/median/mode, or drop).
- Exporting cleaned data.

▶️ How to Run:
    python main.py

✨ Features:
- Read/Write: CSV, Excel (XLSX), JSON, Database (SQLite).
- Check and convert data types.
- Detect missing values.
- Fill or drop missing values.
- Modular design for reuse in other projects.
"""

import file_handler as fh
import preprocessing as pp
import pandas as pd

# Example dataset (instead of reading from file)
sample_data = {
    "Name": ["Ali", "Mona", "Sara", "Omar", None],
    "Age": [20, 22, None, 24, 23],
    "Grade": ["A", "B", "B", None, "A"]
}

df = pd.DataFrame(sample_data)

print("=== Original Data ===")
print(df)

# Check column types
print("\n=== Column Types ===")
print(pp.check_dtypes(df))

# Check missing values
print("\n=== Missing Values ===")
print(pp.check_missing(df))

# Fill missing values in Age with mean
df = pp.fill_missing(df, column="Age", method="mean")

# Drop rows with missing values in any column
df = pp.drop_missing(df)

print("\n=== Cleaned Data ===")
print(df)

# Save cleaned data to Excel
fh.save_excel(df, "cleaned_data.xlsx")
print("\n✅ Cleaned data saved to cleaned_data.xlsx")
