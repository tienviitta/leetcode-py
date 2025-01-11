from typing import Optional
from utils import TreeNode, bst_from_list, bst_to_list


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return root


def test_ex1():
    """
    Input: root = [4,2,7,1,3], val = 2
    Output: [2,1,3]
    """
    sol = Solution()
    lst = [4, 2, 7, 1, 3]
    val = 2
    ref = [2, 1, 3]
    root = bst_from_list(lst)
    out = sol.searchBST(root, val)
    res = bst_to_list(out)
    assert res == ref, "res: {}, ref: {}".format(res, ref)


if __name__ == "__main__":
    test_ex1()
