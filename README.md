# computer-infrastructure
by Oksana Abrosimova

This repository contains a Jupyter Notebook created as part of the *Computer Infrastructure* module within the *Programming for Data Analytics* course. The project automates downloading hourly FAANG stock data, plotting their closing prices, and generating time-stamped CSV and PNG files. It also includes a Python script and a GitHub Actions workflow that runs the full process automatically each week.

## Required Software
- **Python** - The programming language required to run the script and Notebook. Download from Python.org.
- **Github Codespaces** - A cloud-based development environment provided by GitHub that supports running Jupyter Notebooks directly in the browser. Accessible via the "Code" dropdown in this repository.
- **Jupyter** (alternative to Codespaces) - An environment for writing and running code, performing data analysis, and creating visualisations. For installation instructions, refer to the official Jupyter documentation.

## Required Packages
All packages are imported and explained in the Notebook. Quick overview:
- **datetime** – For handling and formatting date/time values.
- **pandas** - For working with DataFrames and performing data manipulation.
- **yfinance** – For fetching and downloading stock market data.
- matplotlib.pyplot – For generating plots and visualisations.

## Project Structure
- **README.md** - Project overview and setup instructions.
- **problems.ipynb** - Jupyter notebook containing the project work.
- **requirements.txt** - List of requirements.