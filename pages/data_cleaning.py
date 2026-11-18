import pandas as pd
import streamlit as st
from pathlib import Path
from datalens.cleaning import (fill_missing_values, count_duplicate_rows, remove_duplicate_rows)

st.title("Data Cleaning 🧹")
st.write("Clean and prepare your dataset for further analysis.")

# Check dataset availability
if st.session_state.original_df is None:
    st.info("Please upload a dataset first.")
    st.stop()

# Reset dataset
if st.button("Reset to Original Dataset"):
    st.session_state.cleaned_df = (st.session_state.original_df.copy())
    st.success("Dataset restored successfully!")

df = st.session_state.cleaned_df

st.divider()

# 1. Missing Values
st.header("1. Missing Values")
missing_columns = df.columns[df.isna().any()].tolist()

if not missing_columns:
    st.success("No missing values found!")
else:
    st.write("Select a column and choose a cleaning strategy.")

    selected_column = st.selectbox(
        "Select Column",
        missing_columns,
        key="missing_column"
    )

    is_numeric = pd.api.types.is_numeric_dtype(
        df[selected_column]
    )

    has_valid_values = df[selected_column].notna().any()
    strategy_options = {}

    if is_numeric and has_valid_values:
        strategy_options["Mean"] = "mean"
        strategy_options["Median"] = "median"

    if has_valid_values:
        strategy_options["Mode"] = "mode"

    strategy_options["Custom Value"] = "constant"
    strategy_options["Drop Rows"] = "drop_rows"

    selected_strategy = st.selectbox(
        "Select Cleaning Strategy",
        list(strategy_options.keys()),
        key="missing_strategy"
    )
    strategy = strategy_options[selected_strategy]

    custom_value = None
    if strategy == "constant":
        if is_numeric:
            custom_value = st.number_input(
                "Enter replacement value",
                value=0.0
            )
        else:
            custom_value = st.text_input(
                "Enter replacement value",
                value="Unknown"
            )

    if st.button("Apply Missing Value Treatment"):
        try:
            cleaned_df, changed_count = fill_missing_values(
                df,
                selected_column,
                strategy,
                custom_value
            )

            st.session_state.cleaned_df = cleaned_df
            df = cleaned_df

            if strategy == "drop_rows":
                st.success(
                    f"{changed_count} rows removed successfully!"
                )
            else:

                st.success(
                    f"{changed_count} missing values filled successfully!"
                )
        except (ValueError, TypeError) as error:

            st.error(str(error))


st.divider()

# 2. Duplicate Rows
st.header("2. Duplicate Rows")
duplicate_columns = st.multiselect(
    "Select columns for duplicate detection (optional)",
    options=df.columns.tolist(),
    help="Leave empty to check entire rows.",
    key="duplicate_columns"
)

subset = duplicate_columns if duplicate_columns else None

duplicate_count = count_duplicate_rows(df, subset=subset)

st.metric(
    "Duplicate Rows Found",
    duplicate_count
)

if duplicate_count > 0:
    keep_option = st.selectbox(
        "Which duplicate row should be kept?",
        ["First", "Last", "None"],
        key="duplicate_keep"
    )
    keep_mapping = {
        "First": "first",
        "Last": "last",
        "None": False
    }
    if st.button("Remove Duplicate Rows"):

        cleaned_df, removed_count = remove_duplicate_rows(
            df,
            subset=subset,
            keep=keep_mapping[keep_option]
        )
        st.session_state.cleaned_df = cleaned_df
        df = cleaned_df
        st.success(
            f"{removed_count} duplicate rows removed!"
        )
else:
    st.success("No duplicate rows found!")

st.divider()

# 3. Dataset Preview
st.header("Current Cleaned Dataset")
st.write(f"Rows: {df.shape[0]:,}")
st.write(f"Columns: {df.shape[1]:,}")
st.dataframe(df, width="stretch")

st.divider()

# 4. Outliers (Coming Soon)
st.header("4. Outlier Detection")

st.info(
    "Outlier detection and treatment will be added in the next development stage."
)

st.divider()

# 5. Export Cleaned Dataset
st.header("5. Export Cleaned Dataset")
st.write("Download your cleaned dataset as a CSV file.")

# Get original filename
original_name = ( st.session_state.dataset_name or "dataset.csv")

# Generate output filename
file_stem = Path(original_name).stem #استخراج نام فایل بدون پسوند
output_filename = f"{file_stem}_cleaned.csv"

# Convert DataFrame to CSV bytes
csv_data = df.to_csv(index=False).encode("utf-8-sig")

# Download button
st.download_button(
    label="📥 Download Cleaned CSV",
    data=csv_data,
    file_name=output_filename,
    mime="text/csv",
    help="Download the cleaned dataset without the DataFrame index."
)
st.caption("Your original dataset remains unchanged.")