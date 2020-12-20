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
asset_one = Asset(7000, 'Equity', 'US', .1, .1)
asset_two = Asset(1000, 'Fixed', 'EM', .3, .2)
asset_three = Asset(2000, 'Equity', 'DM', .08, .075)
asset_four = Asset(3000, 'Equity', 'US', .06, .085)

# Create Liabilities
liability_one = Liability(1500, .03, 30)
liability_two = Liability(6500, .03, 30)

# Add Assets to Portfolio
my_portfolio.add_asset(asset_one)
my_portfolio.add_asset(asset_two)
my_portfolio.add_asset(asset_three)
my_portfolio.add_asset(asset_four)

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
portfolio_assets = total_assets(pd_assets)

# Create Excel Sheet
excel_loc = "C:\\Users\\Noah\\PycharmProjects\\investing\\portfolio.xlsx"

if os.path.exists(excel_loc):
    os.remove(excel_loc)

with pandas.ExcelWriter('portfolio.xlsx') as writer:
    pd_assets.to_excel(writer, sheet_name="assets")
    pd_liability.to_excel(writer, sheet_name="liabilities")
    country_distributon.to_excel(writer, sheet_name="assets", startrow=0, startcol=9)
    asset_distribution.to_excel(writer, sheet_name="assets", startrow=5, startcol=9)

# Plug analysis into excel sheet
my_workbook = openpyxl.load_workbook(excel_loc)
my_worksheet = my_workbook["assets"]

my_worksheet["N1"] = "Portfolio Risk"
my_worksheet["M1"] = "Potential Return"
my_worksheet["N2"].value = round(portfolio_risk, 2)
my_worksheet["N2"].number_format = '0.00%'

my_worksheet["K2"].number_format = '0.00%'
my_worksheet["K3"].number_format = '0.00%'
my_worksheet["K4"].number_format = '0.00%'

my_worksheet["K7"].number_format = '0.00%'
my_worksheet["K8"].number_format = '0.00%'

my_worksheet["M2"].value = round(potential_return, 2)
my_worksheet["M2"].number_format = '0.00%'

my_worksheet["M6"] = "Total Value"
my_worksheet["M7"].value = round(portfolio_assets, 2)
my_worksheet["M7"].number_format = "$ 0.00"

my_workbook.save(excel_loc)
#os.system("open -a 'path/Microsoft Excel.app' 'path/file.xlsx'")

