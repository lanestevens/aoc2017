# -*- coding: utf-8 -*-

import sys

def sanitize(s):
    result = []
    in_garbage = False
    quote = False
    for c in list(s):
        if quote:
            quote = False
            continue
        if in_garbage:
            if c == '!':
                quote = True
            elif c == '>':
                in_garbage = False
            continue
        if c == '!':
            quote = True
            continue
        if c == '<':
            in_garbage = True
            continue
        
        if c in ('{', '}'):
            result.append(c)

    return result

total = 0
score = 0
for c in sanitize(sys.stdin.read()):
    if c == '{':
        score += 1
    else:
        total += score
        score -= 1
print total
