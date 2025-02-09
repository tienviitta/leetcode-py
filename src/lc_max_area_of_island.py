from typing import Dict, List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        visited = set()
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, self.dfs(grid, row, col, visited))
        return max_area

    def dfs(self, grid: List[List[str]], row: int, col: int, visited: Dict):
        if (
            row < 0
            or col < 0
            or row == self.ROWS
            or col == self.COLS
            or grid[row][col] == 0
            or (row, col) in visited
        ):
            return 0
        visited.add((row, col))
        area = 1
        area += self.dfs(grid, row - 1, col, visited)  # Up
        area += self.dfs(grid, row, col + 1, visited)  # Right
        area += self.dfs(grid, row + 1, col, visited)  # Down
        area += self.dfs(grid, row, col - 1, visited)  # Left
        return area


def test_ex1():
    """
    Input: grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.
    """
    sol = Solution()
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    res = sol.maxAreaOfIsland(grid)
    ref = 6
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
