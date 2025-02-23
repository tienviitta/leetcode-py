from collections import deque
from typing import List
from icecream import ic


class Solution:
    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in self.neighbors:
                    row, col = r + dr, c + dc
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


# def is_out_of_bounds(r, c, NROWS, NCOLS):
#     return min(r, c) < 0 or r == NROWS or c == NCOLS


def test_ex1():
    """
    Input: grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]]
    Output: 4
    """
    sol = Solution()
    grid = grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    ic(__name__)
    res = sol.orangesRotting(grid)
    ref = 4
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex2():
    """
    Input: grid = [
        [2,1,1],
        [0,1,1],
        [1,0,1]]
    Output: -1
    """
    sol = Solution()
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    ic(__name__)
    res = sol.orangesRotting(grid)
    ref = -1
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex3():
    """
    Input: grid = [
        [0,2]]
    Output: 0
    """
    sol = Solution()
    grid = [[0, 2]]
    ic(__name__)
    res = sol.orangesRotting(grid)
    ref = 0
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex4():
    """
    Input: grid = [
        [1,2]]
    Output: 1
    """
    sol = Solution()
    grid = [[1, 2]]
    ic(__name__)
    res = sol.orangesRotting(grid)
    ref = 1
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
    test_ex2()
    test_ex3()
    test_ex4()
