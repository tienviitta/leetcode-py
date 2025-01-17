from collections import deque
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
    if not lst:
        return None
    it = iter(lst)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root


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
    bst_preorder(root, lst)
    # bst_postorder(root, lst)
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


def bst_bfs(root: Optional[TreeNode]) -> List[int]:
    lst = []
    queue = deque()
    if root:
        queue.append(root)
    # level = 0
    while len(queue) > 0:
        # print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            # print(curr.val)
            lst.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        # level += 1
    return lst
