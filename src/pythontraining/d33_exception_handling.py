"""
Demo exception handling
"""


try:
    number = int(input("Give me a number: "))
    print(100 / number)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("give me a digit please")
except Exception as exc:
    print("Unexpected error, sending to the logger", type(exc), exc)
