# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def f(root, L, R):
            if root:
                if root.val < L:
                    return f(root.right, L, R)
                elif root.val > R:
                    return f(root.left, L, R)
                else:
                    root.left = f(root.left, L, R)
                    root.right = f(root.right, L, R)
                    return root

        return f(root,L, R)
