from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, num in enumerate(nums):
            seen = target - num
            if seen in cache:
                return [cache[seen], i]
            cache[num] = i
        return []


def test_ex1():
    """
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = sol.twoSum(nums, target)
    ref = [0, 1]
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex2():
    """
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    """
    sol = Solution()
    nums = [3, 2, 4]
    target = 6
    res = sol.twoSum(nums, target)
    ref = [1, 2]
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex3():
    """
    Input: nums = [3,3], target = 6
    Output: [0,1]
    """
    sol = Solution()
    nums = [3, 3]
    target = 6
    res = sol.twoSum(nums, target)
    ref = [0, 1]
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
    test_ex2()
    test_ex3()
