import functools
import operator

from pyutils import *


class UnionFind:
    def __init__(self, elements):
        self.parent = {el: el for el in elements}
        self.size = {el: 1 for el in elements}

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        del self.size[root_b]


def parse(lines):
    boxes = [tuple(map(int, line.split(","))) for line in lines]
    distances = []
    for i in range(len(boxes) - 1):
        for j in range(i + 1, len(boxes)):
            distances.append(
                (
                    sum((boxes[i][k] - boxes[j][k]) ** 2 for k in (0, 1, 2)),
                    boxes[i],
                    boxes[j],
                )
            )
    return boxes, sorted(distances)


@expect({"test": 40})
def solve1(input):
    boxes, distances = input
    uf = UnionFind(boxes)
    for _, a, b in distances[: 10 if len(boxes) == 20 else 1000]:
        uf.union(a, b)
    return functools.reduce(operator.mul, sorted(uf.size.values(), reverse=True)[:3])


@expect({"test": 25272})
def solve2(input):
    boxes, distances = input
    uf = UnionFind(boxes)
    for _, a, b in distances:
        uf.union(a, b)
        if len(uf.size) == 1:
            return a[0] * b[0]
