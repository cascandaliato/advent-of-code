import functools
import operator

from pyutils import *

operators = {"+": operator.add, "*": operator.mul}


def parse(lines):
    return lines


@expect({"test": 4277556})
def solve1(input):
    nums = [list(map(int, l.split())) for l in input[:-1]]

    ans = 0
    for i, op in enumerate(input[-1].split()):
        ans += functools.reduce(operators[op], [nums[j][i] for j in range(len(nums))])
    return ans


@expect({"test": 3263827})
def solve2(input):
    problems = []
    for i, op in enumerate(input[-1]):
        if op == " ":
            continue
        problems.append((i, operators[op]))
    problems.append((len(input[-1]) + 1, None))

    ans = 0
    for i, (start, p) in enumerate(problems[:-1]):
        ans += functools.reduce(
            p,
            [
                int("".join(input[k][j] for k in range(len(input) - 1)))
                for j in range(start, problems[i + 1][0] - 1)
            ],
        )

    return ans
