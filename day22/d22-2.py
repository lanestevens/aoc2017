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
    elif map.get(position, '.') == '.':
        if direction == (1, 0):
            return (0, -1)
        elif direction == (0, -1):
            return (-1, 0)
        elif direction == (-1, 0):
            return (0, 1)
        else:
            return (1, 0)
    elif map.get(position, '.') == 'F':
        return (-direction[0] if direction[0] else 0, -direction[1] if direction[1] else 0)
    else:
        return direction

def print_diagnostics(position, direction, map, infections):
    print position
    print direction
    print_map(map)
    print infections
    
def activity_burst(position, direction, map, infections):
    next_state = {'.': 'W',
                  '#': 'F',
                  'W': '#',
                  'F': '.',
                  }
    direction = next_direction(position, direction, map)
    infections += 1 if map.get(position, '.') == 'W' else 0
    map[position] = next_state[map.get(position, '.')]
    position = (position[0] + direction[0], position[1] + direction[1])
    return position, direction, map, infections

map = get_map()
position = (0, 0)
direction = (1, 0)
infections = 0
for i in range(int(sys.argv[1])):
    position, direction, map, infections = activity_burst(position, direction, map, infections)

#print_diagnostics(position, direction, map, infections)
print infections

