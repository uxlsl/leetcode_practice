# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def f(root,val):
            if root is None:
                return None
            if root.val < val:
                if root.right:
                    f(root.right,val)
                else:
                    root.right = TreeNode(val)
            else:
                if root.left:
                    f(root.left,val)
                else:
                    root.left = TreeNode(val)
            return root

        return f(root, val)
