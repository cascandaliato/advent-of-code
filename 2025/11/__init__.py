from functools import cache

from pyutils import *


def parse(lines):
    adj = {}
    for line in lines:
        a, bs = line.split(": ")
        adj.setdefault(a, []).extend(bs.split())
    return adj


@expect({"test1": 5})
def solve1(adj):
    ans, q = 0, ["you"]
    while q:
        node = q.pop()
        if node == "out":
            ans += 1
            continue
        q.extend(adj[node])
    return ans


@expect({"test2": 2})
def solve2(adj):
    @cache
    def count(start, end, dac=False, fft=False):
        if start in (end, "out"):
            return int((start == end) and dac and fft)
        return sum(
            count(next_, end, dac or (start == "dac"), fft or (start == "fft"))
            for next_ in adj[start]
        )

    return count("svr", "out", False, False)
