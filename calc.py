# Author: Haofeng Chen
from util import *

class Calculator(STransformer):
    def __init__(self):
        self._expr = ""
        self._lCurs = 0
        self._rCurs = 0
 
    def _bin_operator(self, exp):
        arg1, operator_symbol, arg2 = exp.tail
        operator_func = operator_lib[operator_symbol]
 
        return operator_func(arg1, arg2)
 
    number      = lambda self, exp: float(exp.tail[0])
    neg         = lambda self, exp: -exp.tail[0]
    __default__ = lambda self, exp: exp.tail[0]
 
    add = _bin_operator
    mul = _bin_operator

if __name__ == '__main__':
    c = Calculator()
    g = Grammar(grammar)
    while True:
        try:
            s = raw_input('> ')
        except EOFError:
            break
        if s == '':
            break
        tree = g.parse(s)
        print tree
        print c.transform(tree)