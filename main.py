# Python investing program to balance asset classes within a portfolio

# Maybe act as a check, examining age of user and various financial ratios to determine what can be improved

# ***pack annual expenses into one liability
from portfolio import Portfolio
from assets_liabilities import Asset, Liability
from df_functions import percentage_country, percentage_asset

my_portfolio = Portfolio()

asset_one = Asset(1000, 'equity', 'US', .1, .4)
asset_two = Asset(4000, 'equity', 'US', .06, .6)
asset_three = Asset(1000, 'equity', 'US', .01, .1)
asset_four = Asset(2000, 'fixed-income', 'EM', .01, .1)
asset_five = Asset(5000, 'fixed-income', 'US', .01, .1)

liability_one = Liability(1500, .03, 30)
liability_two = Liability(6500, .03, 30)

my_portfolio.add_asset(asset_one)
my_portfolio.add_asset(asset_two)
my_portfolio.add_asset(asset_four)
my_portfolio.add_asset(asset_three)
my_portfolio.add_asset(asset_five)
# my_portfolio.add_liability(liability_one)
# my_portfolio.add_liability(liability_two)

# portfolio_dataframe = PortfolioDataFrame(my_portfolio.generate_dataframe())
pd = my_portfolio.generate_dataframe()

print(percentage_country(pd))
print(percentage_asset(pd))



