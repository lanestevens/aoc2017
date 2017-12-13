# -*- coding: utf-8 -*-

import sys

def firewall_reset(firewall):
    for value in firewall.values():
        if value:
            value['scanner'] = 0
            value['increment'] = 1

def firewall_advance_scanners(firewall):
    for value in firewall.values():
        if value:
            next_scanner_value = value['scanner'] + value['increment']
            if next_scanner_value == value['range']:
                value['increment'] = -1
                next_scanner_value = value['scanner'] + value['increment']
            elif next_scanner_value == -1:
                value['increment'] = 1
                next_scanner_value = value['scanner'] + value['increment']
            value['scanner'] = next_scanner_value
            
def packet_delay(firewall, delay):
    while delay > 0:
        firewall_advance_scanners(firewall)
        delay -= 1

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
