import numpy as np
import pandas as pd

class Asset:

    def __init__(self, value, asset_class, country, potential_annual_return, risk):
        self.value = value
        self.asset_class = asset_class
        self.country = country
        self.potential_annual_return = potential_annual_return
        self.risk = risk

    def return_value(self):
        return self.value


class Liability:

    def __init__(self, value, interest_rate, contract_length):
        self.value = value
        self.interest_rate = interest_rate
        self.contract_length = contract_length

    def return_value(self):
        return self.value