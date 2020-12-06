# Python investing program to balance asset classes within a portfolio

# ***pack annual expenses into one liability

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
            'US', 0,
            'UK', 0,
            'IN', 0,
            'CH', 0,
        }

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

    def net_worth(self, assets, liabilities):
        return assets - liabilities



class Asset:

    def __init__(self):
        self.value = 0
        self.asset_class = None
        self.country = None
        self.potential_annual_return = None
        self.risk = None

    def return_value(self):
        return self.value


class Liability:

    def __init__(self):
        self.value = 0
        self.interest_rate = 0.00
        self.contract_length = 0

    def return_value(self):
        return self.value

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("let's go")

