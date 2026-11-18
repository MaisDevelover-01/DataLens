import streamlit as st
from datalens.visualization import ( get_numeric_columns, calculate_statistics, create_histogram)

st.title("Data Visualization 📊")
st.write("Explore statistical information and data distributions.")

df = st.session_state.cleaned_df
if df is None:
    st.info("Please upload a dataset first.")
    st.stop()

# Find numerical columns
numeric_columns = get_numeric_columns(df)

if not numeric_columns:
    st.info("No numerical columns found.")
    st.stop()

# Select a column
selected_column = st.selectbox("Select a numerical column:", numeric_columns)

# Calculate statistics
statistics = calculate_statistics(df[selected_column])

if statistics is None:
    st.warning("This column has no valid numerical values.")
    st.stop()

# Display statistics
st.divider()
st.subheader("Statistical Summary")

col1, col2, col3 = st.columns(3)
col1.metric("Count", f"{statistics['count']:,}")
col2.metric("Mean", f"{statistics['mean']:,.2f}")
col3.metric("Median", f"{statistics['median']:,.2f}")

col4, col5, col6 = st.columns(3)
col4.metric("Std.Deviation",
    (
        f"{statistics['std']:,.2f}"
        if statistics["std"] is not None
        else "N/A"
    )
)
col5.metric("Minimum", f"{statistics['min']:,.2f}")
col6.metric( "Maximum", f"{statistics['max']:,.2f}")

# Display histogram
st.divider()
st.subheader("Data Distribution")
fig = create_histogram(df[selected_column], selected_column)
st.plotly_chart(fig, width="stretch")