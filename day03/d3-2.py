# -*- coding: utf-8 -*-

import sys

def next_coordinate(xy):
    #special case for origin
    if xy == (0, 0):
        return (1, 0)
    #Bottom right - move out to the right
    if xy[0] > 0 and xy[0] == -xy[1]:
        return (xy[0] + 1, xy[1])
    #Top right - move to the left
    if xy[0] > 0 and xy[0] == xy[1]:
        return (xy[0] - 1, xy[1])
    #Top left - move down
    if xy[0] < 0 and xy[0] == -xy[1]:
        return (xy[0], xy[1] - 1)
    #Bottom left - move right
    if xy[0] < 0 and xy[0] == xy[1]:
        return (xy[0] + 1, xy[1])
    #Mid right - move up
    if xy[0] > 0 and abs(xy[0]) > abs(xy[1]):
        return (xy[0], xy[1] + 1)
    #Mid top - move left
    if xy[1] > 0 and xy[1] > abs(xy[0]):
        return (xy[0] - 1, xy[1])
    #Mid left - move down
    if xy[0] < 0 and abs(xy[0]) > abs(xy[1]):
        return (xy[0], xy[1] - 1)
    #Bottom - move right:
    if xy[1] < 0 and abs(xy[0]) < abs(xy[1]):
        return (xy[0] + 1, xy[1])

target = int(sys.stdin.readline().strip())
ram = {}
for i in range(1, target + 1):
    if i == 1:
        xy = (0, 0)
        ram[xy] = 1
    else:
        xy = next_coordinate(xy)
        ram[xy] =   ram.get((xy[0] + 1, xy[1]), 0)\
                  + ram.get((xy[0] - 1, xy[1]), 0)\
                  + ram.get((xy[0], xy[1] + 1), 0)\
                  + ram.get((xy[0], xy[1] - 1), 0)\
                  + ram.get((xy[0] + 1, xy[1] + 1), 0)\
                  + ram.get((xy[0] + 1, xy[1] - 1), 0)\
                  + ram.get((xy[0] - 1, xy[1] + 1), 0)\
                  + ram.get((xy[0] - 1, xy[1] - 1), 0)
        if ram[xy] > target:
            print ram[xy]
            break

    
