"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math


def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise

def hypotenuse(a,b):
    return math.hypot(a,b)


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a


def exp(a, b):
    return a ** b



def subtract(a,b):
    return a-b


def logarithm(a,b):

    if b<=0 or a<=0 or a==1:
        raise ValueError
    if b==math.e:
        return math.log(a)
    return math.log(a,b)



