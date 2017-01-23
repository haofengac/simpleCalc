from plyplus import STransformer
from plyplus import Grammar
from fractions import Fraction
from decimal import Decimal

class operation():
    def __init__(self, func):
        self._func = func

class binary_op(operation):
    def __init__(self, func, part1, part2):
        self._func = func
        self._part1 = part1
        self._part2 = part2

class unary_op(operation):
    def __init__(self, func, num):
        self._func = func
        self._num = num

class atom():
    def __init__(self):
        self._trueVal = None

class number(atom):
    def __init__(num):
        self._num = num
        self._trueVal = num

class power(atom):
    def __init__(base, pow):
        self._trueVal = base ** pow

class logarithm(atom):
    def __init__(base, num):
        self._base = base
        self._num = num
        self._trueVal = log(self._num) / log(self._base)

class trig(atom):
    trig_lib = {
                'sin': sin,
                'cos': cos,
                'tan': tan,
                'cot': cot,
                'csc': csc,
                'sec': sec
                }

    def __init__(func, num):
        self._func = trig_lib[ func ]
        self._num = num
        self._trueVal = self._func( self._num )

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return Fraction(fractionalize(x), fractionalize(y))

def pow(base, expn):
    # some hard code here:
    if base == 2 or (base < 5 and expn < 5) or expn < 3:
        return base ** expn
    else:
        return Power(base, expn)

def fractionalize(x):
    if type(x) == Fraction:
        return x
    zeros = 10 ** ( -Decimal(str(x)).as_tuple().exponent )
    return Fraction(int(x * zeros), int(zeros))

operator_lib = { '+': add, 
                  '-': sub, 
                  '*': mul, 
                  '/': div }

grammar = "start: add;?add: (add add_symbol)? mul;?mul: (mul mul_symbol)? atom;@atom: neg | number | '\(' add '\)';neg: '-' atom;number: '[\d.]+';mul_symbol: '\*' | '/';add_symbol: '\+' | '-';WHITESPACE: '[ \t]+' (%ignore);"


