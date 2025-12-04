from pyutils import *


def parse(lines):
    return [list(line) for line in lines]


@expect({"test": 13})
def solve1(grid):
    ans = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != "@":
                continue
            adj_rolls = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if (
                        0 <= r + dr < len(grid)
                        and 0 <= c + dc < len(grid[0])
                        and grid[r + dr][c + dc] == "@"
                    ):
                        adj_rolls += 1
            if adj_rolls < 5:
                ans += 1
    return ans


@expect({"test": 43})
def solve2(grid):
    def is_paper_roll(r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "@"

    ans, q = 0, [(r, c) for r in range(len(grid)) for c in range(len(grid[0]))]
    while q:
        r, c = q.pop()
        if not is_paper_roll(r, c):
            continue
        adj_rolls = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if is_paper_roll(r + dr, c + dc):
                    adj_rolls += 1
        if adj_rolls < 5:
            ans += 1
            grid[r][c] = "."
            q.extend((r + dr, c + dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1))
    return ans
