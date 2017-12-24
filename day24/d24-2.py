# -*- coding: utf-8 -*-

import sys

def bridge(pipes, this_bridge, candidates, used):
    if not candidates:
        return this_bridge
    if candidates[0]['id'] in used:
        return bridge(pipes, this_bridge, candidates[1:], used)
    return [bridge(pipes, this_bridge + [candidates[0]], pipes[candidates[0]['that']], used + [candidates[0]['id']])]\
        + [bridge(pipes, this_bridge, candidates[1:], used)]
    
def flatten(l):
    if not l:
        return []
    if not l[0]:
        return []

    if isinstance(l[0][0], dict):
        return [l[0]] + flatten(l[1:])
    return flatten(l[0]) + flatten(l[1:])

pipes = {}
for i, line in enumerate(sys.stdin.readlines()):
    ends = [int(x) for x in line.strip().split('/')]
    for item in [{'id': i, 'this': ends[0], 'that': ends[1]}, {'id': i, 'this': ends[1], 'that': ends[0]}]:
        if item['this'] in pipes:
            pipes[item['this']].append(item)
        else:
            pipes[item['this']] = [item]

def bridge_strength(l):
    return sum([x['this'] + x['that'] for x in l])

bridges = sorted([(len(x), x) for x in flatten(bridge(pipes, [], pipes[0], []))])
longest_bridges = [x[1] for x in bridges if x[0] == bridges[-1][0]]
print max([sum([y['this'] + y['that'] for y in x]) for x in longest_bridges])

