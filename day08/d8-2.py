# -*- coding: utf-8 -*-

import sys

def lt(a, b):
    return a < b

def lte(a, b):
    return a <= b

def gt(a, b):
    return a > b

def gte(a, b):
    return a >= b

def ne(a, b):
    return a != b

def eq(a, b):
    return a == b

def inc(a, b):
    return a + b

def dec(a, b):
    return a - b

operators = {'<': lt,
             '<=': lte,
             '>': gt,
             '>=': gte,
             '!=': ne,
             '==': eq,
             'inc': inc,
             'dec': dec,
             }

registers = {}
the_max = 0
for line in sys.stdin.readlines():
    target, incdec, val, noise, a, comp, b = line.strip().split()
    if operators[comp](registers.get(a, 0), int(b)):
        registers[target] = operators[incdec](registers.get(target, 0), int(val))
        the_max = max(the_max, registers[target])
        

print the_max
    
