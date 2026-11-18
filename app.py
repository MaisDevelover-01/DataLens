import streamlit as st

# Page configuration
st.set_page_config(
    page_title="DataLens",
    page_icon="🔎",
    layout="wide"
)

# Initialize session state
if "original_df" not in st.session_state:
    st.session_state.original_df = None

if "cleaned_df" not in st.session_state:
    st.session_state.cleaned_df = None

if "dataset_name" not in st.session_state:
    st.session_state.dataset_name = None


# Define application pages
home_page = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
    default=True
)

explorer_page = st.Page(
    "pages/data_explorer.py",
    title="Data Explorer",
    icon="📂"
)

quality_page = st.Page(
    "pages/data_quality.py",
    title="Data Quality",
    icon="🔍"
)

visualization_page = st.Page(
    "pages/data_visualization.py",
    title="Data Visualization",
    icon="📊"
)

cleaning_page = st.Page(
    "pages/data_cleaning.py",
    title="Data Cleaning",
    icon="🧹"
)

ml_page = st.Page(
    "pages/machine_learning.py",
    title="Machine Learning",
    icon="🤖"
)
# Navigation
pg = st.navigation(
    [
        home_page,
        explorer_page,
        quality_page,
        visualization_page,
        cleaning_page,
        ml_page
    ],
    position="sidebar"
)

pg.run()