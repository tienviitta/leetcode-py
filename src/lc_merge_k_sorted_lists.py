from queue import PriorityQueue
from utils import ListNode, from_list, to_list
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        for i in range(1, len(lists)):
            lists[i] = self.mergeList(lists[i - 1], lists[i])
        return lists[-1]

    def mergeList(self, l1, l2):
        """
        Merge two lists into one.
        """
        head = ListNode()
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return head.next

    def mergeKListsPq(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = PriorityQueue()
        for list in lists:
            curr = ListNode()
            curr = list
            while curr:
                pq.put(curr.val)
                curr = curr.next
        head = ListNode()
        curr = head
        while not pq.empty():
            new = ListNode(pq.get())
            curr.next = new
            curr = new
        return head.next


def test_ex1():
    """
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6
    """
    sol = Solution()
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    linkedLists = []
    for lst in lists:
        linkedLists.append(from_list(lst))
    resLinkedList = sol.mergeKLists(linkedLists)
    resList = to_list(resLinkedList)
    assert resList == [1, 1, 2, 3, 4, 4, 5, 6]


def test_ex2():
    """
    Input: lists = [
        [-6,-3,-1,1,2,2,2],
        [-10,-8,-6,-2,4],
        [-2],
        [-8,-4,-3,-3,-2,-1,1,2,3],
        [-8,-6,-5,-4,-2,-2,2,4]]
    Output: [-10,-8,-8,-8,-6,-6,-6,-5,-4,-4,-3,-3,-3,
            -2,-2,-2,-2,-2,-1,-1,1,1,2,2,2,2,2,3,4,4]
    """
    sol = Solution()
    lists = [
        [-6, -3, -1, 1, 2, 2, 2],
        [-10, -8, -6, -2, 4],
        [-2],
        [-8, -4, -3, -3, -2, -1, 1, 2, 3],
        [-8, -6, -5, -4, -2, -2, 2, 4],
    ]
    linkedLists = []
    for lst in lists:
        linkedLists.append(from_list(lst))
    resLinkedList = sol.mergeKLists(linkedLists)
    resList = to_list(resLinkedList)
    # fmt: off
    assert resList == [
        -10, -8, -8, -8, -6, -6, -6, -5, -4, -4, -3, -3, -3, 
        -2, -2, -2, -2, -2, -1, -1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 4]
    # fmt: on


def test_ex3():
    """
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6
    """
    sol = Solution()
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    linkedLists = []
    for lst in lists:
        linkedLists.append(from_list(lst))
    resLinkedList = sol.mergeKListsPq(linkedLists)
    resList = to_list(resLinkedList)
    assert resList == [1, 1, 2, 3, 4, 4, 5, 6]


if __name__ == "__main__":
    # test_ex1()
    # test_ex2()
    test_ex3()
