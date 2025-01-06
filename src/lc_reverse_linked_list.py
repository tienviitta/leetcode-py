from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new = head
        if head.next:
            new = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return new


def from_list(lst: List[int]) -> Optional[ListNode]:
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def to_list(ln: Optional[ListNode]) -> List[int]:
    lst = []
    head = ln
    while head:
        lst.append(head.val)
        head = head.next
    return lst


def test_ex1():
    """
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
    """
    sol = Solution()
    # head = ListNode(1, ListNode(2, ListNode(3)))
    inp = [1, 2, 3, 4, 5]
    head = from_list(inp)
    res = sol.reverseList(head)
    out = to_list(res)
    assert out == inp[::-1]


if __name__ == "__main__":
    test_ex1()
