from pyutils import *


def parse(lines):
    ranges = []
    for range in lines[0].split(","):
        ranges.append(tuple(map(int, range.split("-"))))
    return list(sorted(ranges))


def gen(ranges, repeat=2):
    n, i, candidates = 1, 0, set()
    while True:
        s = int(repeat * str(n))
        while i < len(ranges) and s > ranges[i][1]:
            i += 1
        if i == len(ranges):
            break
        if ranges[i][0] <= s <= ranges[i][1]:
            candidates.add(s)
        n += 1
    return candidates


def solve(ranges, candidates):
    i, ans = 0, 0
    for c in sorted(candidates):
        while i < len(ranges) and c > ranges[i][1]:
            i += 1
        if i == len(ranges):
            break
        if ranges[i][0] <= c <= ranges[i][1]:
            ans += c
    return ans


@expect({"test": 1227775554})
def solve1(ranges):
    return solve(ranges, gen(ranges))


@expect({"test": 4174379265})
def solve2(ranges):
    candidates = set()
    for repeat in range(2, len(str(ranges[-1][1])) + 1):
        candidates.update(gen(ranges, repeat))
    return solve(ranges, candidates)
