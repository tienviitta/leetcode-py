from typing import Optional
from utils import TreeNode, bst_from_list, bst_to_list


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


def test_ex1():
    """
    Input: root = [4,2,7,1,3], val = 5
    Output: [4,2,7,1,3,5]
    """
    sol = Solution()
    root = bst_from_list([4, 2, 7, 1, 3])
    val = 5
    out = sol.insertIntoBST(root, val)
    ref = [4, 2, 7, 1, 3, 5]
    # TODO: Fix this?!
    res = bst_to_list(out)
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
