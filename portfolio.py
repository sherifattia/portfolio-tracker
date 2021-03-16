import pandas as pd
import yfinance


class Portfolio:
    def __init__(self, transactions):
        self.trades = self._read_transactions(transactions)
        self.holdings = self._generate_holdings()

    def _read_transactions(self, transactions):
        df = pd.read_csv(
            transactions,
            usecols=["Date", "Symbol", "Quantity", "Price"],
            index_col=["Date"],
            parse_dates=["Date"],
            dtype={"Symbol": "str", "Quantity": "float", "Price": "float"},
        )
        df = df.rename(columns={"Symbol": "symbol", "Quantity": "quantity", "Price": "price"})
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
