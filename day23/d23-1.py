# -*- coding: utf-8 -*-

import sys

def decode(r, x):
    try:
        return int(x)
    except:
        return r.get(x, 0)

def iset(r, x, xv, yv):
    r[x] = yv

def isub(r, x, xv, yv):
    r[x] = xv - yv

def imul(r, x, xv, yv):
    r[x] = xv * yv
    r['mulct'] += 1

def ijnz(r, x, xv, yv):
    if xv:
        r['ip'] += yv
    else:
        r['ip'] += 1
        
def iexec(r, i, x, y):
    controller = {'set': iset,
                  'sub': isub,
                  'mul': imul,
                  'jnz': ijnz,
                  }
    xv = decode(r, x)
    yv = decode(r, y)
    controller[i](r, x, xv, yv)
    r['ict'] += 1
    if i != 'jnz':
        r['ip'] += 1
    
instructions = [x.strip().split() for x in sys.stdin.readlines()]
last_instruction = len(instructions) - 1
registers = {'ip': 0, 'ict': 0, 'mulct': 0}

while True:
    if 0 <= registers['ip'] <= last_instruction:
        iexec(registers, *instructions[registers['ip']])
        continue
    break

print registers['mulct']
