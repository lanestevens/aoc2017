# -*- coding: utf-8 -*-

import itertools
import sys

def get_row_cksum(l):
    candidates = [x for x in itertools.product(l, l) if x[0] > x[1]]
    for candidate in candidates:
        if candidate[0] % candidate[1] == 0:
            return candidate[0] / candidate[1]
    
cksum = 0
for line in sys.stdin.readlines():
    vals = [int(x) for x in line.split('\t')]
    cksum += get_row_cksum(vals)
print cksum
