import pandas as pd

class Portfolio:

    def __init__(self):
        self.market_value = 0
        self.assets = []
        self.liabilities = []

    def asset_allocation(self):
        asset_allocation = pd.DataFrame(self.assets, columns=["Name", "Type", "Country", "Value", "Return", "Risk"])
        return asset_allocation

    def asset_type_counter(self, new_asset_class):
        counter = 0
        if len(self.assets) > 0:
            for asset in self.assets:
                if asset[1] == new_asset_class:
                    counter += 1
        return counter

    def add_asset(self, new_asset):
        new_asset_catagory = str(new_asset.asset_class)
        asset_type_count = self.asset_type_counter(new_asset_catagory)
        new_asset_name = new_asset_catagory + str(asset_type_count + 1)
        self.assets.append(
            [new_asset_name, new_asset.asset_class, new_asset.country, new_asset.value, new_asset.potential_annual_return, new_asset.risk])

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
