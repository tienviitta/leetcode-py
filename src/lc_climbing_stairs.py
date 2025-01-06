class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one

    def climbStairsRec(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairsRec(n - 1) + self.climbStairsRec(n - 2)

    cache = {}

    def climbStairsMem(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.cache:
            return self.cache[n]
        else:
            self.cache[n] = self.climbStairsMem(n - 1) + self.climbStairsMem(n - 2)
        return self.cache[n]


def test_ex1():
    """
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    """
    sol = Solution()
    assert sol.climbStairs(2) == 2
    assert sol.climbStairsRec(2) == 2


def test_ex2():
    """
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    """
    sol = Solution()
    assert sol.climbStairs(3) == 3
    assert sol.climbStairsRec(3) == 3


def test_ex3():
    """
    Input: n = 5
    Output: 8
    ...
    """
    sol = Solution()
    assert sol.climbStairs(5) == 8
    assert sol.climbStairsRec(5) == 8
    assert sol.climbStairsMem(5) == 8


if __name__ == "__main__":
    test_ex1()
    test_ex2()
    test_ex3()
