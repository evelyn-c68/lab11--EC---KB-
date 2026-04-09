"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
#https://github.com/evelyn-c68/lab11--EC---KB-.git
# Partner 1: Evelyn Chen
# Partner 2: Kaylee Bleeker
import math

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

