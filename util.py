from plyplus import STransformer
from plyplus import Grammar
from fractions import Fraction
from decimal import Decimal

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


