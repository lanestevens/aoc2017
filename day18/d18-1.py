# -*- coding: utf-8 -*-

import sys

registers = {}

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
    if registers.get(r, 0) > 0:
        try:
            registers['ip'] += int(v)
        except:
            registers['ip'] += registers.get(v, 0)
    else:
        registers['ip'] += 1
            
def i_rcv(registers, r):
    try:
        val = int(r)
    except:
        val = registers.get(r, 0)
    registers['ip'] += 1
    if val:
        print registers['snd']
        sys.exit()

def i_snd(registers, r):
    try:
        registers['snd'] = int(r)
    except:
        registers['snd'] = registers.get(r, 0)
    registers['ip'] += 1
    
registers = {'ip': 0, 'snd': None}

instructions = [x.strip() for x in sys.stdin.readlines()]
controller = {'snd': i_snd,
              'set': i_set,
              'add': i_add,
              'mul': i_mul,
              'mod': i_mod,
              'rcv': i_rcv,
              'jgz': i_jgz,
              }

i = 0
while True:
    i += 1
    instruction = instructions[registers['ip']].split()
    controller[instruction[0]](registers, *instruction[1:])
