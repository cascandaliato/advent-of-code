from pyutils import *


def parse(lines):
    return [int(line[1:]) * (+1 if line[0] == "R" else -1) for line in lines]


@expect({"test": 3})
def solve1(rotations):
    pos, ans = 50, 0
    for r in rotations:
        pos = (pos + r) % 100
        ans += pos == 0
    return ans


@expect({"test": 6})
def solve2(rotations):
    pos, ans = 50, 0
    for r in rotations:
        ans += (pos + r) // 100 if r > 0 else ((100 - pos) % 100 - r) // 100
        pos = (pos + r) % 100
    return ans
