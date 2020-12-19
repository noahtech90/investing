import pandas as pd


class Portfolio:

    def __init__(self):
        self.market_value = 0
        self.assets = []
        self.liabilities = []

    def generate_dataframe(self):
        asset_allocation = pd.DataFrame(self.assets, columns=["Name", "Category", "Type", "Country", "Value", "Return","Risk"])
        return asset_allocation

    def asset_type_counter(self, new_asset_class):
        counter = 0
        if len(self.assets) > 0:
            for asset in self.assets:
                if asset[1] == new_asset_class:
                    counter += 1
        return counter

    def add_asset(self, new_asset):
        asset_type_count = self.asset_type_counter(new_asset.asset_class)
        new_asset_name = new_asset.asset_class + str(asset_type_count + 1)
        self.assets.append(
            [new_asset_name, "asset", new_asset.asset_class, new_asset.country, new_asset.value,
             new_asset.potential_annual_return, new_asset.risk])

    def add_liability(self, new_liability):
        self.liabilities.append(new_liability)

