import streamlit as st
from datalens.data_loader import load_csv

st.title("Data Explorer 📂")
st.write("Upload and explore your dataset.")
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if st.button("Load Dataset", disabled=uploaded_file is None):
    try:
        df = load_csv(uploaded_file)
        st.session_state.original_df = df.copy()
        st.session_state.cleaned_df = df.copy()
        st.session_state.dataset_name = uploaded_file.name
        st.success("Dataset loaded successfully!")

    except Exception as error:
        st.error(f"Could not read the CSV file: {error}")


# Display loaded dataset
df = st.session_state.original_df #this line retrieves the original dataset from the session state and assigns it to the variable df. This allows the app to display the dataset and its details if it has been successfully loaded.

if df is not None:
    st.divider()
    st.subheader("Dataset Overview")
    col1, col2 = st.columns(2)
    col1.metric("Rows", f"{df.shape[0]:,}")
    col2.metric("Columns", f"{df.shape[1]:,}")

    st.subheader("Data Preview")
    st.dataframe(df, width="stretch")