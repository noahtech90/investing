# Python investing program to balance asset classes within a portfolio

# Maybe act as a check, examining age of user and various financial ratios to determine what can be improved

import time
import os
import pandas
import openpyxl

from portfolio import Portfolio
from assets_liabilities import Asset, Liability
from df_functions import percentage_country, percentage_asset, total_risk, \
    potential_annual_return, total_assets, future_value, potential_risk
from excel_reformat import format_excel

# Establish Portfolio Class
my_portfolio = Portfolio()
# Create Assets
asset_one = Asset(7000, 'Equity', 'US', .5, .1)
asset_two = Asset(1000, 'Fixed', 'EM', .3, .2)
asset_three = Asset(2000, 'Equity', 'DM', .08, .075)
asset_four = Asset(30000, 'Equity', 'US', .06, .085)
asset_five = Asset(6000, 'Fixed', 'EM', .05, .03)
asset_six = Asset(2000, 'Equity', 'DM', .08, .075)
asset_seven = Asset(30000, 'Equity', 'US', .06, .085)

# Create Liabilities
liability_one = Liability(1500, .03, 30)
liability_two = Liability(6500, .03, 30)

# Add Assets to Portfolio
my_portfolio.add_asset(asset_one)
my_portfolio.add_asset(asset_two)
my_portfolio.add_asset(asset_three)
my_portfolio.add_asset(asset_four)
my_portfolio.add_asset(asset_five)
my_portfolio.add_asset(asset_six)
#my_portfolio.add_asset(asset_seven)

# Add Liabilities to Portfolio
my_portfolio.add_liability(liability_one)
my_portfolio.add_liability(liability_two)

# Create Asset and Liabilities Dataframes
pd_assets = my_portfolio.asset_dataframe()
pd_liability = my_portfolio.liability_dataframe()

# Collect Age Variable
#age = input("What is your age?\n")
age = 23
years_until_retirement = 23
while type(age) is str:
    try:
        age = int(age)
        years_until_retirement = 65 - age
    except:
        age = input("Please enter a number, what is your age?\n")

# Run analysis on Portfolio Assets
country_distributon = percentage_country(pd_assets)
asset_distribution = percentage_asset(pd_assets)
portfolio_risk = round(total_risk(pd_assets), 3)
potential_return = round(potential_annual_return(pd_assets), 3)
portfolio_assets = total_assets(pd_assets)
expected_returns = future_value(pd_assets, years_until_retirement)
risk = potential_risk(pd_assets)




# Create Excel Sheet

excel_loc = "C:\\Users\\Noah\\PycharmProjects\\investing\\portfolio.xlsx"

if os.path.exists(excel_loc):
    os.remove(excel_loc)

with pandas.ExcelWriter('portfolio.xlsx') as writer:
    pd_assets.to_excel(writer, sheet_name="assets")
    pd_liability.to_excel(writer, sheet_name="liabilities")
    country_distributon.to_excel(writer, sheet_name="assets", startrow=0, startcol=9)
    asset_distribution.to_excel(writer, sheet_name="assets", startrow=5, startcol=9)
    risk.to_excel(writer, sheet_name="assets", startrow=14, startcol=9)

# Format Excel Sheet
format_excel(excel_loc, portfolio_risk, potential_return, portfolio_assets, years_until_retirement, expected_returns)

# os.system("open -a 'path/Microsoft Excel.app' 'path/file.xlsx'")
