import pandas as pd
import plotly.express as px


def get_numeric_columns(df):
    """
    Return the names of numerical columns.
    """
    return df.select_dtypes(include="number").columns.tolist()

def calculate_statistics(series):
    """
    Calculate statistical metrics for a numerical column.
    """
    data = series.dropna()
    if data.empty:
        return None

    return {
        "count": int(data.count()),
        "mean": float(data.mean()),
        "median": float(data.median()),
        "std": (float(data.std()) if data.count() > 1 else None),
        "min": float(data.min()),
        "max": float(data.max())
    }

def create_histogram(series, column_name, bins=20):
    """
    Create an interactive histogram using Plotly Express.
    """
    data = series.dropna()
    fig = px.histogram(
        x=data,
        nbins=bins,
        title=f"Distribution of {column_name}"
    )
    fig.update_layout(xaxis_title=column_name, yaxis_title="Frequency")
    return fig