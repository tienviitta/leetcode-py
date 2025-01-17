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
    # root = TreeNode(lst[0])
    # for val in lst[1:]:
    #     bst_insert(root, val)
    # return root
    if not lst:
        return None
    root = TreeNode(lst.pop())
    bst(root, lst)
    return root


def bst(root, lst):
    while lst:
        pass


def bst_insert(root: Optional[TreeNode], val) -> Optional[TreeNode]:
    if not val:
        return None
    if not root:
        return TreeNode(val)
    elif val < root.val:
        root.left = bst_insert(root.left, val)
    else:
        root.right = bst_insert(root.right, val)
    return root


def bst_to_list(root: Optional[TreeNode]) -> List[int]:
    lst = []
    # bst_inorder(root, lst)
    # bst_preorder(root, lst)
    bst_postorder(root, lst)
    return lst


def bst_preorder(root: Optional[TreeNode], lst: List[int]):
    if not root:
        return
    lst.append(root.val)
    bst_preorder(root.left, lst)
    bst_preorder(root.right, lst)


def bst_inorder(root: Optional[TreeNode], lst: List[int]):
    if not root:
        return
    bst_inorder(root.left, lst)
    lst.append(root.val)
    bst_inorder(root.right, lst)


def bst_postorder(root: Optional[TreeNode], lst: List[int]):
    if not root:
        return
    bst_postorder(root.left, lst)
    bst_postorder(root.right, lst)
    lst.append(root.val)
