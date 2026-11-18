import streamlit as st
from datalens.quality import (get_quality_summary, get_column_quality)


st.title("Data Quality 🔍")
st.write("Analyze the quality of your dataset.")

if "original_df" not in st.session_state:
    st.info("Please upload a dataset first")
    st.stop()

df = st.session_state.cleaned_df

if df is None:
    st.info("Please upload a dataset first.")
    st.stop()

# Calculate quality metrics
summary = get_quality_summary(df)

# Display general metrics
st.subheader("Quality Overview")
col1, col2, col3 = st.columns(3)

col1.metric("Missing Cells", f"{summary['missing_cells']:,}")
col2.metric("Duplicate Rows", f"{summary['duplicate_rows']:,}")
col3.metric("Complete Cells", f"{summary['complete_cells']:,}")

st.caption(f"Missing cells represent " f"{summary['missing_percentage']:.1f}% ""of all cells.")

# Display column quality
st.divider()
st.subheader("Column Quality")

if df.shape[1] > 0:
    quality_report = get_column_quality(df)
    st.dataframe(quality_report,hide_index=True, width="stretch")
else:
    st.info("The dataset has no columns.")