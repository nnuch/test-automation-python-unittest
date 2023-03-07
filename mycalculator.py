#4 Functions incoulding add, substract, multiply, and divide (with a condition)
def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("cannot divide a number by zero")
    return x/y