import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


class MyKthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k + 1
        self.heap = [0]
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.push(val)
        while len(self.heap) > self.k:
            self.pop()
        return self.heap[1]

    def push(self, val: int):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        res = self.heap[1]
        # Move last value to root
        self.heap[1] = self.heap.pop()
        i = 1
        # Percolate down
        while 2 * i < len(self.heap):
            if (
                2 * i + 1 < len(self.heap)
                and self.heap[2 * i + 1] < self.heap[2 * i]
                and self.heap[i] > self.heap[2 * i + 1]
            ):
                # Swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # Swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res


def test_ex1():
    """
    Input:
    ["KthLargest", "add", "add", "add", "add", "add"]
    [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    Output: [null, 4, 5, 5, 8, 8]
    Explanation:
    KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
    kthLargest.add(3); // return 4
    kthLargest.add(5); // return 5
    kthLargest.add(10); // return 5
    kthLargest.add(9); // return 8
    kthLargest.add(4); // return 8
    """
    # fmt: off
    cmds = [
        ["KthLargest", [3, [4, 5, 8, 2]], None], 
        ["add", [3], 4], 
        ["add", [5], 5], 
        ["add", [10], 5], 
        ["add", [9], 8], 
        ["add", [4], 8], 
    ]
    # fmt: on
    sol = None
    for cmd in cmds:
        match cmd[0]:
            case "KthLargest":
                sol = KthLargest(cmd[1][0], cmd[1][1])
            case "add":
                res = sol.add(cmd[1][0])
                ref = cmd[2]
                assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex2():
    """
    Input:
    ["KthLargest", "add", "add", "add", "add"]
    [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
    Output: [null, 7, 7, 7, 8]
    """
    # fmt: off
    cmds = [
        ["KthLargest", [4, [7, 7, 7, 7, 8, 3]], None], 
        ["add", [2], 7], 
        ["add", [10], 7], 
        ["add", [9], 7], 
        ["add", [9], 8], 
    ]
    # fmt: on
    sol = None
    for cmd in cmds:
        match cmd[0]:
            case "KthLargest":
                sol = KthLargest(cmd[1][0], cmd[1][1])
            case "add":
                res = sol.add(cmd[1][0])
                ref = cmd[2]
                assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
    test_ex2()
