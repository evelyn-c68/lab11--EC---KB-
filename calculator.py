"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
<<<<<<< HEAD
import math

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm arguments must be positive")
    return log(a, b)

def exponent(a, b):
    return a**b



=======
# First example
#https://github.com/evelyn-c68/lab11--EC---KB-.git
# Partner 1: Evelyn Chen
# Partner 2: Kaylee Bleeker
import math
>>>>>>> 6cff8c039725e4b5b112352e5343d55ef9fc2359

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a ==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b/a

def log(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid input for a logarithm")
    return math.log(b, a)

def exp(a, b):
    return a **b

