# -*- coding: utf-8 -*-

class Turing(object):
    def __init__(self):
        self.tape = {}
        self.cursor = 0
        self.state = 'A'
        self.iterations = 0
        self.transitions = {'A': ((1, 1, 'B'), (0, -1, 'C')),
                            'B': ((1, -1, 'A'), (1, 1, 'D')),
                            'C': ((1, 1, 'A'), (0, -1, 'E')),
                            'D': ((1, 1, 'A'), (0, 1, 'B')),
                            'E': ((1, -1, 'F'), (1, -1, 'C')),
                            'F': ((1, 1, 'D'), (1, 1, 'A')),
                            }

    def process(self):
        this_transition = self.transitions[self.state][self.tape.get(self.cursor, 0)]
        self.tape[self.cursor] = this_transition[0]
        self.cursor += this_transition[1]
        self.state = this_transition[2]
        self.iterations += 1

    def checksum(self):
        return sum([x for x in self.tape.values()])

t = Turing()
for i in range(12919244):
    t.process()
print t.checksum()

            
