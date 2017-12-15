# -*- coding: utf-8 -*-

import sys

a = 618
b = 814

fa = lambda x: (16807 * x) % 2147483647
fb = lambda x: (48271 * x) % 2147483647

i = 0
matches = 0
while i < 40000000:
    a = fa(a)
    b = fb(b)
    if (a & 0xffff) == (b & 0xffff):
        matches += 1
    i += 1
print matches
