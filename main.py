# Python investing program to balance asset classes within a portfolio

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
    def total_market_value(self):
        market_value = 0
        for asset in self.assets:
            market_value += asset.value
        return market_value


    def total_liability_value(self):
        liability_value = 0
        for liability in self.liabilities:
            liability_value += liability.value
        return liability_value

class Asset:

    def __init__(self):
        self.value = 0
        self.asset_class = None
        self.country = None
        self.potential_annual_return = None
        self.risk = None


class Liability:

    def __init__(self):
        self.value = 0
        self.interest_rate = 0.03
        self.contract_length = 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("lets go")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
