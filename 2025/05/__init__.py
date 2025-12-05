from pyutils import *


def parse(lines):
    ranges, ids = [], []
    i = 0
    while lines[i] != "":
        ranges.append(tuple(map(int, lines[i].split("-"))))
        i += 1

    ranges.sort()
    ranges_merged = [ranges[0]]
    for j in range(1, len(ranges)):
        if ranges_merged[-1][1] >= ranges[j][0]:
            ranges_merged[-1] = (
                ranges_merged[-1][0],
                max(ranges[j][1], ranges_merged[-1][1]),
            )
        else:
            ranges_merged.append(ranges[j])

    i += 1
    while i < len(lines):
        ids.append(int(lines[i]))
        i += 1
    return ranges_merged, ids


@expect({"test": 3})
def solve1(input):
    ranges, ids = input
    ans = 0
    for id in ids[:]:
        l, r = 0, len(ranges) - 1
        while l <= r:
            m = (l + r) // 2
            if id < ranges[m][0]:
                r = m - 1
            elif id > ranges[m][1]:
                l = m + 1
            else:
                ans += 1
                break
    return ans


@expect({"test": 14})
def solve2(input):
    return sum(r[1] - r[0] + 1 for r in input[0])
