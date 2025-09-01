# file_handler.py
import pandas as pd
import sqlite3

# ========== READ FUNCTIONS ==========

def read_csv(file_path):
    """Read data from CSV file."""
    return pd.read_csv(file_path)

def read_excel(file_path, sheet_name=0):
    """Read data from Excel file."""
    return pd.read_excel(file_path, sheet_name=sheet_name)

def read_json(file_path):
    """Read data from JSON file."""
    return pd.read_json(file_path)

def read_db(db_path, table_name):
    """Read data from a database table (SQLite)."""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df


# ========== SAVE FUNCTIONS ==========

def save_csv(df, file_path):
    """Save DataFrame to CSV file."""
    df.to_csv(file_path, index=False)

def save_excel(df, file_path, sheet_name="Sheet1"):
    """Save DataFrame to Excel file."""
    df.to_excel(file_path, index=False, sheet_name=sheet_name)

def save_json(df, file_path):
    """Save DataFrame to JSON file."""
    df.to_json(file_path, orient="records", indent=4)

def save_db(df, db_path, table_name):
    """Save DataFrame to database table (SQLite)."""
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
