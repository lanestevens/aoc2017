# -*- coding: utf-8 -*-

import sys

instructions = []
for line in sys.stdin.readlines():
    instructions.append(int(line.strip()))

ip = 0
clock = 0
limit = len(instructions)
while True:
    target = ip + instructions[ip]
    if instructions[ip] >= 3:
        instructions[ip] -= 1
    else:
        instructions[ip] += 1
    ip = target
    clock += 1
    if ip >= limit:
        break

print clock

    
