# 💎 Diamond Price Analysis Dashboard

## Project Overview
The Diamond Price Analysis Dashboard is an interactive data analysis project built with Python. It helps users explore diamond prices based on carat weight, color, cut quality, and price range.

The dashboard uses interactive filters, summary metrics, and visualizations to make diamond data easier to understand.

## Features
- Filter diamonds by carat weight.
- Filter by diamond color and cut quality.
- Select a price range.
- View the number of matching diamonds.
- Display average and highest diamond prices.
- Explore diamond prices using interactive charts.
- View filtered diamond records in a table.
- Download filtered data as a CSV file.
- View a summary of average, minimum, and maximum prices.

## Technologies Used
- Python
- Pandas
- Streamlit
- Plotly

## Project Structure
```text
Project_for_python/
├── analysis.py
├── requirements.txt
├── README.md
└── data/
    └── diamonds.csv
```

## Installation and Setup

### 1. Clone or Download the Project
Download the project files to your computer.

### 2. Open the Project Folder
Open the project folder in VS Code and open its terminal.

### 3. Install the Required Libraries
```bash
python -m pip install -r requirements.txt
```

### 4. Run the Dashboard
```bash
python -m streamlit run analysis.py
```

### 5. Open the Dashboard
Streamlit will provide a local URL, usually:

`http://localhost:8501`

Open that URL in your web browser if it does not open automatically.

## How to Use
1. Run the application.
2. Select the desired carat range.
3. Choose a diamond color and cut quality.
4. Adjust the price range.
5. Review the updated metrics, table, and charts.
6. Download the filtered data if needed.

## Learning Objectives
This project demonstrates practical skills in:
- Data loading and cleaning with Pandas.
- Data filtering and aggregation.
- Interactive dashboard development with Streamlit.
- Data visualization with Plotly.
- Exporting filtered data to CSV.

## Future Improvements
- Add more interactive filters.
- Improve dashboard styling and layout.
- Add additional statistical analyses.
- Deploy the dashboard online.

## Author
**Faisa Waleed**

## License
This project is intended for educational and portfolio purposes. Check the dataset's original license before redistributing the data.
