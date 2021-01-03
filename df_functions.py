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


# Future value of current investments
def future_value(portfolio, years):
    return portfolio["Value"].sum() * (
                1 + (portfolio["Return"] * portfolio["Value"] / portfolio["Value"].sum()).sum()) ** years

def potential_risk(portfolio):
    country_allocation = percentage_country(portfolio)
    asset_allocation = percentage_asset(portfolio)
    risks = []
    i = 0
    j = 0

    for country_percentage in country_allocation:
        if country_percentage > .7:
            risks.append([country_allocation.index[i], country_percentage])
        i += 1

    for asset_percentage in asset_allocation:
        if asset_percentage > .7:
            risks.append([asset_allocation.index[j], asset_percentage])
        j += 1

    print(risks)
    return risks


