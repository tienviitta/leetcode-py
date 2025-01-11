from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next = next


def linked_list_from_list(lst: List[int]) -> Optional[ListNode]:
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_list_to_list(ln: Optional[ListNode]) -> List[int]:
    lst = []
    head = ln
    while head:
        lst.append(head.val)
        head = head.next
    return lst


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_from_list(lst: List[int]) -> Optional[TreeNode]:
    root = TreeNode(lst[0])
    for val in lst[1:]:
        bst_insert(root, val)
    return root


def bst_insert(root: Optional[TreeNode], val) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)
    elif val < root.val:
        root.left = bst_insert(root.left, val)
    else:
        root.right = bst_insert(root.right, val)
    return root


def bst_to_list(root: Optional[TreeNode]) -> List[int]:
    lst = []
    bst_traverse(root, lst)
    return lst


def bst_traverse(root: Optional[TreeNode], lst: List[int]):
    if root:
        lst.append(root.val)
        bst_traverse(root.left, lst)
        bst_traverse(root.right, lst)
