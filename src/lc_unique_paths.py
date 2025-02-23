class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * n
        for r in range(m - 1, -1, -1):
            col = [0] * n
            col[n - 1] = 1
            for c in range(n - 2, -1, -1):
                col[c] = row[c] + col[c + 1]
            row = col
        return row[0]


def test_ex1():
    """
    Input: m = 3, n = 7
    Output: 28
    """
    m = 3
    n = 7
    ref = 28
    sol = Solution()
    res = sol.uniquePaths(m, n)
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex2():
    """
    Input: m = 3, n = 2
    Output: 3
    """
    m = 3
    n = 7
    ref = 28
    sol = Solution()
    res = sol.uniquePaths(m, n)
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
    test_ex2()
