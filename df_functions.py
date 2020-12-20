# Country weighting
def percentage_country(portfolio):
    return portfolio.groupby("Country")["Value"].sum() / portfolio["Value"].sum()


# Asset weighting
def percentage_asset(portfolio):
    return portfolio.groupby("Type")["Value"].sum() / portfolio["Value"].sum()


# Potential risk weighted by market value
def total_risk(portfolio):
    return (portfolio["Risk"] * (portfolio["Value"] / portfolio["Value"].sum())).sum()


# Potential return weighted by market value
def potential_annual_return(portfolio):
    return (portfolio["Return"] * (portfolio["Value"] / portfolio["Value"].sum())).sum()

# Return total value of current assets
def total_assets(portfolio):
    return portfolio["Value"].sum()

def future_value(portfolio, years):
    return total_assets(portfolio)(1 + potential_annual_return(portfolio)^years)
