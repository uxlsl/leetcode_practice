# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def f(root):
            if root:
                yield root
                yield from f(root.left)
                yield from f(root.right)

        lst = list(f(root))
        first = lst[0]
        p = first

        for i in lst[1:]:
            p.right = i
            p.left = None
            p = i

        return first
