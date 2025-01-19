from typing import Optional

from utils import bst_from_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathSum = 0
        has = self.pathSum(root, pathSum, targetSum)
        return has

    def pathSum(self, root: Optional[TreeNode], pathSum: int, targetSum: int) -> bool:
        if not root:
            return False
        pathSum += root.val
        if not root.left and not root.right:
            return pathSum == targetSum
        if self.pathSum(root.left, pathSum, targetSum):
            return True
        if self.pathSum(root.right, pathSum, targetSum):
            return True
        return False


def test_ex1():
    """
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: true
    Explanation: The root-to-leaf path with the target sum is shown.
    """
    sol = Solution()
    root = bst_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    targetSum = 22
    res = sol.hasPathSum(root, targetSum)
    ref = True
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex2():
    """
    Input: root = [1,2,3], targetSum = 5
    Output: false
    Explanation: There are two root-to-leaf paths in the tree:
    (1 --> 2): The sum is 3.
    (1 --> 3): The sum is 4.
    There is no root-to-leaf path with sum = 5.
    """
    sol = Solution()
    root = bst_from_list([1, 2, 3])
    targetSum = 5
    res = sol.hasPathSum(root, targetSum)
    ref = False
    assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex3():
    """
    Input: root = [], targetSum = 0
    Output: false
    """
    sol = Solution()
    root = bst_from_list([])
    targetSum = 0
    res = sol.hasPathSum(root, targetSum)
    ref = False
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
    test_ex2()
    test_ex3()
