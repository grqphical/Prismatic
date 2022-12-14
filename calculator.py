from mathparser import simpleeval
from math import *
from decimal import Decimal

# Function for converting radians to degrees
def rad2deg(radians):
    return Decimal(radians * 180/pi)

# Function to round numbers to the nearest one
def round_half_up(n):
    multiplier = 10 ** 0
    return floor(n*multiplier + 0.5) / multiplier

class Calculator:
    def __init__(self, max_memory=100):
        self.history = []
        self.parser = simpleeval.SimpleEval()
        self.ansCount = -1
        self.memory = [nan] * max_memory
        # Custom functions
        self.parser.functions = {
            "sin" : sin,
            "cos" : cos,
            "rad2deg" : rad2deg,
            "round" : round_half_up,
            "clear" : self.clear_history,
            "prevans" : self.get_historical_value,
            "getmem" : self.get_memory,
            "store" : self.store_memory,
            "clearmem" : self.clear_memory
        }

        # Custom constants
        self.parser.names = {
            "PI" : pi,
            "E" : e,
            "TAU" : tau,
            "INF" : inf
        }
        
    def evaluate_expression(self, expression):
        self.ansCount += 1
        error = False
        try:
            ans = self.parser.eval(expression)
        except Exception as e:
            error = True
            ans = e
        self.history.append((expression, ans, self.ansCount, error))

        return ans
    
    def clear_history(self):
        self.history = []
    
    def get_historical_value(self, index):
        return self.history[index-1][1]
    
    def get_memory(self, index):
        return self.memory[index-1]
    
    def store_memory(self, index, value):
        self.memory.insert(index-1, value)
    
    def clear_memory(self, index):
        self.memory.insert(index-1, nan)
