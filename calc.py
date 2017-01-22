'''A Calculator Implemented With A Top-Down, Recursive-Descent Parser'''
# Author: Haofeng Chen
from util import *

class Calculator():
    def __init__(self):
        self._expr = ""
        self._lCurs = 0
        self._rCurs = 0

    def match(self, rule_name, tokens):
        if tokens and rule_name == tokens[0].name:      # Match a token?
            return tokens[0], tokens[1:]
        for expansion in rule_map.get(rule_name, ()):   # Match a rule?
            remaining_tokens = tokens
            matched_subrules = []
            for subrule in expansion.split():
                matched, remaining_tokens = self.match(subrule, remaining_tokens)
                if not matched:
                    break   # no such luck. next expansion!
                matched_subrules.append(matched)
            else:
                return RuleMatch(rule_name, matched_subrules), remaining_tokens
        return None, None   # match not found

    def step(self, expr):
        print "= " + expr

    def _recurse_tree(self, tree, func):
        temp = map(func, (tree.matched)) if tree.name in rule_map else tree[1]
        return temp


    def flatten_right_associativity(self, tree):
        new = self._recurse_tree(tree, self.flatten_right_associativity)
        if tree.name in fix_assoc_rules and len(new)==3 and new[2].name==tree.name:
            new[-1:] = new[-1].matched
        return RuleMatch(tree.name, new)

    def evaluate(self, tree):
        solutions = self._recurse_tree(tree, self.evaluate)
        solution = calc_map.get(tree.name, lambda x:x)(solutions)
        # if tree.name != "atom":
            # step here!

        return solution

    def calc(self, expr):
        self._expr = expr
        split_expr = re.findall('[\d.]+|[%s]' % ''.join(token_map), expr)
        tokens = [Token(token_map.get(x, 'NUM'), x) for x in split_expr]
        tree = self.match('add', tokens)[0]
        tree = self.flatten_right_associativity( tree )
        return self.evaluate(tree)

if __name__ == '__main__':
    c = Calculator()
    while True:
        print( c.calc(raw_input('> ')) )