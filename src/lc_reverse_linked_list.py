from utils import ListNode, linked_list_from_list, linked_list_to_list
from typing import Optional


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


def test_ex1():
    """
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
    """
    sol = Solution()
    # head = ListNode(1, ListNode(2, ListNode(3)))
    inp = [1, 2, 3, 4, 5]
    head = linked_list_from_list(inp)
    res = sol.reverseList(head)
    out = linked_list_to_list(res)
    assert out == inp[::-1]


if __name__ == "__main__":
    test_ex1()
