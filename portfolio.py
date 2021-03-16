import pandas as pd
import yfinance


class Portfolio:
    def __init__(self, transactions):
        self._trades = pd.read_csv(transactions, usecols=["Date", "Symbol", "Quantity", "Price"], index_col="Date")
