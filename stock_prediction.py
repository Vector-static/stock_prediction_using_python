import yfinance as yf

def get_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    return stock.history(start=start_date, end=end_date)

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOGL']
    start_date = '2020-01-01'
    end_date = '2021-01-01'

    portfolio = {}
    for ticker in tickers:
        portfolio[ticker] = get_stock_data(ticker, start_date, end_date)

    for ticker, data in portfolio.items():
        print(f"\n{ticker} Data:")
        print(data.head()) #print 5 rows
