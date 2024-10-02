import yfinance as yf
import pandas as pd

ford = yf.Ticker("F")
stock_data = yf.download("F", period='1y')

print(stock_data)

stock_data.to_csv('ford_stock_data.csv')
#stock_data.to_json('ford_stock_data.json', orient='records', date_format='iso')
print("Data saved to ford_stock_data.csv")