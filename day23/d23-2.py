# -*- coding: utf-8 -*-

import sys

b = 57
c = b
b = b * 100
b += 100000
c = b
c += 17000
h = 0
while True:
    f = 1
    d = 2
    while d * 2 <= b and f:
        e = 2
        while e * d <= b and f:
            if e * d == b:
                f = 0
            e += 1
        d += 1
    if f == 0:
        h += 1
    if c == b:
        break
    b += 17
print h
