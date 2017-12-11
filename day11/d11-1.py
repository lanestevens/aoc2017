# -*- coding: utf-8 -*-

import sys

moves = [x for x in sys.stdin.readline().strip().split(',')]

move_counts = {'nw': 0,
               'n': 0,
               'ne': 0,
               'sw': 0,
               's': 0,
               'se': 0,
               }

for move in moves:
    move_counts[move] += 1

if move_counts['s'] > move_counts['n']:
    move_counts['s'] = move_counts['s'] - move_counts['n']
    move_counts['n'] = 0
else:
    move_counts['n'] = move_counts['n'] - move_counts['s']
    move_counts['s'] = 0
    
if move_counts['se'] > move_counts['nw']:
    move_counts['se'] = move_counts['se'] - move_counts['nw']
    move_counts['nw'] = 0
else:
    move_counts['nw'] = move_counts['nw'] - move_counts['se']
    move_counts['se'] = 0

if move_counts['sw'] > move_counts['ne']:
    move_counts['sw'] = move_counts['sw'] - move_counts['ne']
    move_counts['ne'] = 0
else:
    move_counts['ne'] = move_counts['ne'] - move_counts['sw']
    move_counts['sw'] = 0

if move_counts['sw'] > move_counts['se']:
    move_counts['s'] = move_counts['s'] + move_counts['se']
    move_counts['sw'] = move_counts['sw'] - move_counts['se']
    move_counts['se'] = 0
else:
    move_counts['s'] = move_counts['s'] + move_counts['sw']
    move_counts['se'] = move_counts['se'] - move_counts['sw']
    move_counts['sw'] = 0

print move_counts['s'] + move_counts['se']



