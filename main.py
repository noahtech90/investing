# Python investing program to balance asset classes within a portfolio

# Maybe act as a check, examining age of user and various financial ratios to determine what can be improved

# ***pack annual expenses into one liability

from portfolio import Portfolio
from assets_liabilities import Asset, Liability


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    my_portfolio = Portfolio()

    asset_one = Asset(1000, 'equity', 'US', .1, .4)
    asset_two = Asset(4000, 'equity', 'EM', .06, .6)

    liability_one = Liability(1500, .03, 30)

    my_portfolio.add_asset(asset_one)
    my_portfolio.add_asset(asset_two)
    my_portfolio.add_liability(liability_one)

    #print(my_portfolio.net_worth())
    allocation_dataframe = my_portfolio.country_allocation()
    print(allocation_dataframe['country'].sum())
