from typing import Dict, List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islands += self.dfs(grid, row, col, visited)
        return islands

    def dfs(self, grid: List[List[str]], row: int, col: int, visited: Dict):
        ROWS = len(grid)
        COLS = len(grid[0])
        if (
            row < 0
            or col < 0
            or row == ROWS
            or col == COLS
            or grid[row][col] == "0"
            or (row, col) in visited
        ):
            return 0
        visited.add((row, col))
        self.dfs(grid, row - 1, col, visited)  # Up
        self.dfs(grid, row, col + 1, visited)  # Right
        self.dfs(grid, row + 1, col, visited)  # Down
        self.dfs(grid, row, col - 1, visited)  # Left
        return 1


def test_ex1():
    """
    Example 1:

    Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    Output: 1
    """
    sol = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    res = sol.numIslands(grid)
    ref = 1
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex2():
    """
    Example 2:
    Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    Output: 3
    """
    sol = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    res = sol.numIslands(grid)
    ref = 3
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
    test_ex2()
