# preprocessing.py
import pandas as pd

# ========== DATA TYPE CHECKING ==========

def check_dtypes(df):
    """Return data types of DataFrame columns."""
    return df.dtypes

def convert_dtype(df, column, new_type):
    """Convert column data type."""
    df[column] = df[column].astype(new_type)
    return df


# ========== MISSING VALUES ==========

def check_missing(df):
    """Return count of missing values per column."""
    return df.isnull().sum()

def fill_missing(df, column, method="mean"):
    """Fill missing values in a column using mean/median/mode."""
    if method == "mean":
        value = df[column].mean()
    elif method == "median":
        value = df[column].median()
    elif method == "mode":
        value = df[column].mode()[0]
    else:
        raise ValueError("Method must be 'mean', 'median', or 'mode'")
    
    df[column].fillna(value, inplace=True)
    return df

def drop_missing(df):
    """Drop rows with any missing values."""
    return df.dropna()
