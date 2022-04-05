"""
Demo and explanation of best practices.
"""
# Constant
EUR_USD_EXCHANGE_RATE = 1.14

# Bad examples
var = ...
data = ...
temp = ...
df = ...
list = ...
l = ...
distance = ...
fname = ...

# Good examples
number_of_children = 3
age = 42
postal_code = 2000

# Concatenation
streetname = "Main Street"
# camelCase
streetName = ...
# PascalCase
StreetName = ...
# kebab-case
# street-name = ...
# snake_case
street_name = ...


def convert(amount):
    return amount * 1.14


def convertEur2Usd(amount):
    return amount * 1.14


def convert_eur_to_usd(amount):
    return amount * EUR_USD_EXCHANGE_RATE


# Classes
class RectangleShape:    # PascalCase

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):   # snake_case
        return self.width * self.length
