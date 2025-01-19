import heapq
from typing import List


class MaxHeap:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def top(self):
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = MaxHeap()
        for stone in stones:
            max_heap.push(stone)
        # max_heap = [-stone for stone in stones]
        # heapq.heapify(max_heap)
        while len(max_heap) > 1:
            y, x = max_heap.pop(), max_heap.pop()
            if x != y:
                max_heap.push(y - x)
        # if len(max_heap) == 0:
        #     return 0
        # else:
        #     return max_heap.top()
        max_heap.push(0)
        return max_heap.top()


def test_ex1():
    """
    Input: stones = [2,7,4,1,8,1]
    Output: 1
    """
    sol = Solution()
    res = sol.lastStoneWeight([2, 7, 4, 1, 8, 1])
    ref = 1
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
