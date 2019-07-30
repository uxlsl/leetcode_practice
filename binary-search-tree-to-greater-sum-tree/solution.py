# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        total = 0
        def f(root):
            if root is None:
                return
            nonlocal total
            f(root.right)
            total += root.val
            root.val
            f(root.left)
        return f(root)
