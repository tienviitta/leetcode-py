from typing import List, Optional

from utils import TreeNode, bst_from_list, bst_to_list


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.inorder(root, lst)
        return lst

    def inorder(self, root: Optional[TreeNode], lst: List[int]):
        if not root:
            return
        self.inorder(root.left, lst)
        lst.append(root.val)
        self.inorder(root.right, lst)


def test_ex1():
    """
    Input: root = [1,null,2,3]
    Output: [1,3,2]
    """
    sol = Solution()
    # root = bst_from_list([1, None, 2, 3)
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    out = sol.inorderTraversal(root)
    # res = bst_to_list(out)
    # ref = [1, 3, 2]
    # assert res == ref, "res: {}, ref: {}".format(res, ref)


def test_ex2():
    """
    Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    Output: [4,2,6,5,7,1,3,9,8]
    """
    sol = Solution()
    root = bst_from_list([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
    out = sol.inorderTraversal(root)
    res = bst_to_list(out)
    ref = [4, 2, 6, 5, 7, 1, 3, 9, 8]
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex2()
