import pandas as pd
import random

class Portfolio:

    def __init__(self):
        self.market_value = 0
        self.assets = []
        self.liabilities = []
        self.asset_distribution = {
            'Name': [],
            'Type': []
        }
        self.country_distribution = {
        }

    def country_allocation(self):
        country_dataframe = pd.DataFrame([self.country_distribution])
        return country_dataframe

    def asset_allocation(self):
        asset_allocation = pd.DataFrame([self.asset_distribution])
        return asset_allocation

    def asset_type_counter(self, new_asset_class):
        counter = 0
        for asset in self.assets:
            if asset.asset_class == new_asset_class:
                counter += 1
        return counter

    def add_asset(self, new_asset):
        new_asset_catagory = str(new_asset.asset_class)
        asset_type_count = self.asset_type_counter(new_asset_catagory)
        self.assets.append(new_asset)
        self.asset_distribution[new_asset_catagory + str(asset_type_count + 1)] = new_asset.value

    def add_liability(self, new_liability):
        self.liabilities.append(new_liability)

    def total_asset_value(self):
        market_value = 0
        for asset in self.assets:
            market_value += asset.value
        return market_value

    def total_liability_value(self):
        liability_value = 0
        for liability in self.liabilities:
            liability_value += liability.value
        return liability_value

    def net_worth(self):
        net_worth = self.total_asset_value() - self.total_liability_value()
        print(f"Net Worth: {net_worth}")
        return net_worth
