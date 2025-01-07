from typing import List

BUCKETS = [0, 1, 2]


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        j = 0
        for i, bucket in enumerate(counts):
            for n in range(bucket):
                nums[j] = BUCKETS[i]
                j += 1


def test_ex1():
    """
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    """
    sol = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


if __name__ == "__main__":
    test_ex1()
