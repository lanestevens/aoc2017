# -*- coding: utf-8 -*-

import binascii
import sys

total = 0
for line in sys.stdin.readlines():
    this = ''
    for c in line.strip():
        this += '{:04b}'.format(int(c, 16))
    total += sum([int(x) for x in this])
print total

    
    
