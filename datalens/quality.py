import pandas as pd


def get_quality_summary(df):
    """
    Calculate general data quality metrics.
    """
    total_rows = df.shape[0]
    total_columns = df.shape[1]
    total_cells = total_rows * total_columns
    missing_cells = int(df.isna().sum().sum())
    duplicate_rows = int(df.duplicated().sum())
    complete_cells = total_cells - missing_cells

    if total_cells > 0:
        missing_percentage = (missing_cells / total_cells) * 100
    else:
        missing_percentage = 0

    return {
        "total_rows": total_rows,
        "total_columns": total_columns,
        "total_cells": total_cells,
        "missing_cells": missing_cells,
        "duplicate_rows": duplicate_rows,
        "complete_cells": complete_cells,
        "missing_percentage": missing_percentage
    }


def get_column_quality(df):
    """
    Generate a quality report for each column.
    """
    missing_by_column = df.isna().sum()

    if df.shape[0] > 0:
        missing_percentages = (df.isna().mean() * 100).round(1)
    else:
        missing_percentages = pd.Series(0.0,index=df.columns)

    quality_report = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str).to_numpy(),
        "Non-null Values": (df.notna().sum().to_numpy()),
        "Missing Values": ( missing_by_column.to_numpy()),
        "Missing (%)": (missing_percentages.to_numpy())
    })

    return quality_report