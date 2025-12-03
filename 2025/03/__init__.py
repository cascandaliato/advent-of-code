from pyutils import *


def parse(lines):
    return [[int(d) for d in line] for line in lines]


@expect({"test": 357})
def solve1(batteries):
    ans = 0
    for battery in batteries:
        a, b = battery[-2:]
        for d in reversed(battery[:-2]):
            if d >= a:
                if a > b:
                    b = a
                a = d
        ans += 10 * a + b
    return ans


@expect({"test": 3121910778619})
def solve2(batteries):
    ans = 0
    for battery in batteries:
        active = battery[-12:]
        for d in reversed(battery[:-12]):
            for i in range(len(active)):
                if d >= active[i]:
                    active[i], d = d, active[i]
                else:
                    break
        ans += int("".join(map(str, active)))
    return ans
