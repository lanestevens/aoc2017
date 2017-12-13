# -*- coding: utf-8 -*-

import sys

firewall = {}
for line in sys.stdin.readlines():
    the_key = int(line[:line.index(':')])
    the_range = int(line.strip()[line.index(' ') + 1:])
    firewall[the_key] = {'range': the_range, 'scanner': 0, 'increment': 1}
    
limit = max(firewall.keys())
for i in range(limit):
    if i in firewall:
        continue
    firewall[i] = None

position = -1
severity = 0
while position < limit:
    position += 1
    if firewall[position] and firewall[position]['scanner'] == 0:
        severity += position * firewall[position]['range']
    for value in firewall.values():
        if value:
            next_value = value['scanner'] + value['increment']
            if next_value == value['range']:
                value['increment'] = -1
                next_value = value['scanner'] + value['increment']
            elif next_value == -1:
                value['increment'] = 1
                next_value = value['scanner'] + value['increment']
            value['scanner'] = next_value

print severity

    
