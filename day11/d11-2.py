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

def distance(d):
    opposites = (('n', 's'),
                 ('ne', 'sw'),
                 ('nw', 'se'),
                 )
    for k1, k2 in opposites:
        if d[k1] > d[k2]:
            d[k1] = d[k1] - d[k2]
            d[k2] = 0
        else:
            d[k2] = d[k2] - d[k1]
            d[k1] = 0

    compliments = (('nw', 'ne', 'n'),
                   ('sw', 'se', 's'),
                   )
    for k1, k2, k3 in compliments:
        if d[k1] and d[k2]:
            if d[k1] > d[k2]:
                d[k3] = d[k3] + d[k2]
                d[k1] = d[k1] - d[k2]
                d[k2] = 0
            else:
                d[k3] = d[k3] + d[k1]
                d[k2] = d[k2] - d[k1]
                d[k1] = 0
    offsets = (('ne', 's'),
               ('nw', 's'),
               ('se', 'n'),
               ('sw', 'n'),
               )
    for k1, k2 in offsets:
        if d[k1] and d[k2]:
            if d[k1] > d[k2]:
                d[k2] = 0
            else:
                d[k1] = 0

    return sum([x for x in d.values()])

max_distance = 0
for move in moves:
    move_counts[move] += 1
    max_distance = max(max_distance, distance(move_counts.copy()))

print distance(move_counts.copy())
print max_distance
print move_counts
