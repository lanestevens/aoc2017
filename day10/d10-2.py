# -*- coding: utf-8 -*-

import sys

s = range(256)
list_length = len(s)
current_position = 0
skip_size = 0

lengths = [ord(x) for x in sys.stdin.readline().strip()] + [17, 31, 73, 47, 23]

for i in range(64):
    for length in lengths:
        if length <= 1:
            pass
        elif current_position + length >= list_length:
            rollover = (current_position + length) % list_length
            segment = s[current_position:] + s[0:(current_position + length) % list_length]
            segment.reverse()
            s = segment[length - rollover:] + s[rollover:current_position] + segment[0:length - rollover]
        else:
            segment = s[current_position: current_position + length]
            segment.reverse()
            s = s[0:current_position] + segment + s[current_position + length:]
        current_position += length + skip_size
        if current_position > list_length:
            current_position = current_position % list_length
        skip_size += 1

result = []
for i in range(16):
    val = 0
    for j in range(16):
        val = val ^ s[j]
    result.append(val)
    s = s[16:]

hex = ''
for v in result:
    hex += '{:02x}'.format(v)

print hex


