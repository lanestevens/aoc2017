# -*- coding: utf-8 -*-

import sys

class Square(object):
    def __init__(self, enhancement_rules):
        self.enhancement_rules = enhancement_rules
        self.square = ['.#.', '..#', '###']

    def _rotate(self, square):
        size = len(square)
        rotated_square = ['' for x in range(size)]
        for row in reversed(square):
            for i in range(size):
                rotated_square[i] = rotated_square[i] + row[i]
        return rotated_square

    def _hflip(self, square):
        flipped_square = []
        for row in square:
            flipped_square.append(row[::-1])
        return flipped_square

    def _vflip(self, square):
        return square[::-1]

    def permute(self, square):
        permutations = []
        rotated_square = square
        for i in range(4):
            rotated_square = self._rotate(rotated_square)
            permutations.append('/'.join(rotated_square))
            permutations.append('/'.join(self._hflip(rotated_square)))
            permutations.append('/'.join(self._vflip(rotated_square)))
            permutations.append('/'.join(self._hflip(self._vflip(rotated_square))))
        return permutations

    def subdivide(self, square):
        size = len(square)
        subdivisions = []
        if size % 2 == 0:
            for i in range(0,size, 2):
                for j in range(0, size, 2):
                    subdivisions.append([square[i][j:j + 2], square[i + 1][j:j + 2]])
        elif size % 3 == 0:
            for i in range(0, size, 3):
                for j in range(0, size, 3):
                    subdivisions.append([square[i][j:j + 3],
                                         square[i + 1][j: j + 3],
                                         square[i + 2][j: j + 3]])
        return subdivisions

    def assemble(self, subsquares):
        size = int(len(subsquares)**0.5)
        assembled_square = []
        for i in range(size * len(subsquares[0])):
            adjustment = (i // len(subsquares[0])) * size
            offset = i  % len(subsquares[0])
            assembled_square.append(''.join([subsquares[adjustment + j][offset] for j in range(size)]))
        return assembled_square

    def count_ons(self):
        sum = 0
        for row in self.square:
            sum += row.count('#')
        return sum
    
    def iterate(self):
        subdivideds = self.subdivide(self.square)
        new_square = []
        for subdivided in subdivideds:
            for permuted in self.permute(subdivided):
                if permuted in self.enhancement_rules:
                    new_square.append(self.enhancement_rules[permuted].split('/'))
                    break
        self.square = self.assemble(new_square)

enhancement_rules = {}
for line in sys.stdin.readlines():
    k, v = line.strip().split(' => ')
    enhancement_rules[k] = v

square = Square(enhancement_rules)
for i in range(5):
    square.iterate()
print square.count_ons()

