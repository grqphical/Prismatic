from . import simpleeval
from math import *
from decimal import Decimal

parser = simpleeval.SimpleEval()

# Function for converting radians to degrees
def rad2deg(radians):
    return Decimal(radians * 180/pi)

# Function to round numbers to the nearest one
def round_half_up(n):
    multiplier = 10 ** 0
    return floor(n*multiplier + 0.5) / multiplier



# Custom functions
parser.functions = {
    "sin" : sin,
    "cos" : cos,
    "rad2deg" : rad2deg,
    "round" : round_half_up
}

# Custom constants
parser.names = {
    "PI" : pi,
    "E" : e,
    "TAU" : tau,
    "INF" : inf
}
