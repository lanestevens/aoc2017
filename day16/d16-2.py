# -*- coding: utf-8 -*-

import sys

num_programs = 16

programs = []
for i in range(num_programs):
    if programs:
        programs.append(chr(ord(programs[-1]) + 1))
    else:
        programs.append('a')
starting_programs = ''.join(programs)

def s(l, cmd):
    i = int(cmd[1:])
    return l[-i:] + l[0:-i]

def x(l, cmd):
    a, b = [int(v) for v in cmd[1:].split('/')]
    t = l[a]
    l[a] = l[b]
    l[b] = t
    return l

def p(l, cmd):
    ca, cb = [v for v in cmd[1:].split('/')]
    a = l.index(ca)
    b = l.index(cb)
    t = l[a]
    l[a] = l[b]
    l[b] = t
    return l

moves = {'s': s,
         'x': x,
         'p': p,
         }

commands = sys.stdin.readline().strip().split(',')

# i = 0
# while i < 100:
#     for cmd in commands:
#         programs = moves[cmd[0]](programs, cmd)
#     i += 1
# print ''.join(programs)
# sys.exit()

results = []
while True:
    for cmd in commands:
        programs = moves[cmd[0]](programs, cmd)
    this_result = ''.join(programs)
    results.append(this_result)
    if this_result == starting_programs:
        print results[1000000000 % len(results) -1]
        break
