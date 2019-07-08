# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def f(root, lst):
            if root is not None:
                f(root.left,lst)
                lst.append(root.val)
                f(root.right,lst)

        lst = []
        f(root, lst)
        return f(root, lst)
