# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lst = []
        def f(node):
            if node:
                lst.append(node.val)
                f(node.left)
                f(node.right)

        f(root)
        lst = sorted(lst)
        val = float('inf')

        for i in range(len(lst)-1):
            if abs(lst[i+1] - lst[i]) < val:
                val = abs(lst[i+1] - lst[i])

        return val
