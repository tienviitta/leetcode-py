from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next = next


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
