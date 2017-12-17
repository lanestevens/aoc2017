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

monitored_value = None
for i in range(50000000):
    current_position = (current_position + steps) % (i + 1) + 1
    if current_position == 1:
        monitored_value = i + 1

print monitored_value

