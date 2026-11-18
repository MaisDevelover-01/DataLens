import pandas as pd

def fill_missing_values(df, column, strategy, value=None):
    """
    Handle missing values in a selected column.
    """
    if column not in df.columns:
        raise ValueError("Column does not exist.")

    result = df.copy() #Don't want to change the og dataset
    missing_count = int(result[column].isna().sum())

    if missing_count == 0:
        return result, 0

    valid_values = result[column].dropna() #valid values for calculatin mean and mode

    # Mean Imputation
    if strategy == "mean":
        if not pd.api.types.is_numeric_dtype(result[column]):
            raise TypeError("Mean requires numerical data.")
        
        if valid_values.empty:
            raise ValueError("No valid values available.")

        fill_value = valid_values.mean()

    # Median Imputation
    elif strategy == "median":

        if not pd.api.types.is_numeric_dtype(result[column]):
            raise TypeError("Median requires numerical data.")

        if valid_values.empty:
            raise ValueError("No valid values available.")

        fill_value = valid_values.median()

    # Mode Imputation
    elif strategy == "mode":
        modes = valid_values.mode()

        if modes.empty:
            raise ValueError("No valid values available.")

        fill_value = modes.iloc[0]

    # Custom Value Imputation
    elif strategy == "constant":

        if value is None:
            raise ValueError("A replacement value is required.")

        fill_value = value

    # Drop Rows
    elif strategy == "drop_rows":

        result = result.dropna( subset=[column]).copy()
        removed_rows = len(df) - len(result)
        return result, removed_rows

    else:
        raise ValueError("Invalid cleaning strategy.")

    result[column] = result[column].fillna(fill_value)
    return result, missing_count

def count_duplicate_rows(df, subset=None):
    """
    Count duplicate rows.
    """
    return int(df.duplicated(subset=subset).sum())

def remove_duplicate_rows(df, subset=None, keep="first"):
    """
    Remove duplicate rows from the dataset.
    """
    result = df.drop_duplicates(subset=subset, keep=keep).copy()
    removed_count = len(df) - len(result)
    return result, removed_count