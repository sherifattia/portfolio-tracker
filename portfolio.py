import pandas as pd
import yfinance as yf


class Portfolio:
    def __init__(self, transactions):
        self.trades = self._read_transactions(transactions)
        self.holdings = self._generate_holdings()
        self.returns = self._generate_returns()

    def _read_transactions(self, transactions):
        df = pd.read_csv(
            transactions,
            usecols=["date", "symbol", "quantity", "price"],
            index_col=["date"],
            parse_dates=["date"],
            dtype={"symbol": "str", "quantity": "float", "price": "float"},
        )
        df.index.name = "date"
        df = df.sort_values(by=["date"])
        df["cost"] = df.quantity * df.price
        return df

    def _generate_holdings(self):
        df = pd.DataFrame(columns=["symbol", "quantity", "cost"], index=pd.DatetimeIndex(self.trades.index.unique()))
        for date in self.trades.index.unique():
            df.loc[date, "symbol"] = self.trades[self.trades.index == date]["symbol"][0]
            df.loc[date, "quantity"] = self.trades.loc[date, "quantity"].sum()
            df.loc[date, "cost"] = self.trades.loc[date, "cost"].sum()
        return df

    def _generate_returns(self):
        start_date = self.holdings.index.min() + pd.Timedelta(days=1)
        end_date = pd.to_datetime("today") - pd.Timedelta(days=1)
        daterange = pd.date_range(start_date, end_date)
        symbol = yf.Ticker('PLTR')
        prices = symbol.history(start=start_date)
        df = pd.DataFrame(columns=["symbol", "market_value", "cost", "profit", "return"])
        for date in daterange:
            pass
