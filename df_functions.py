import pandas as pd


class PortfolioDataFrame:

    def __init__(self, df):
        self.df = df

    def market_cap(self):
        return self.df['Value'].sum()