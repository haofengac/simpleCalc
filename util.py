import re, collections, decimal
from fractions import Fraction

Token = collections.namedtuple('Token', ['name', 'value'])
RuleMatch = collections.namedtuple('RuleMatch', ['name', 'matched'])
token_map = {'+':'ADD', '-':'ADD', '*':'MUL', '/':'MUL', '(':'LPAR', ')':'RPAR'}
rule_map = {
    'add' : ['mul ADD add', 'mul'],
    'mul' : ['atom MUL mul', 'atom'],
    'atom': ['NUM', 'LPAR add RPAR', 'neg'],
    'neg' : ['ADD atom'],
}
fix_assoc_rules = 'add', 'mul'

class Power():
    def __init__(self, base, expn):
        self._base = base
        self._expn = expn
        self._trueVal = base ** expn

    def __str__(self):
        return "(%f ^ %f)" % (base, expn)

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
    zeros = 10 ** ( -decimal.Decimal(str(x)).as_tuple().exponent )
    return Fraction(int(x * zeros), int(zeros))

bin_calc_map = {'*':mul, '/':div, '+':add, '-':sub}

def calc_binary(x):
    while len(x) > 1:
        x[:3] = [ bin_calc_map[x[1]](x[0], x[2]) ]
    return x[0]

calc_map = {
    'NUM' : float,
    'atom': lambda x: x[len(x)!=1],
    'neg' : lambda (op,num): (num,-num)[op=='-'],
    'mul' : calc_binary,
    'add' : calc_binary,
}
