# Python investing program to balance asset classes within a portfolio

# Maybe act as a check, examining age of user and various financial ratios to determine what can be improved

# ***pack annual expenses into one liability
from portfolio import Portfolio
from assets_liabilities import Asset, Liability
from df_functions import percentage_country, percentage_asset, total_risk, potential_annual_return

my_portfolio = Portfolio()

asset_one = Asset(7000, 'equity', 'US', .1, .1)
asset_two = Asset(1000, 'fixed-income', 'EM', .05, .2)


liability_one = Liability(1500, .03, 30)
liability_two = Liability(6500, .03, 30)

my_portfolio.add_asset(asset_one)
my_portfolio.add_asset(asset_two)

my_portfolio.add_liability(liability_one)
my_portfolio.add_liability(liability_two)

pd = my_portfolio.generate_dataframe()

print(f"\nAssets By Country: {percentage_country(pd)} \n")
print(f"Asset Allocation: {percentage_asset(pd)} \n")
print(f"Total Risk of Assets: {round(total_risk(pd), 3)}")

# Return weighted by market cap
print(f"Potential Return of Assets: {round(potential_annual_return(pd), 3)}")


