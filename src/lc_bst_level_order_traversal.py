# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        queue = deque()
        if root:
            queue.append(root)
        res = []
        while len(queue) > 0:
            lst = []
            for i in range(len(queue)):
                curr = queue.popleft()
                lst.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(lst)


def lst_to_bst(lst) -> Optional[TreeNode]:
    if not lst:
        return None
    it = iter(lst)
    root = TreeNode(next(it))
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            queue.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            queue.append(node.right)
    return root


def test_ex1():
    """
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
    """
    sol = Solution()
    # root = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15), TreeNode(7)))
    root = lst_to_bst([3, 9, 20, None, None, 15, 7])
    res = sol.levelOrder(root)


if __name__ == "__main__":
    test_ex1()
