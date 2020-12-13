# Python investing program to balance asset classes within a portfolio

# Maybe act as a check, examining age of user and various financial ratios to determine what can be improved

# ***pack annual expenses into one liability
from portfolio import Portfolio
from assets_liabilities import Asset, Liability

my_portfolio = Portfolio()

asset_one = Asset(1000, 'equity', 'US', .1, .4)
asset_two = Asset(4000, 'equity', 'EM', .06, .6)
asset_three = Asset(1000, 'fixed-income', 'US', .01, .1)

liability_one = Liability(1500, .03, 30)

my_portfolio.add_asset(asset_one)
my_portfolio.add_asset(asset_two)
my_portfolio.add_asset(asset_three)
my_portfolio.add_liability(liability_one)

allocation_dataframe = my_portfolio.country_allocation()
#print(allocation_dataframe)
print(my_portfolio.asset_allocation())
