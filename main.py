# Python investing program to balance asset classes within a portfolio

# Maybe act as a check, examining age of user and various financial ratios to determine what can be improved

import time
import os
import pandas
import openpyxl

from portfolio import Portfolio
from assets_liabilities import Asset, Liability
from df_functions import percentage_country, percentage_asset, total_risk, potential_annual_return, total_assets

# Establish Portfolio Class
my_portfolio = Portfolio()
# Create Assets
asset_one = Asset(7000, 'equity', 'US', .1, .1)
asset_two = Asset(1000, 'fixed-income', 'EM', .05, .2)
asset_three = Asset(4000, 'equity', 'US', .05, .2)
# Create Liabilities
liability_one = Liability(1500, .03, 30)
liability_two = Liability(6500, .03, 30)
# Add Assets to Portfolio
my_portfolio.add_asset(asset_one)
my_portfolio.add_asset(asset_two)
my_portfolio.add_asset(asset_three)
# Add Liabilities to Portfolio
my_portfolio.add_liability(liability_one)
my_portfolio.add_liability(liability_two)
# Create Asset and Liabilities Dataframes
pd_assets = my_portfolio.asset_dataframe()
pd_liability = my_portfolio.liability_dataframe()
# Run analysis on Portfolio
country_distributon = percentage_country(pd_assets)
asset_distribution = percentage_asset(pd_assets)
portfolio_risk = round(total_risk(pd_assets), 3)
potential_return = round(potential_annual_return(pd_assets), 3)

excel_loc = "C:\\Users\\Noah\\PycharmProjects\\investing\\portfolio.xlsx"

if os.path.exists(excel_loc):
    os.remove(excel_loc)

with pandas.ExcelWriter('portfolio.xlsx') as writer:
    pd_assets.to_excel(writer, sheet_name="assets")
    pd_liability.to_excel(writer, sheet_name="liabilities")

my_workbook = openpyxl.load_workbook(excel_loc)

my_worksheet = my_workbook["assets"]
my_worksheet["K4"] = "Test"
my_workbook.save(excel_loc)
