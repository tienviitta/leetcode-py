from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for num in nums:
            if num in numsSet:
                return True
            numsSet.add(num)
        return False

    def containsDuplicateMap(self, nums: List[int]) -> bool:
        numsMap = {}
        for num in nums:
            if num in numsMap:
                return True
            else:
                numsMap[num] = True
        return False


def test_ex1():
    """
    Input: nums = [1,2,3,1]
    Output: true
    Explanation:
    The element 1 occurs at the indices 0 and 3.
    """
    sol = Solution()
    nums = [1, 2, 3, 1]
    res = sol.containsDuplicate(nums)
    ref = True
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex2():
    """
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true
    Explanation:
    The element 1 occurs at the indices 0 and 3.
    """
    sol = Solution()
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    res = sol.containsDuplicate(nums)
    ref = True
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
    test_ex2()
