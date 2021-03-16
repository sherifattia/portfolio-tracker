import pandas as pd
import yfinance


class Portfolio:
    def __init__(self, transactions):
        self.trades = pd.read_csv(
            transactions,
            usecols=["Date", "Symbol", "Quantity", "Price"],
            index_col=["Date"],
            parse_dates=["Date"],
            dtype={"Symbol": "str", "Quantity": "float", "Price": "float"},
        )
        self.trades = self.trades.rename(
            columns={"Date": "date", "Symbol": "symbol", "Quantity": "quantity", "Price": "price"}
        )
        self.trades = self.trades.sort_values(by="date")
        self.holdings = self._generate_holdings()

    def _generate_holdings(self):
        pass
