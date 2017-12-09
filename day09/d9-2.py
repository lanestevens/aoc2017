# -*- coding: utf-8 -*-

import sys

def sanitize(s):
    garbage_count = 0
    in_garbage = False
    quote = False
    for c in list(s):
        if quote:
            quote = False
            continue
        if in_garbage:
            if c == '!':
                quote = True
                continue
            elif c == '>':
                in_garbage = False
                continue
            else:
                garbage_count += 1
                continue
        if c == '!':
            quote = True
            continue
        if c == '<':
            in_garbage = True
            continue
        
    return garbage_count

print sanitize(sys.stdin.read())
