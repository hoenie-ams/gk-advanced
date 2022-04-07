"""
Demo of pylint. Install via "pip install pylint"

Run from the terminal: pylint <folder>/<filename>
"""


def convert_eur_to_usd(amount):
    result = amount * 1.20
    return result


if __name__ == "__main":
    print(convert_eur_to_usd(500))
