from typing import Optional
from utils import TreeNode, bst_from_list, bst_to_list


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the node to delete
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Find the minimum node at the right sub-tree
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)
        return root


def test_ex1():
    """
    Input: root = [5,3,6,2,4,null,7], key = 3
    Output: [5,4,6,2,null,null,7]
    """
    sol = Solution()
    root = bst_from_list([5, 3, 6, 2, 4, None, 7])
    # root = TreeNode(
    #     5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))
    # )
    val = 3
    out = sol.deleteNode(root, val)
    ref = [5, 4, 6, 2, None, None, 7]
    # TODO: Fix this?!
    res = bst_to_list(out)
    assert res == ref, "res: {}, ref: {}".format(res, ref)
    print(out)


if __name__ == "__main__":
    test_ex1()
