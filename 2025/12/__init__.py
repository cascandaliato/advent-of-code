from pyutils import *


def parse(lines):
    shapes, problems = [], []
    i = 0
    while i < len(lines):
        if len(lines[i]) == 2:
            shapes.append(lines[i + 1 : i + 4])
            i += 5
        else:
            grid, num_shapes = lines[i].split(": ")
            grid_x, grid_y = map(int, grid.split("x"))
            problems.append(((grid_x, grid_y), list(map(int, num_shapes.split()))))
            i += 1
    return shapes, problems


def solve1(input):
    shapes, problems = input
    shapes = [len([c for row in shape for c in row if c == "#"]) for shape in shapes]

    ans = 0
    for (x, y), num_shapes in problems:
        if (x // 3) * (y // 3) >= sum(num_shapes):
            ans += 1
    return ans
