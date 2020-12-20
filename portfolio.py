import pandas as pd


# Portfolio class holds assets & liabilities and generates a dataframe

class Portfolio:

    def __init__(self):
        self.market_value = 0
        self.assets = []
        self.liabilities = []

    def asset_dataframe(self):
        asset_allocation = pd.DataFrame(self.assets,
                                        columns=["Name", "Category", "Type", "Country", "Value", "Return", "Risk"])
        return asset_allocation

    def liability_dataframe(self):
        liability_allocation = pd.DataFrame(self.liabilities,
                                            columns=["Name", "Category", "Value", "Interest Rate", "Contract Length"])
        return liability_allocation

    def asset_type_counter(self, new_asset_class):
        counter = 0
        if len(self.assets) > 0:
            for asset in self.assets:
                # asset 2 holds type of equity, this should probably be replaced with a dictionary
                if asset[2] == new_asset_class:
                    counter += 1
        return counter

    def add_asset(self, new_asset):
        asset_type_count = self.asset_type_counter(new_asset.asset_class)
        new_asset_name = new_asset.asset_class + str(asset_type_count + 1)
        self.assets.append(
            [new_asset_name, "asset", new_asset.asset_class, new_asset.country, new_asset.value,
             new_asset.potential_annual_return, new_asset.risk])

    def add_liability(self, new_liability):
        liability_type_count = len(self.liabilities)
        new_liability_name = "liability" + str(liability_type_count + 1)
        self.liabilities.append(
            [new_liability_name, "liability", new_liability.value,
             new_liability.interest_rate, new_liability.contract_length])
