import itertools

import z3

from pyutils import *


def parse(lines):
    machines = []
    for line in lines:
        diagram, *wiring, joltage = line.split()
        diagram = list(0 if c == "." else 1 for c in diagram[1:-1])
        wiring = list(set(map(int, w[1:-1].split(","))) for w in wiring)
        joltage = list(map(int, joltage[1:-1].split(",")))
        machines.append((diagram, wiring, joltage))
    return machines


@expect({"test": 7})
def solve1(machines):
    def shortest(diagram, wiring):
        for l in range(len(wiring)):
            for buttons in itertools.combinations(wiring, l + 1):
                current = [0] * len(diagram)
                for button in buttons:
                    for i in button:
                        current[i] = 1 - current[i]
                if current == diagram:
                    return l + 1

    return sum(shortest(diagram, wiring) for diagram, wiring, _ in machines)


@expect({"test": 33})
def solve2(machines):
    ans = 0
    for _, wiring, joltage in machines:
        s = z3.Optimize()
        vars = z3.Ints(" ".join(f"x{i}" for i in range(len(wiring))))
        s.add(vars[i] >= 0 for i in range(len(vars)))
        for i in range(len(joltage)):
            s.add(
                z3.Sum([vars[j] for j in range(len(vars)) if i in wiring[j]])
                == joltage[i]
            )
        h = s.minimize(z3.Sum(vars))
        if s.check() == z3.sat:
            ans += s.lower(h).as_long()
    return ans
