
def multiply(x, y):
    return x * y


def divide(x, y):
    return round(x / y, 1)


def round_up(x):
    result = int(x) + int((x > 0) and (x - int(x)) > 0)
    return result
