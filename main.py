# Python investing program to balance asset classes within a portfolio

class Portfolio:

    def __init__(self):
        self.market_value = 0
        self.asset_distribution = {
            'equity': 0,
            'fixed_income': 0,
            'real_estate': 0,
            'direct_investment': 0,
        }
        self.country_distribution = {
            "US": 0,
            "UK": 0,

        }


class Asset:

    def __init__(self):
        self.asset_class = None
        self.country = None
        self.value = None
        self.potential_annual_return = None
        self.risk = None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("lets go")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
