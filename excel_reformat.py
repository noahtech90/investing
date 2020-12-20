import pandas
import os
import openpyxl


def format_excel(excel_loc, portfolio_risk, potential_return, portfolio_assets):
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
