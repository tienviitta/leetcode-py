from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        row = [0] * n
        row[n - 1] = 1
        for r in range(m - 1, -1, -1):
            col = [0] * n
            col[n - 1] = 0 if obstacleGrid[r][n - 1] else row[n - 1]
            for c in range(n - 2, -1, -1):
                col[c] = 0 if obstacleGrid[r][c] else row[c] + col[c + 1]
            row = col
        return row[0]


def test_ex1():
    """
    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    """
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    ref = 2
    sol = Solution()
    res = sol.uniquePathsWithObstacles(obstacleGrid)
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex2():
    """
    Input: obstacleGrid = [[0,1],[0,0]]
    Output: 1
    """
    obstacleGrid = [[0, 1], [0, 0]]
    ref = 1
    sol = Solution()
    res = sol.uniquePathsWithObstacles(obstacleGrid)
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex3():
    """
    Input: obstacleGrid = [[0,0],[1,1],[0,0]]
    Output: 1
    """
    obstacleGrid = [[0, 0], [1, 1], [0, 0]]
    ref = 0
    sol = Solution()
    res = sol.uniquePathsWithObstacles(obstacleGrid)
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
    test_ex2()
    test_ex3()
