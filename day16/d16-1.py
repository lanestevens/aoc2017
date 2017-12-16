# -*- coding: utf-8 -*-

import sys

num_programs = 16

programs = []
for i in range(num_programs):
    if programs:
        programs.append(chr(ord(programs[-1]) + 1))
    else:
        programs.append('a')

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

for cmd in sys.stdin.readline().strip().split(','):
    programs = moves[cmd[0]](programs, cmd)
print ''.join(programs)
