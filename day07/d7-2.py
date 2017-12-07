# -*- coding: utf-8 -*-

import sys

def program_weight(name, programs):
    held_weight = 0
    for held_item in programs[name]['held_items']:
        held_weight += program_weight(held_item, programs)
    return programs[name]['weight'] + held_weight

programs = {}
all_held_items = set([])
all_holders = set([])
for line in sys.stdin.readlines():
    name = line.split()[0].strip()
    split_items = line.strip().split('>')
    if len(split_items) > 1:
        held_items = [x.strip() for x in split_items[1].split(',')]
    else:
        held_items = []
    programs[name] = {'weight': int(line[line.index('(') + 1:line.index(')')]),
                      'held_items': held_items}
for name in programs.keys():
    if programs[name]['held_items']:
        these_weights = sorted([(program_weight(x, programs), x) for x in programs[name]['held_items']])
        if these_weights[0][0] == these_weights[-1][0]:
            continue


        difference = these_weights[-1][0] - these_weights[0][0]
        item = these_weights[-1][1]

while True:
    if programs[item]['held_items']:
        these_weights = sorted([(program_weight(x, programs), x) for x in programs[item]['held_items']])
        if these_weights[0][0] == these_weights[-1][0]:
            print programs[item]['weight'] - difference
            break

        item = these_weights[-1][1]
        continue
    else:
        print programs[item]['weight'] - difference
        break

        


    
