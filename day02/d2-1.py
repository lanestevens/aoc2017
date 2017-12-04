# -*- coding: utf-8 -*-

import sys

cksum = 0
for line in sys.stdin.readlines():
    vals = [int(x) for x in line.split('\t')]
    cksum += (max(vals) - min(vals))
print cksum
