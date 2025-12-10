import itertools
from functools import cache

from pyutils import *


def parse(lines):
    return [tuple(map(int, line.split(","))) for line in lines]


@expect({"test": 50})
def solve1(reds):
    return max(
        (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        for (x1, y1), (x2, y2) in itertools.combinations(reds, 2)
    )


@expect({"test": 24})
def solve2(reds):
    xs_orig, ys_orig = [], []
    for x, y in reds:
        xs_orig.append(x)
        ys_orig.append(y)
    xs_orig.sort()
    ys_orig.sort()

    xs, ys = {}, {}
    for i, x in enumerate(xs_orig):
        xs[x] = i
    for i, y in enumerate(ys_orig):
        ys[y] = i

    for i, (x, y) in enumerate(reds):
        reds[i] = (xs[x] + 1, ys[y] + 1)

    grid = []
    for x in range(len(xs_orig) + 2):
        grid.append(["."] * (len(ys_orig) + 2))
    for i in range(len(reds)):
        x1, y1 = reds[i]
        x2, y2 = reds[(i + 1) % len(reds)]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1][y] = "#"
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[x][y1] = "#"

    q, outer = [(0, 0)], set()
    while q:
        x, y = q.pop()
        if (x, y) in outer:
            continue
        outer.add((x, y))
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if (
                0 <= x + dx < len(grid)
                and 0 <= y + dy < len(grid[0])
                and grid[x + dx][y + dy] == "."
            ):
                q.append((x + dx, y + dy))

    ans = 0
    for i in range(len(reds) - 1):
        for j in range(i + 1, len(reds)):
            x1, y1 = reds[i]
            x2, y2 = reds[j]
            if all(
                (x, y) not in outer
                for x in range(min(x1, x2), max(x1, x2) + 1)
                for y in range(min(y1, y2), max(y1, y2) + 1)
            ):
                ans = max(
                    ans,
                    (
                        (xs_orig[max(x1, x2) - 1] - xs_orig[min(x1, x2) - 1] + 1)
                        * (ys_orig[max(y1, y2) - 1] - ys_orig[min(y1, y2) - 1] + 1)
                    ),
                )
    return ans
