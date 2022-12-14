from mathparser import *

class Primsatic:
    def __init__(self, parser, max_history_limit=15):
        self.max_history_limit = max_history_limit
        self.history = []
        self.parser = parser
    def evaluate_expression(self, expression):
        return parser.eval(expression)



p = Primsatic(parser)
print(p.evaluate_expression("round(5.5)"))
