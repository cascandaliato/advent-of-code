import collections

from pyutils import *


def parse(lines):
    return lines


@expect({"test": 21})
def solve1(lines):
    beams, ans = set(), 0
    for line in lines[::2]:
        beams_next = set()
        for i, c in enumerate(line):
            if c == "S":
                beams_next.add(i)
            elif c == "." and i in beams:
                beams_next.add(i)
            elif c == "^" and i in beams:
                ans += 1
                beams_next.add(i - 1)
                beams_next.add(i + 1)
        beams = beams_next
    return ans


@expect({"test": 40})
def solve2(lines):
    beams = collections.Counter()
    for line in lines[::2]:
        beams_next = collections.Counter()
        for i, c in enumerate(line):
            if c == "S":
                beams_next[i] += 1
            elif c == "." and i in beams:
                beams_next[i] += beams[i]
            elif c == "^" and i in beams:
                beams_next[i - 1] += beams[i]
                beams_next[i + 1] += beams[i]
        beams = beams_next
    return sum(beams.values())
