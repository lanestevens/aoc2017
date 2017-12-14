# -*- coding: utf-8 -*-

import binascii
import sys

rows = []
for line in sys.stdin.readlines():
    this = ''
    for c in line.strip():
        this += '{:04b}'.format(int(c, 16))
    rows.append([int(x) for x in this])

used_coordinates = set([])
for i in range(128):
    for j in range(128):
        if rows[i][j]:
            used_coordinates.add((i,j))

groups = []
for used_coordinate in used_coordinates:
    neighbors = [(used_coordinate[0] + 1, used_coordinate[1]),
                 (used_coordinate[0] - 1, used_coordinate[1]),
                 (used_coordinate[0], used_coordinate[1] + 1),
                 (used_coordinate[0], used_coordinate[1] - 1),
                 used_coordinate,
                 ]
    groups.append({x for x in neighbors if x in used_coordinates})

singles = [x for x in groups if len(x) == 1]
multis = [x for x in groups if len(x) > 1]

while True:
    changed = False
    source_groups = multis
    multis = []
    used_groups = set([])
    for i in range(len(source_groups)):
        if i in used_groups:
            continue
        this_group = source_groups[i]
        for j in range(i + 1, len(source_groups)):
            if this_group.intersection(source_groups[j]):
                this_group = this_group.union(source_groups[j])
                used_groups.add(j)
                changed = True
        multis.append(this_group)
    if not changed:
        break
print len(multis) + len(singles)
