from collections import deque
from typing import List, Optional

from utils import bst_from_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        queue = deque()
        if root:
            queue.append(root)
        while len(queue) > 0:
            llst = []
            for i in range(len(queue)):
                curr = queue.popleft()
                llst.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            lst.append(llst[-1])
        return lst


def test_ex1():
    """
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]
    """
    sol = Solution()
    # root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    root = bst_from_list([1, 2, 3, None, 5, None, 4])
    res = sol.rightSideView(root)
    ref = [1, 3, 4]
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex2():
    """
    Input: root = [1,2,3,4,null,null,null,5]
    Output: [1,3,4,5]
    """
    sol = Solution()
    # root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    root = bst_from_list([1, 2, 3, 4, None, None, None, 5])
    res = sol.rightSideView(root)
    ref = [1, 3, 4, 5]
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
    test_ex2()
