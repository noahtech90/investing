# Python investing program to balance asset classes within a portfolio

# Maybe act as a check, examining age of user and various financial ratios to determine what can be improved

# ***pack annual expenses into one liability
from portfolio import Portfolio
from assets_liabilities import Asset, Liability

my_portfolio = Portfolio()

asset_one = Asset(1000, 'equity', 'US', .1, .4)
asset_two = Asset(4000, 'equity', 'EM', .06, .6)
asset_three = Asset(1000, 'fixed-income', 'US', .01, .1)
asset_four = Asset(2000, 'fixed-income', 'US', .01, .1)
asset_five = Asset(5000, 'fixed-income', 'US', .01, .1)

liability_one = Liability(1500, .03, 30)
liability_two = Liability(6500, .03, 30)

my_portfolio.add_asset(asset_one)
my_portfolio.add_asset(asset_two)
my_portfolio.add_asset(asset_five)
my_portfolio.add_liability(liability_one)
my_portfolio.add_liability(liability_two)

asset_df = my_portfolio.asset_allocation()
print(asset_df)
