from math import ceil
from typing import List


class Solution:
    def minEatingSpeedBf(self, piles: List[int], h: int) -> int:
        speed = 1  # [bananas per hour]
        while True:
            total = 0
            for pile in piles:
                total += ceil(pile / speed)
            if total <= h:
                return speed
            speed += 1

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        speed = right
        while left <= right:
            mid = (left + right) // 2
            total = 0
            for pile in piles:
                total += ceil(pile / mid)
            if total <= h:
                right = mid - 1
                speed = mid
            else:
                left = mid + 1
        return speed


def test_ex1():
    """
    Input: piles = [3,6,7,11], h = 8
    Output: 4
    """
    sol = Solution()
    piles = [3, 6, 7, 11]
    h = 8
    ref = 4
    res = sol.minEatingSpeed(piles, h)
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
