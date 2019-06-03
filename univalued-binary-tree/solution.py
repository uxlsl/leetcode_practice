# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def f(root,val):
            if root is None:
                return True
            if root.val == val:
                return f(root.left, val) and f(root.right, val)
            else:
                return False

        return f(root.val, root.val)
