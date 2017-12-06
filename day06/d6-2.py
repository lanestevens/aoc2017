# -*- coding: utf-8 -*-

import sys

history = set([])
memory_banks = [int(x) for x in sys.stdin.readline().strip().split('\t')]

num_banks = len(memory_banks)
while True:
    i = memory_banks.index(max(memory_banks))
    blocks_to_redistribute = memory_banks[i]
    memory_banks[i] = 0
    while blocks_to_redistribute:
        i = (i + 1) % num_banks
        memory_banks[i] += 1
        blocks_to_redistribute -= 1
    this = tuple(memory_banks)
    if this in history:
        break
    history.add(this)

count = 0
target = this
while True:
    count += 1
    i = memory_banks.index(max(memory_banks))
    blocks_to_redistribute = memory_banks[i]
    memory_banks[i] = 0
    while blocks_to_redistribute:
        i = (i + 1) % num_banks
        memory_banks[i] += 1
        blocks_to_redistribute -= 1
    if tuple(memory_banks) == target:
        break
print count
