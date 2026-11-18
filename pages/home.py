import streamlit as st

st.title("Welcome to DataLens 🔎")
st.write("Your personal data analysis and machine learning platform.")

st.divider()

st.subheader("Explore Your Data")
st.write("""DataLens helps you understand, analyze, visualize and prepare your datasets.""")

if st.session_state.original_df is not None: #this line checks if the original_df is not None, meaning a dataset has been loaded into the session state. If a dataset is present, it displays a success message indicating that the dataset has been loaded and shows the name of the dataset stored in st.session_state.dataset_name.
    st.success(f"Dataset loaded: {st.session_state.dataset_name}")

    df = st.session_state.original_df
    col1, col2 = st.columns(2)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

else:
    st.info("Start by uploading a CSV file in Data Explorer.")