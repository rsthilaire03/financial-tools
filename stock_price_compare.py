import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Function to fetch historical stock data
def get_stock_data(stock_symbol, start_date, end_date):
    stock = yf.Ticker(stock_symbol)
    stock_data = stock.history(start=start_date, end=end_date)
    return stock_data

# Function to plot stock data
def plot_stock_data(stock_data, label):
    plt.plot(stock_data.index, stock_data["Close"], label=label)

# Specify the list of stocks and date range
stock_symbols = ["TSLA", "AAPL", "GOOGL", "MSFT"]  # Replace with your desired stock symbols
start_date = "2021-01-01"  # Replace with your desired start date
end_date = "2023-01-01"    # Replace with your desired end date

# Fetch and plot historical stock data for each stock
plt.figure(figsize=(12, 6))

for stock_symbol in stock_symbols:
    stock_data = get_stock_data(stock_symbol, start_date, end_date)
    plot_stock_data(stock_data, stock_symbol)

# Customize the plot
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.title("Stock Price Comparison")
plt.grid(True)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()


