import yfinance as yf

data_df = yf.download("^GSPC", start="1990-04-24", end="2023-04-24")
data_df.to_csv('sp500.csv')
