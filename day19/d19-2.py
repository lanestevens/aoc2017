# -*- coding: utf-8 -*-

import sys

class Navigator(object):
    def __init__(self, diagram):
        self.diagram = diagram
        self.waypoints = []
        self.position = self._find_start()
        self.direction = 'down'
        self.max_right = len(self.diagram[0]) - 1
        self.max_down = len(self.diagram) - 1
        self.steps = 1

    def _find_start(self):
        return (0, self.diagram[0].index('|'))
        
    def move(self):
        if self.direction == 'down':
            self.position = (self.position[0] + 1, self.position[1])
        elif self.direction == 'up':
            self.position = (self.position[0] - 1, self.position[1])
        elif self.direction == 'right':
            self.position = (self.position[0], self.position[1] + 1)
        else:
            self.position = (self.position[0], self.position[1] - 1)

        if self.diagram[self.position[0]][self.position[1]] == ' ':
            return False
        elif self.diagram[self.position[0]][self.position[1]] == '+':
            if self.direction in ('down', 'up'):
                if self.position[1] == 0:
                    self.direction = 'right'
                elif self.position[1] == self.max_right:
                    self.direction = 'left'
                elif self.diagram[self.position[0]][self.position[1] - 1] == ' ':
                    self.direction = 'right'
                else:
                    self.direction = 'left'
            else:
                if self.position[0] == 0:
                    self.direction = 'down'
                elif self.position[0] == self.max_down:
                    self.direction = 'up'
                elif self.diagram[self.position[0] + 1][self.position[1]] == ' ':
                    self.direction = 'up'
                else:
                    self.direction = 'down'
        elif self.diagram[self.position[0]][self.position[1]] not in ('|', '-', '+'):
            self.waypoints.append(self.diagram[self.position[0]][self.position[1]])
        self.steps += 1
        return True

diagram = [x.rstrip('\n') for x in sys.stdin.readlines()]
navigator = Navigator(diagram)
while navigator.move():
    pass
print navigator.steps



