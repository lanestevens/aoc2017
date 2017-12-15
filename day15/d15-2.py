# -*- coding: utf-8 -*-

import sys

#a = 65
#b = 8921
a = 618
b = 814

fa = lambda x: (16807 * x) % 2147483647
fb = lambda x: (48271 * x) % 2147483647

i = 0
matches = 0
while i < 5000000:
    a = fa(a)
    while a % 4:
        a = fa(a)

    b = fb(b)
    while b % 8:
        b = fb(b)

    if (a & 0xffff) == (b & 0xffff):
        matches += 1
    i += 1
print matches
