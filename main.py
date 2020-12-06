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
