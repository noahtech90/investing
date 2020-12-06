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

    def net_worth(self):
        return self.total_asset_value() - self.total_liability_value()


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
    asset_two = Asset(3000, 'equity', 'EM', .06, .6)

    liability_one = Liability(1500, .03, 30)
