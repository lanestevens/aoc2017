# -*- coding: utf-8 -*-

import sys

operators = {'<': lambda a,b: a < b,
             '<=': lambda a,b: a <= b,
             '>': lambda a,b: a > b,
             '>=': lambda a,b: a >= b,
             '!=': lambda a,b: a != b,
             '==': lambda a,b: a == b,
             'inc': lambda a,b: a + b,
             'dec': lambda a,b: a - b,
             }

registers = {}
the_max = 0
for line in sys.stdin.readlines():
    target, incdec, val, noise, a, comp, b = line.strip().split()
    if operators[comp](registers.get(a, 0), int(b)):
        registers[target] = operators[incdec](registers.get(target, 0), int(val))
        the_max = max(the_max, registers[target])
        

print the_max
    
