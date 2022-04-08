"""
Refactoring in PyCharm
"""
from enum import Enum


def calculate_price(volume, item_price):
    discount = determine_discount(volume)

    total_price = volume * item_price
    total_discount = total_price * discount

    return total_price - total_discount


def determine_discount(volume):
    if volume >= 500:
        discount = 0.15
    elif volume >= 200:
        discount = 0.10
    elif volume >= 100:
        discount = 0.05
    else:
        discount = 0
    return discount


print(calculate_price(volume=200, item_price=10))


# The Arrow
bank_is_closed = True
account_balance = 200


def process_transaction(currency, amount):
    if bank_is_closed:              # Guard clause (return early)
        return "Bank is closed"
    if currency != "EUR":           # Guard clause
        return "only EUR transactions allowed"
    if amount > account_balance:    # Guard clause
        return "Balance too low"

    monitor_large_transaction(amount)   # extracted method
    return "transaction success"


def monitor_large_transaction(amount):
    if amount >= 100:
        print("attention, large transaction", amount)


print(process_transaction("EUR", 150))
