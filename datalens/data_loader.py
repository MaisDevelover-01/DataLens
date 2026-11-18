import pandas as pd

def load_csv(uploaded_file):
    """
    Read an uploaded CSV file and return a DataFrame.
    """
    uploaded_file.seek(0)# Reset the file pointer to the beginning of the file before reading it. This ensures that the entire file is read, especially if it has been read or processed before this function is called.
    df = pd.read_csv(uploaded_file)
    return df