# -*- coding: utf-8 -*-

import sys

def i_set(registers, r, v):
    try:
        registers[r] = int(v)
    except:
        registers[r] = registers.get(v, 0)
    registers['ip'] += 1

def i_add(registers, r, v):
    try:
        registers[r] = registers.get(r, 0) + int(v)
    except:
        registers[r] = registers.get(r, 0) + registers.get(v, 0)
    registers['ip'] += 1

def i_mul(registers, r, v):
    try:
        registers[r] = registers.get(r, 0) * int(v)
    except:
        registers[r] = registers.get(r, 0) * registers.get(v, 0)
    registers['ip'] += 1

def i_mod(registers, r, v):
    try:
        registers[r] = registers.get(r, 0) % int(v)
    except:
        registers[r] = registers.get(r, 0) % registers.get(v, 0)
    registers['ip'] += 1

def i_jgz(registers, r, v):
    try:
        t = int(r)
    except:
        t = registers.get(r, 0)
        
    if t > 0:
        try:
            registers['ip'] += int(v)
        except:
            registers['ip'] += registers.get(v, 0)
    else:
        registers['ip'] += 1
            
def i_rcv(registers, r):
    if not registers['queue']:
        return
    registers[r] = registers['queue'][0]
    registers['queue'] = registers['queue'][1:]
    registers['ip'] = registers['ip'] + 1

def i_snd(registers, r, other_registers):
    try:
        other_registers['queue'].append(int(r))
    except:
        other_registers['queue'].append(registers.get(r, 0))
    registers['count'] += 1
    registers['ip'] += 1
    
registers = [{'ip': 0, 'p': 0, 'queue': [], 'count': 0, 'id': 0},
             {'ip': 0, 'p': 1, 'queue': [], 'count': 0, 'id': 1},
             ]

instructions = [x.strip() for x in sys.stdin.readlines()]
controller = {'snd': i_snd,
              'set': i_set,
              'add': i_add,
              'mul': i_mul,
              'mod': i_mod,
              'rcv': i_rcv,
              'jgz': i_jgz,
              }

dones = [False, False]
blocks = [False, False]
while True:
    for i in range(2):
        blocks[i] = instructions[registers[i]['ip']].startswith('rcv') and not registers[i]['queue']
    if blocks[0] and blocks[1]:
        break
    if blocks[0] and dones[1] or dones[0] and blocks[1]:
        break
    if dones[0] and blocks[1] or blocks[0] and dones[1]:
        break
    if dones[0] and dones[1]:
        break
    for i in range(2):
        if dones[i]:
            continue
        if registers[i]['ip'] < 0 or registers[i]['ip'] >= len(instructions):
            dones[i] = True
            continue
        instruction = instructions[registers[i]['ip']].split()
        if instruction[0] == 'snd':
            instruction.append(registers[(i + 1) % 2])
        controller[instruction[0]](registers[i], *instruction[1:])

print registers[1]['count']
