# DataLens

**A Python-based application for exploring, analyzing, visualizing, and cleaning CSV datasets.**

DataLens is a multi-page data analysis app built with Streamlit, Pandas, and Plotly. It provides a simple interface for loading a CSV file, inspecting data quality, viewing basic statistics, exploring a numerical column's distribution, and applying selected cleaning operations.

> **Project status:** Early development — `v0.1.0` scope. Some planned features, including outlier treatment and machine-learning workflows, are not implemented yet.

## Features

### Data Explorer

- Upload a CSV file.
- Preview the dataset in an interactive table.
- View the number of rows and columns.

### Data Quality

- Count missing cells and duplicate rows.
- Calculate the percentage of missing cells.
- Inspect each column's data type, non-null values, and missing values.

### Data Visualization

- Select a numerical column.
- View basic descriptive statistics: count, mean, median, standard deviation, minimum, and maximum.
- Explore the selected column's distribution with an interactive Plotly histogram.

### Data Cleaning

- Fill missing values using the mean, median, mode, or a custom value (where applicable).
- Drop rows with missing values in a selected column.
- Detect and remove duplicate rows, optionally using selected columns to define duplicates.
- Reset the working dataset to the originally uploaded dataset.
- Download the cleaned dataset as a CSV file.

## Tech Stack

- **Python** — application language
- **Streamlit** — multi-page web interface
- **Pandas** — data loading, analysis, and cleaning
- **Plotly Express** — interactive data visualization

## Project Structure

```text
DataLens/
├── app.py
├── pages/
│   ├── home.py
│   ├── data_explorer.py
│   ├── data_quality.py
│   ├── data_visualization.py
│   ├── data_cleaning.py
│   └── machine_learning.py
├── datalens/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── quality.py
│   ├── visualization.py
│   └── cleaning.py
├── sample_data/
│   └── sample_quality.csv
├── tests/
│   ├── test_quality.py
│   └── test_cleaning.py
├── requirements.txt
├── .gitignore
└── README.md
```

The `pages/` directory contains the Streamlit pages. The `datalens/` package contains reusable data-loading, quality-analysis, visualization, and cleaning functions.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<YOUR-USERNAME>/DataLens.git
cd DataLens
```

Replace `<YOUR-USERNAME>` with your GitHub username.

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, you can run the app using the virtual environment's Python executable directly (see step 5), without activating it.

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Check the sample dataset

A small sample CSV is provided in `sample_data/sample_quality.csv`. You can use it to try the upload, quality-report, visualization, and cleaning workflows.

### 5. Run the application

With the virtual environment activated:

```bash
python -m streamlit run app.py
```

On Windows, you can also run it without activating the environment:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Streamlit will start a local server and provide a URL to open the app in your browser.

## Typical Workflow

1. Open **Data Explorer** and upload a CSV file.
2. Review the dataset in **Data Quality**.
3. Explore numerical columns in **Data Visualization**.
4. Use **Data Cleaning** to apply the cleaning operations you choose.
5. Download the cleaned dataset as a CSV file.

The app keeps the originally uploaded DataFrame separate from the working cleaned DataFrame during the current Streamlit session, so you can reset the working data to the original upload.

## Current Limitations

- CSV files are currently supported by the upload workflow.
- Data-cleaning operations are basic and should be reviewed before using the output for important decisions.
- Outlier detection and treatment are not implemented yet.
- Advanced chart selection, automated cleaning recommendations, AI assistance, and machine-learning model training are planned, not current features.
- Session State is temporary application-session storage; it is not a persistent database or long-term file store.
- Automated test coverage has not been implemented yet; the `tests/` files are currently placeholders.
- The project is an early-stage learning and development project, not a production data-governance system.

## Roadmap

- [ ] Add outlier detection and configurable treatment methods.
- [ ] Expand visualization options (bar, scatter, line, and box plots).
- [ ] Add before-and-after cleaning comparisons.
- [ ] Add automated data-cleaning recommendations.
- [ ] Explore an AI-assisted cleaning assistant.
- [ ] Add machine-learning workflows for regression, classification, and clustering.
- [ ] Expand automated tests and documentation.

## Contributing

Suggestions, bug reports, and contributions are welcome. For significant changes, open an issue first to discuss the proposed change.

## License

No license has been selected yet. Until a license is added to this repository, please do not assume that the code is available for unrestricted reuse, modification, or redistribution.
