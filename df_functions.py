def percentage_country(portfolio):
    return portfolio.groupby("Country")["Value"].sum() / portfolio["Value"].sum()


def percentage_asset(portfolio):
    return portfolio.groupby("Type")["Value"].sum() / portfolio["Value"].sum()


def total_risk(portfolio):
    return portfolio["Risk"].sum() / len(portfolio['Risk'].index)

def potential_annual_return(portfolio):
    return (portfolio["Return"] * (portfolio["Value"]/portfolio["Value"].sum())).sum()
