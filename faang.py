#! /usr/bin/env python

# Date and time handling
import datetime as dt

# Data manipulation
import pandas as pd

# Yahoo Finance data
import yfinance as yf

# Plotting
import matplotlib.pyplot as plt

# Date formatting for plots
import matplotlib.dates as mdates

# Listing files in a folder
import os

# Function to get data and save to CSV
def get_data():
    """Download data and save to CSV file."""

    # Get historical data for the last 5 days
    df = yf.download(('META AAPL AMZN NFLX GOOG'), period='5D', 
                     interval='1h',auto_adjust=False)

    # Create a filename with the current date and time
    filename = 'data/' + dt.datetime.now().strftime('%Y%m%d-%H%M%S') + '.csv'

    # Save data to CSV
    df.to_csv(filename)

    # Return the dataframe
    return df

# Call the function to get data and save to CSV
faang_df = get_data()

# Function to plot data for the latest CSV file
def plot_data():
    """Plot the latest CSV file data."""

    # List files in the 'data' folder
    data_files = os.listdir('data')
    # Sort files by name in descending order
    data_files.sort(reverse=True)
    
    # Read the most recent file
    df = pd.read_csv('data/' + data_files[0], header=[0,1],
                     index_col=0, parse_dates=True)
    # Select Closing prices
    closing_price = df['Close']
    
    # Plot close prices passing
    fig, ax = plt.subplots(figsize=(8, 6))
    closing_price.plot(ax=ax)

    # Set title as date using today's date
    now = dt.datetime.now()
    ax.set_title(now.strftime('%Y-%m-%d'))

    # Set X and Y axes labels
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')

    # X-axis formatting
    # Major ticks: daily markers with Month-Day labels
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
    # Minor ticks: hourly markers without labels
    ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))

    # Y-axis formatting
    ax.yaxis.set_major_formatter('${x:1.2f}')

    # Place legend outside the plot area
    ax.legend(bbox_to_anchor=(1.05, 1),
              loc='upper left', borderaxespad=0.)
    # Add grid
    ax.grid(True)

    # Save the plot to a folder
    # Generate a figure name using the current date and time in .png format
    figure_name =  'plots/' + dt.datetime.now().strftime('%Y%m%d-%H%M%S') + '.png'
    # Save the figure with 300 dpi resolution
    fig.savefig(figure_name,
                dpi = 300,
                bbox_inches='tight')
    
    return closing_price

# Call the function to get data and save to CSV
closing_price = plot_data()
