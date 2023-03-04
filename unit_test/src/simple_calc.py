def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError
    return numerator / denominator