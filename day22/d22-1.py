# -*- coding: utf-8 -*-

import sys

def get_map():
    map = {}
    for line in sys.stdin.readlines():
        if not map:
            size = (len(line.strip()) / 2)
            x = size
        else:
            x -= 1
        for y, c in enumerate(line.strip()):
            map[(x,y - size)] = c
    return map

def print_map(map):
    the_max = 0
    for key in map.keys():
        the_max = max(the_max, *[abs(x) for x in key])
    for i in range(the_max, -the_max - 1, -1):
        row = ''
        for j in range(-the_max, the_max + 1):
            row += map.get((i, j), '.')
        print row

def next_direction(position, direction, map):
    if map.get(position, '.') == '#':
        if direction == (1, 0):
            return (0, 1)
        elif direction == (0, 1):
            return (-1, 0)
        elif direction == (-1, 0):
            return (0, -1)
        else: #direction == (0, -1)
            return (1, 0)
    else:
        if direction == (1, 0):
            return (0, -1)
        elif direction == (0, -1):
            return (-1, 0)
        elif direction == (-1, 0):
            return (0, 1)
        else:
            return (1, 0)

def print_diagnostics(position, direction, map, infections):
    print position
    print direction
    print_map(map)
    print infections
    
def activity_burst(position, direction, map, infections):
    direction = next_direction(position, direction, map)
    infections += 0 if map.get(position, '.') == '#' else 1
    map[position] = ('.' if map.get(position, '.') == '#' else '#')
    position = (position[0] + direction[0], position[1] + direction[1])
    return position, direction, map, infections



map = get_map()
position = (0, 0)
direction = (1, 0)
infections = 0
for i in range(int(sys.argv[1])):
    position, direction, map, infections = activity_burst(position, direction, map, infections)

print infections
