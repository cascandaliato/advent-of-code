import functools
import operator

from pyutils import *

operators = {"+": operator.add, "*": operator.mul}


def parse(lines):
    return lines


@expect({"test": 4277556})
def solve1(lines):
    return sum(
        functools.reduce(operators[operation], map(int, nums))
        for *nums, operation in zip(*map(str.split, lines))
    )


@expect({"test": 3263827})
def solve2(lines):
    ans, operands, i = 0, [], len(lines[0]) - 1
    while i >= 0:
        operands.append(int("".join(lines[j][i] for j in range(len(lines) - 1))))
        if operator := operators.get(lines[-1][i], None):
            ans += functools.reduce(operator, operands)
            operands, i = [], i - 1
        i -= 1
    return ans
