# leetcode 1022
# https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/submissions/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def f(n, path):
            if n is None:
                return 0
            elif n.left is None and n.right is None:
                return path << 1 | n.val
            else:
                path = path << 1 | n.val
                return f(n.left, path) + f(n.right, path)

        return f(root, 0)
