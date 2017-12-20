# -*- coding: utf-8 -*-

import sys

class Particle(object):
    def __init__(self, spec):
        items = spec.split(', ')
        self.p = self._decode(items[0])
        self.v = self._decode(items[1])
        self.a = self._decode(items[2])

    def _decode(self, item):
        v1, v2, v3 = item.split(',')
        return (int(v1.split('<')[1]), int(v2), int(v3.split('>')[0]))

    def move(self):
        self.v = (self.v[0] + self.a[0],
                  self.v[1] + self.a[1],
                  self.v[2] + self.a[2])
        self.p = (self.p[0] + self.v[0],
                  self.p[1] + self.v[1],
                  self.p[2] + self.v[2])

    def manhatten_distance(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

particles = []
for line in sys.stdin.readlines():
    particles.append(Particle(line))

for i in range(5000):
    positions = {}
    for particle in particles:
        particle.move()
        if particle.p in positions:
            positions[particle.p].append(particle)
        else:
            positions[particle.p] = [particle]
    collisions = {x for x in positions.keys() if len(positions[x]) > 1}
    particles = [x for x in particles if x.p not in collisions]

print len(particles)

