# -*- coding: utf-8 -*-

import sys

steps = int(sys.stdin.readline().strip())

memory = [0]
current_position = 0

def advance(l, steps, current_position, insert_value):
    if len(l) == 1:
        l.append(insert_value)
        return 1

    current_position = (current_position + steps) % len(l)
    l.insert(current_position + 1, insert_value)
    return current_position + 1

for i in range(2017):
    current_position = advance(memory, steps, current_position, i + 1)

print memory[current_position + 1]
