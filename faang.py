#! /usr/bin/env python

# Date and time handling
import datetime as dt

# Data manipulation
import pandas as pd

# Yahoo Finance data
import yfinance as yf

# Download historical data for the last 5 days
# data = yf.download('META AAPL AMZN NFLX GOOG', start = five_days_ago, end = now , interval='1h')
df = yf.download('META AAPL AMZN NFLX GOOG', period='5d', interval='1h')

# Get today's date 
now = dt.datetime.now()

# File name
filename =  'data/' + dt.datetime.now().strftime('%Y%m%d-%H%M%S') + '.csv'

# Save to CSV
df.to_csv(filename)
