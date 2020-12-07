# Python investing program to balance asset classes within a portfolio

# Maybe act as a check, examining age of user and various financial ratios to determine what can be improved

# ***pack annual expenses into one liability

import numpy as np
import pandas as pd

class Portfolio:

    def __init__(self):
        self.market_value = 0
        self.assets = []
        self.liabilities = []
        self.asset_distribution = {
            'equity': 0,
            'fixed_income': 0,
            'real_estate': 0,
            'direct_investment': 0,
        }
        self.country_distribution = {
            'US': 5,
            'UK': 2,
            'IN': 2,
            'CH': 1,
        }

    def country_allocation(self):
        country_dataframe = pd.DataFrame([self.country_distribution])
        return country_dataframe

    def add_asset(self, new_asset):
        self.assets.append(new_asset)

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


class Asset:

    def __init__(self, value, asset_class, country, potential_annual_return, risk):
        self.value = value
        self.asset_class = asset_class
        self.country = country
        self.potential_annual_return = potential_annual_return
        self.risk = risk

    def return_value(self):
        return self.value


class Liability:

    def __init__(self, value, interest_rate, contract_length):
        self.value = value
        self.interest_rate = interest_rate
        self.contract_length = contract_length

    def return_value(self):
        return self.value


# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    my_portfolio = Portfolio()

    asset_one = Asset(1000, 'equity', 'US', .1, .4)
    asset_two = Asset(4000, 'equity', 'EM', .06, .6)

    liability_one = Liability(1500, .03, 30)

    my_portfolio.add_asset(asset_one)
    my_portfolio.add_asset(asset_two)
    my_portfolio.add_liability(liability_one)

    print(my_portfolio.net_worth())
    print(type(my_portfolio.country_distribution))
    print(my_portfolio.country_allocation())
