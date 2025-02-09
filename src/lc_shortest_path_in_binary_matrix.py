from collections import deque
from typing import List


class Solution:
    neighbors = [
        [0, 1],
        [1, 1],
        [0, -1],
        [-1, -1],
        [1, 0],
        [1, -1],
        [-1, 0],
        [-1, 1],
    ]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0, 0, 1)])  # r, c, length
        visit = set((0, 0))
        while q:
            r, c, length = q.popleft()
            if min(r, c) < 0 or max(r, c) == N or grid[r][c] == 1:
                continue
            if r == N - 1 and c == N - 1:
                return length
            for dr, dc in self.neighbors:
                if (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
        return -1


def test_ex1():
    """
    Input: grid = [[0,1],[1,0]]
    Output: 2
    """
    sol = Solution()
    grid = grid = [[0, 1], [1, 0]]
    res = sol.shortestPathBinaryMatrix(grid)
    ref = 2
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex2():
    """
    Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4
    """
    sol = Solution()
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    res = sol.shortestPathBinaryMatrix(grid)
    ref = 4
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex3():
    """
    Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
    Output: -1
    """
    sol = Solution()
    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    res = sol.shortestPathBinaryMatrix(grid)
    ref = -1
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
    test_ex2()
    test_ex3()
