def percentage_country(portfolio):
    return portfolio.groupby("Country")["Value"].sum() / portfolio["Value"].sum()


def percentage_asset(portfolio):
    return portfolio.groupby("Type")["Value"].sum() / portfolio["Value"].sum()