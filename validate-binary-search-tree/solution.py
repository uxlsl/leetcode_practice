# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def f(root, lst):
            if root:
                f(root.left, lst)
                lst.append(root.val)
                f(root.right, lst)

        lst = []
        f(root, lst)

        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                return False
        return True
