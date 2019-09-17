# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def f(root, val):
            if root:
                if root.left or root.right:
                    return f(root.left, 10 * val + root.val) + f(
                        root.right, 10 * val + root.val
                    )
                return 10 * val + root.val
            return 0

        return f(root, 0)
