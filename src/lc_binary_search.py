from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Find the middle of the array 📍
        Check if target found! 🎯
        If target is bigger, look right ➡️
        If target is smaller, look left ⬅️
        Repeat until found or not found! 🔄
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


def test_ex1():
    """
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4
    """
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    ref = 4
    res = sol.search(nums, target)
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex2():
    """
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1
    """
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    ref = -1
    res = sol.search(nums, target)
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
    test_ex2()
