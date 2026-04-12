#https://github.com/evelyn-c68/lab11--EC---KB-.git
# Partner 1: Evelyn Chen
# Partner 2: Kaylee Bleeker

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid input for a logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def hypotenuse(a, b):
    return math.hypot(a, b)

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)



