# -*- coding: utf-8 -*-

import sys

firewall = {}
for line in sys.stdin.readlines():
    the_key = int(line[:line.index(':')])
    the_range = int(line.strip()[line.index(' ') + 1:])
    the_period = the_range + the_range - 2
    the_offset = (the_period - the_key) % the_period
    firewall[the_key] = {'range': the_range,
                         'scanner': the_offset,
                         'increment': 1,
                         'f': lambda x: x['scanner'] + x['period'],
                         'period': the_period,
                         'offset': the_offset,
                         'depth': the_key,
                         }

delay = 0
while True:
    caught = False
    for value in firewall.values():
        if value['scanner'] < delay:
            while value['scanner'] < delay:
                value['scanner'] = value['f'](value)
                if value['scanner'] == delay:
                    caught = True
                    break
        if value['scanner'] == delay:
            caught = True
            break
    if not caught:
        break
    delay += 1
print delay
