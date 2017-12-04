# -*- coding: utf-8 -*-

import sys

good_passphrases = 0
for line in sys.stdin.readlines():
    line = line.strip().split()
    if len(line) == len(set(line)):
        good_passphrases += 1
print good_passphrases
