from collections import Counter
from random import shuffle

from pyutils import *


# Source (roll + turn + rotations): https://stackoverflow.com/a/16467849

def roll(v): return (v[0], v[2], -v[1])
def turn(v): return (-v[1], v[0], v[2])


def rotations(coords):
    for _ in range(2):
        for _ in range(3):
            coords = set(roll(c) for c in coords)
            yield(coords)
            for _ in range(3):
                coords = set(turn(c) for c in coords)
                yield(coords)
        coords = set(roll(turn(roll(c))) for c in coords)


def parse(lines):
    return [set(tuple(int(n) for n in beacon.split(',')) for beacon in beacons[1:])
            for beacons in split_by_empty_line(lines)]


def match(s1, done, offsets):
    shuffle(done)
    for i2 in done:
        s2 = offsets[i2][1]
        for s1r in rotations(s1):
            deltas = []
            for b1 in s1r:
                for b2 in s2:
                    deltas.append((b1[0]-b2[0], b1[1]-b2[1], b1[2]-b2[2]))
            delta, freq = Counter(deltas).most_common(1)[0]
            if freq >= 12:
                return (i2, s1r, delta)


def calculate_offsets(scanners):
    done, todo = [0], list(range(1, len(scanners)))
    offsets = [(0, scanners[0], (0, 0, 0))] + [None]*(len(scanners)-1)

    while todo:
        shuffle(todo)
        for idx in todo:
            offsets[idx] = match(scanners[idx], done, offsets)
            if offsets[idx]:
                todo.remove(idx)
                done.append(idx)
                break

    return offsets


@expect({'test': 79})
def solve1(scanners):
    offsets = calculate_offsets(scanners)
    all_beacons = set()
    for i in range(len(scanners)):
        ref, beacons, (dx, dy, dz) = offsets[i]
        beacons = set((b[0]-dx, b[1]-dy, b[2]-dz) for b in beacons)
        while ref != 0:
            ref, _, (dx, dy, dz) = offsets[ref]
            beacons = set((b[0]-dx, b[1]-dy, b[2]-dz) for b in beacons)
        all_beacons = all_beacons.union(beacons)
    return len(all_beacons)


@expect({'test': 3621})
def solve2(scanners):
    offsets, positions, max_distance = calculate_offsets(scanners), [], -1
    for i in range(len(scanners)):
        ref, _, position = offsets[i]
        while ref != 0:
            ref, _, (dx, dy, dz) = offsets[ref]
            position = (position[0]+dx, position[1]+dy, position[2]+dz)
        positions.append(position)
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            max_distance = max(max_distance, sum(abs(a-b)
                               for a, b in zip(positions[i], positions[j])))
    return max_distance
