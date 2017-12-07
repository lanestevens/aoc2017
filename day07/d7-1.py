# -*- coding: utf-8 -*-

import sys

all_held_items = set([])
all_holders = set([])
for line in sys.stdin.readlines():
    name = line.split()[0].strip()
    split_items = line.strip().split('>')
    if len(split_items) > 1:
        held_items = [x.strip() for x in split_items[1].split(',')]
        for held_item in held_items:
            all_held_items.add(held_item)
        all_holders.add(name)
print all_holders.difference(all_held_items)

        
    
