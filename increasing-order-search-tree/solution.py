# leetcode
# https://leetcode-cn.com/problems/increasing-order-search-tree/
# 分析难点在于原地排

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def f(root, list1):
            if root is None:
                return
            else:
                f(root.left, list1)
                list1.append(root)
                f(root.right, list1)
        lst = []
        f(root, lst)

        p = lst[0]

        for i in lst[1:]:
            p.right = i
            p = p.right

        return p
