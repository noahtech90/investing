
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
            'country': {
                'US': 5,
                'UK': 2,
                'IN': 2,
                'CH': 1,
            }
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