# -*- coding: utf-8 -*-

import sys

pipes = {}
for line in sys.stdin.readlines():
    key = int(line[0:line.index(' ')])
    val = {int(x.strip()) for x in line.strip()[line.index('>') + 1:].split(',')}
    val.add(key)
    pipes[key] = val

groups = []
for program_start in pipes.keys():
    programs = pipes[program_start]
    processed = set([])
    changed = True
    while changed:
        changed = False
        new_items = set([])
        for program in programs:
            if program in processed:
                continue
            processed.add(program)
            new_items = new_items.union(pipes[program])
        if new_items:
            programs = programs.union(new_items)
            changed = True
            
    found = False
    for group in groups:
        if group == programs:
            found = True
            break
    if not found:
        groups.append(programs)

print len(groups)
