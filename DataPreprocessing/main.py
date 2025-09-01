# main.py
import file_handler as fh
import preprocessing as pp

# Example CSV file (you can replace with your own data file)
sample_data = {
    "Name": ["Ali", "Mona", "Sara", "Omar", None],
    "Age": [20, 22, None, 24, 23],
    "Grade": ["A", "B", "B", None, "A"]
}

import pandas as pd
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
